import cv2
import numpy as np
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Function to apply texture to a region of an image
def apply_texture(image, texture, mask):
    texture_resized = cv2.resize(texture, (mask.shape[1], mask.shape[0]))
    masked_texture = cv2.bitwise_and(texture_resized, texture_resized, mask=mask)
    inverted_mask = cv2.bitwise_not(mask)
    masked_image = cv2.bitwise_and(image, image, mask=inverted_mask)
    return cv2.add(masked_image, masked_texture)

# Function to get the texture at the point
def get_texture_at_point(frame, x, y):
    patch_size = 50
    x_start = max(0, x - patch_size // 2)
    y_start = max(0, y - patch_size // 2)
    x_end = min(frame.shape[1], x + patch_size // 2)
    y_end = min(frame.shape[0], y + patch_size // 2)
    
    patch = frame[y_start:y_end, x_start:x_end]
    if patch.size == 0:
        return None
    return patch

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
            
            # Get the texture at the pointing location
            texture_patch = get_texture_at_point(frame, x, y)
            if texture_patch is not None:
                # Apply the detected texture to the hand skin region
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                lower_skin = np.array([0, 20, 70], dtype=np.uint8)
                upper_skin = np.array([20, 255, 255], dtype=np.uint8)
                skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)
                frame = apply_texture(frame, texture_patch, skin_mask)
    
    # Display the resulting frame
    cv2.imshow('Hand Texture', frame)
    
    # Press 'q' to quit the webcam
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
