# Real-time Camera-Based Gesture Control System for Games  

## **Overview**  
This project enables players to control PC games using **hand gestures** via a standard webcam. It uses **computer vision** to detect gestures in real time and converts them into **gamepad inputs**, allowing seamless gameplay without special hardware or game code modifications.  

---

## **Features**  
- Real-time gesture detection  
- Works with any game supporting gamepad input  
- No additional hardware required  
- Simple and user-friendly interface  

---

## **Requirements**  
**Hardware:**  
- PC with Intel i3 or above  
- Minimum 4GB RAM  
- HD webcam (720p or above)  

**Software:**  
- Python 3.x  
- OpenCV  
- MediaPipe
- Pyautgui
- Gamepad API or equivalent library  

---

## **How It Works**  
1. Captures real-time video from the webcam  
2. Detects hand landmarks using **MediaPipe**  
3. Classifies gestures using rule-based or ML models  
4. Maps gestures to standard gamepad inputs for controlling games  

---

## **Future Scope**  
- Support for VR gaming environments  
- Multiple gesture combinations for complex game controls  
- Hybrid control system combining gestures and voice commands  
