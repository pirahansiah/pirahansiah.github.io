# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# brew install gstreamer gst-plugins-base gst-plugins-good gst-plugins-bad gst-plugins-ugly
# conda install -c conda-forge gstreamer

import cv2

# Define GStreamer pipeline to grab video from a device
gst_str = (
    "autovideosrc ! "
    "videoconvert ! "
    "videoscale ! "
    "video/x-raw,format=(string)BGR,width=640,height=480 ! "
    "appsink"
)

# Create VideoCapture object
cap = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("VideoCapture not opened")
    exit(-1)

while True:
    ret, frame = cap.read()
    if not ret:
        print("empty frame")
        break

    cv2.imshow('GStreamer with OpenCV', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
