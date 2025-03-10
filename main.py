import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# Screen size
screen_width, screen_height = pyautogui.size()

# Initialize MediaPipe Hands
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=0,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6,
    max_num_hands=2
)

# Click Cooldown
click_cooldown = 1
last_left_click_time = 0
last_right_click_time = 0

# Control variables
dragging = False
scrolling = False
initial_scroll_y = None
cursor_position = np.array([0, 0])
zooming = False
initial_zoom_distance = None

# Smooth cursor movement parameters
alpha = 0.3  # Smoothing factor (0.1 - 0.3 recommended)

# Zoom Sensitivity (Increase this value to slow down zooming)
zoom_threshold = 20


def fast_distance(p1, p2):
    """Fast Euclidean distance calculation."""
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def is_finger_curled(landmarks, finger_tip, finger_base):
    """Check if a finger is curled by comparing tip position with base."""
    return landmarks[finger_tip][1] > landmarks[finger_base][1]


def move_cursor(landmarks):
    """Move the cursor smoothly if index is extended and other fingers are curled."""
    global cursor_position

    if 8 in landmarks:
        index_tip = landmarks[8]

        if (
                not is_finger_curled(landmarks, 8, 6)
                and is_finger_curled(landmarks, 12, 10)
                and is_finger_curled(landmarks, 16, 14)
                and is_finger_curled(landmarks, 20, 18)
        ):
            x, y = index_tip
            screen_x = np.interp(x, (50, 590), (0, screen_width))
            screen_y = np.interp(y, (50, 430), (0, screen_height))

            # Exponential Moving Average (EMA) Smoothing
            cursor_position[0] = alpha * screen_x + (1 - alpha) * cursor_position[0]
            cursor_position[1] = alpha * screen_y + (1 - alpha) * cursor_position[1]

            pyautogui.moveTo(*cursor_position, duration=0.01)  # Faster response


def detect_gestures(landmarks_list):
    """Detect gestures and perform corresponding actions."""
    global last_left_click_time, last_right_click_time, dragging, scrolling, initial_scroll_y, zooming, initial_zoom_distance

    current_time = time.time()
    hand_count = len(landmarks_list)

    if hand_count == 1:
        landmarks = landmarks_list[0]

        thumb_tip = landmarks.get(4)
        index_tip = landmarks.get(8)
        middle_tip = landmarks.get(12)

        move_cursor(landmarks)

        # Left Click
        if thumb_tip and index_tip and fast_distance(thumb_tip, landmarks[5]) < 40:
            if current_time - last_left_click_time > click_cooldown:
                pyautogui.click()
                last_left_click_time = current_time

        # Right Click
        if thumb_tip and middle_tip and fast_distance(thumb_tip, middle_tip) < 40:
            if current_time - last_right_click_time > click_cooldown:
                pyautogui.rightClick()
                last_right_click_time = current_time

        # Drag & Drop
        if index_tip and thumb_tip and fast_distance(index_tip, thumb_tip) < 40:
            if not dragging:
                pyautogui.mouseDown()
                dragging = True
        else:
            if dragging:
                pyautogui.mouseUp()
                dragging = False

        # Scroll
        if (
                not is_finger_curled(landmarks, 8, 6)
                and not is_finger_curled(landmarks, 12, 10)
                and is_finger_curled(landmarks, 16, 14)
                and is_finger_curled(landmarks, 20, 18)
        ):
            if not scrolling:
                initial_scroll_y = index_tip[1]
                scrolling = True

            scroll_delta = initial_scroll_y - index_tip[1]
            pyautogui.scroll(int(scroll_delta * 0.5))

        else:
            scrolling = False
            initial_scroll_y = None

    elif hand_count == 2:
        hand1, hand2 = landmarks_list

        def is_hand_fully_curled(hand):
            """Check if all fingers are curled on one hand."""
            return all(is_finger_curled(hand, i, i - 2) for i in [8, 12, 16, 20])

        def is_zoom_ready_hand(hand):
            """Check if only the index and thumb are extended, other fingers curled."""
            return (
                not is_finger_curled(hand, 8, 6) and  # Index Extended
                not is_finger_curled(hand, 4, 2) and  # Thumb Extended
                is_finger_curled(hand, 12, 10) and  # Middle Curled
                is_finger_curled(hand, 16, 14) and  # Ring Curled
                is_finger_curled(hand, 20, 18)  # Pinky Curled
            )

        if is_hand_fully_curled(hand1) and is_zoom_ready_hand(hand2):
            zoom_hand = hand2
        elif is_hand_fully_curled(hand2) and is_zoom_ready_hand(hand1):
            zoom_hand = hand1
        else:
            zooming = False
            return

        thumb_tip = zoom_hand.get(4)
        index_tip = zoom_hand.get(8)

        if thumb_tip and index_tip:
            zoom_distance = fast_distance(thumb_tip, index_tip)

            if not zooming:
                initial_zoom_distance = zoom_distance
                zooming = True

            if zoom_distance - initial_zoom_distance > zoom_threshold:
                pyautogui.hotkey('ctrl', '+')
                initial_zoom_distance += zoom_threshold  # Slow down zoom-in

            elif zoom_distance - initial_zoom_distance < -zoom_threshold:
                pyautogui.hotkey('ctrl', '-')
                initial_zoom_distance -= zoom_threshold  # Slow down zoom-out


def process_frame(frame):
    """Processes each frame and detects gestures."""
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    processed = hands.process(frameRGB)
    landmarks_list = []

    if processed.multi_hand_landmarks:
        for hand_landmarks in processed.multi_hand_landmarks:
            landmark_dict = {}
            for id, lm in enumerate(hand_landmarks.landmark):
                x, y = int(lm.x * 640), int(lm.y * 480)
                landmark_dict[id] = (x, y)
            landmarks_list.append(landmark_dict)

    detect_gestures(landmarks_list)


def main():
    """Runs the gesture control system."""
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            process_frame(frame)
            cv2.imshow('Gesture Control', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
