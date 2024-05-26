import cv2
import numpy as np

# Load the hand texture images
textures = {
    "texture1": cv2.imread("/Users/farshid/Documents/2024May/img/farshid.png"),
    "texture2": cv2.imread("/Users/farshid/Documents/2024May/img/farshid.png"),
    "texture3": cv2.imread("/Users/farshid/Documents/2024May/img/farshid.png")
}

# Function to apply texture to a region of an image
def apply_texture(image, texture, mask):
    texture_resized = cv2.resize(texture, (mask.shape[1], mask.shape[0]))
    masked_texture = cv2.bitwise_and(texture_resized, texture_resized, mask=mask)
    inverted_mask = cv2.bitwise_not(mask)
    masked_image = cv2.bitwise_and(image, image, mask=inverted_mask)
    return cv2.add(masked_image, masked_texture)

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range of skin color in HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Create a mask for skin color
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Assume the hand is touching something triggering texture1
    texture_key = "texture1"

    # Apply texture if a hand is detected
    if texture_key in textures:
        frame = apply_texture(frame, textures[texture_key], mask)

    # Display the resulting frame
    cv2.imshow('Hand Texture', frame)

    # Press 'q' to quit the webcam
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
