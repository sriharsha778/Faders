# Faders

Gesture-Based Human-Computer Interaction System 🎮✋

A computer control system using hand gestures powered by OpenCV, MediaPipe, and PyAutoGUI.

📌 Features
✅ Cursor Movement - Move the cursor by extending your index finger while keeping other fingers curled.
✅ Left Click - Touch thumb to index base.
✅ Right Click - Touch thumb to index middle.
✅ Drag & Drop - Touch thumb to index tip and hold.
✅ Scrolling - Touch index & middle fingers, curl the rest, and move up/down.
✅ Zoom In/Out - Curl all fingers on one hand, extend only index & thumb on the other, then move fingers apart/together.

🛠 Installation
1️⃣ Clone the repository
sh
Copy
Edit
git clone https://github.com/sriharsha778/Faders.git
cd Faders

2️⃣ Install dependencies
sh
Copy
Edit
pip install opencv-python mediapipe pyautogui numpy

3️⃣ Run the script
sh
Copy
Edit
python main.py


📌 Controls & Gestures
Gesture	Action
☝️ Index Extended	Move Cursor
👍 Thumb + Index Base	Left Click
👍 Thumb + Index Middle	Right Click
✊ Thumb + Index Tip	Drag & Drop
✌️ Index & Middle Touching	Scroll Up/Down
🤏 Zoom Gesture	Zoom In/Out (Slow & Smooth)

🖥 How It Works?
Uses OpenCV to capture the live webcam feed.
Detects hand landmarks with MediaPipe Hands.
Identifies gestures based on finger positions.
Performs corresponding mouse actions with PyAutoGUI.

⚡ Customization
Adjust zoom speed in zoom_threshold (default 20).
Modify cursor sensitivity in alpha (default 0.3).
Add more custom gestures inside detect_gestures().

📝 To-Do
 Add gesture-based text input
 Implement customizable gesture shortcuts
 Improve scrolling smoothness
🤝 Contributing
Got an idea? Found a bug? PRs & Issues are welcome! 🚀

Fork the repo
Create a feature branch (git checkout -b feature-name)
Commit changes (git commit -m "Added new feature")
Push to GitHub (git push origin feature-name)
Open a Pull Request
📜 License
This project is open-source and available under the MIT License.

🌟 Show Some Love!
⭐ Star this repo if you find it useful! 😊
