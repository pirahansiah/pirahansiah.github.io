How to create a video with images in Python using OpenCV library. The OpenCV library is a powerful tool for computer vision. It can be used to create videos with images, and other types of media. This code creates a video with images. The images are resized to 3840x2160 pixels. The video is encoded with the FMP4 codec and has a frame rate of 15 frames per second.

## convert image to video 
```python
import cv2
import numpy as np
import glob
w=3840
h=2160
time_video_min=0.1
calcFrames=int(time_video_min*60*15)

def copyBig(small,big):
    center_y = big.shape[0]//2
    center_x = big.shape[1]//2
    h, w = small.shape[:2]
    roi_top = center_y - h//2
    roi_bottom = roi_top + h
    roi_left = center_x - w//2
    roi_right = roi_left + w
    roi = big[roi_top:roi_bottom, roi_left:roi_right]
    img1_resized = cv2.resize(small, (w, h)) 
    np.copyto(roi, img1_resized)
    # cv2.imshow("test",big)
    # cv2.waitKey(200)
    return big

img_array = []
for filename in glob.glob('images/*.png'):
    img = cv2.imread(filename)
    img=cv2.resize(img,(w,h))
    img_array.append(img)
qrcode_array = []
for filename in glob.glob('qrcode/*.png'):
    big_image=np.zeros(( h,w, 3),dtype=np.uint8) # np is not opencv the h,w is w,h
    img = cv2.imread(filename)
    img=cv2.resize(img,( 600,600))
    big_image=copyBig(img,big_image)
    qrcode_array.append(big_image)
out = cv2.VideoWriter('pirahansiah.mp4',cv2.VideoWriter_fourcc(*'FMP4'), 15,(w,h))


for j in range(len(img_array)): 
    for i in range(calcFrames):
        out.write(img_array[j])
for j in range(len(qrcode_array)): 
    for i in range(calcFrames):
        out.write(qrcode_array[j])
out.release()
```
