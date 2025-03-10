# Faders - Gesture-Based Human-Computer Interaction System  

🚀 **Faders** is an advanced **gesture-based system** that allows you to control your computer using **hand gestures** via a webcam. It leverages **OpenCV, MediaPipe, and PyAutoGUI** to recognize hand movements and map them to actions like mouse control, clicks, scrolling, and zooming.  

## 📌 Features  
- 🖱️ **Cursor Control** - Move the mouse by extending your index finger while keeping other fingers curled.  
- 🔘 **Left Click** - Touch your **thumb to the base of your index finger**.  
- ⚪ **Right Click** - Touch your **thumb to the tip of your middle finger**.  
- 🎯 **Drag & Drop** - Touch your **thumb to the tip of your index finger** and move.  
- 🔄 **Scrolling** - Touch your **index and middle fingers together**, curl other fingers, and move up/down.  
- 🔍 **Zooming** - One hand fully curled + Other hand with only **index & thumb extended** → Adjust zoom by changing their distance.  

## 🛠️ Installation  

### Step 1: Clone the Repository  
git clone https://github.com/sriharsha778/Faders.git
cd Faders

### Step 2: Install Dependencies  
Ensure you have Python 3 installed, then install the required libraries:  
pip install opencv-python mediapipe pyautogui numpy

### Step 3: Run the Application  
python main.py

## 📷 How It Works  
1. Starts webcam and tracks hand gestures using **MediaPipe Hands**.  
2. Uses **Euclidean distance** to detect specific finger positions.  
3. Maps recognized gestures to **mouse and keyboard actions**.  
4. Implements **smoothing techniques** for precise cursor movement.  

## 🔧 Tech Stack  
- **OpenCV** → Video capture & processing  
- **MediaPipe** → Hand tracking & gesture recognition  
- **PyAutoGUI** → Simulating mouse & keyboard actions  
- **NumPy** → Mathematical operations & smoothing  

## 📌 Gesture Controls  

| Gesture | Action | Condition |  
|---------|--------|-----------|  
| **Cursor Movement** | Move Mouse | Extend index, curl other fingers |  
| **Left Click** | Click | Thumb touches index base |  
| **Right Click** | Right Click | Thumb touches middle tip |  
| **Drag & Drop** | Hold & Move | Thumb touches index tip |  
| **Scrolling** | Scroll Up/Down | Index & Middle fingers touch, move up/down |  
| **Zoom In/Out** | Zoom | One hand curled, other with index+thumb extended |  


## 🤝 Contribution  
Want to improve Faders? Follow these steps:  
1. Fork the repo 📌  
2. Create a new branch 🛠  
3. Make changes & commit 🚀  
4. Submit a Pull Request 🤝  

## 📜 License  
This project is **open-source** and licensed under the **MIT License**.  

---

🔥 **Enjoy a touch-free, futuristic experience!** 🚀
