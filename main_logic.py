import cv2
import mediapipe as mp
import pyautogui


mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)
last_action = None


GAS_BTN = (1689, 900)  
BRAKE_BTN = (214, 900)

def detect_gesture(landmarks):
    finger_tips = [8, 12, 16, 20]
    finger_dips = [6, 10, 14, 18]

    open_fingers = 0
    for tip, dip in zip(finger_tips, finger_dips):
        if landmarks[tip].y < landmarks[dip].y:  
            open_fingers += 1

    if open_fingers == 0:       
        return "brake"
    elif open_fingers >= 4:     
        return "accelerate"
    else:
        return "none"

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    action = "none"

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark
            action = detect_gesture(landmarks)

    if action != last_action:
        if action == "accelerate":
            pyautogui.mouseDown(GAS_BTN)
            #pyautogui.mouseUp(BRAKE_BTN)  # release brake if pressed
            print("Accelerating (Open Palm)")
        elif action == "brake":
            pyautogui.mouseDown(BRAKE_BTN)
 
            print("Braking (Fist)")
        else:
            pyautogui.mouseUp(GAS_BTN)
            pyautogui.mouseUp(BRAKE_BTN)
            print("Neutral")

        last_action = action

    cv2.putText(frame, f"Action: {action}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Hill Climb Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
