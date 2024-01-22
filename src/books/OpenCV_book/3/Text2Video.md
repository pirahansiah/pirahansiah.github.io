Convert Text to Video with Python! Text2Video by python and OpenCV  
source code: https://github.com/pirahansiah/farshid/blob/master/src/  
more: https://www.pirahansiah.com/projects-products/opencv_book  
#opencv #python

## convert text to video 
```python
import cv2
import numpy as np
fileName='line2video.py'
font=cv2.FONT_HERSHEY_SIMPLEX
font_scale=1
thickness=1
color=(255,255,255)
tab_size = 1 
textHeight = 50 
textX=10
textY=50
image = np.zeros((900,900,3), np.uint8)
with open(fileName, 'r') as f:
    lines = f.read().splitlines() 
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
video = cv2.VideoWriter(fileName+'_.mp4', fourcc, 1, (900,900))
for line1 in lines:
    line = line1.expandtabs(tab_size)  
    if textY<800:
        textY=textY+50
    else:
        image = np.zeros((900,900,3), np.uint8)
        textY=50
    (w, h), _ = cv2.getTextSize(line, font, 1, thickness)
    w=w+200
    scale = image.shape[1] / w
    scale = min(scale, 1.0)  
    textSize = cv2.getTextSize(line, font, scale, thickness)
    textWidth = textSize[0][0]
    cv2.putText(image, line, (5,textY), font, scale, color, thickness)
    textHeight += textSize[0][1] 
    video.write(image)
video.release()
# www.pirahansiah.com

```

![[text2video.png]]