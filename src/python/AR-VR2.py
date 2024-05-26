import cv2
import numpy as np
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame and find hands
    result = hands.process(rgb_frame)
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw hand landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Get the coordinates of the index finger tip (landmark 8)
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            
            # Convert normalized coordinates to pixel coordinates
            h, w, _ = frame.shape
            x = int(index_finger_tip.x * w)
            y = int(index_finger_tip.y * h)
            
            # Draw a circle at the index finger tip
            cv2.circle(frame, (x, y), 10, (0, 255, 0), cv2.FILLED)
            
            # Display the coordinates
            cv2.putText(frame, f"Pointing at: ({x}, {y})", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('Finger Pointing Detection', frame)
    
    # Press 'q' to quit the webcam
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
