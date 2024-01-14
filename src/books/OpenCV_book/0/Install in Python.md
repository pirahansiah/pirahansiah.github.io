```
pip install opencv-python​
```
Install OpenCV in python is easy and just need few steps. 
Based on Python 3.11 you can install OpenCV 5 with below commands.
```python
pip install opencv-python
pip install opencv-contrib-python
Pip install pirahansiah
conda install -c conda-forge ffmpeg
brew install gstreamer gst-plugins-base gst-plugins-good gst-plugins-bad gst-plugins-ugly
conda install -c conda-forge gstreamer
```
The `pip install opencv-python` will be install OpenCV 5 and in most cases it all you need. However, if you want to use other advanced method which may not license free you can install extra package of OpenCV by using `pip install opencv-contrib-python` command. For demo purposes I created a package for simplify running demo function without entering a lot of codes `Pip install pirahansiah`. if you use conda and you want to use ffmpeg (a package for multimedia) you can use `conda install -c conda-forge ffmpeg` command. 

## OpenCV import
For the OpenCV you need to import `cv2`
`import cv2`
And you may need two other packages 
`import matplotlib.pyplot as plt`
`import numpy as np`

# Build OpenCV in Mac with QT, Gstreamer Support

## Install dependencies
```
brew install cmake 
brew install qt5 
brew install gstreamer gst-plugins-base gst-plugins-good gst-plugins-bad gst-plugins-ugly gst-libav 
pip3 install numpy
```

## Download OpenCV source code
```
git clone https://github.com/opencv/opencv.git
cd opencv
git checkout master
cd ..
```

```
git clone https://github.com/opencv/opencv_contrib.git
cd opencv_contrib
git checkout master
cd ..
```

## Configure with require flags
```
mkdir build_opencv
cd build_opencv
```

```
brew info qt5
export QT5PATH=/Users/farshid/Qt/5.15.10/clang_64/


cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D BUILD_opencv_python2=OFF \
    -D BUILD_opencv_python3=ON \
    -D OPENCV_ENABLE_NONFREE=ON \
    -D PYTHON3_EXECUTABLE=$(which python3) \
    -D PYTHON3_INCLUDE_DIR=$(python3 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \
    -D PYTHON3_PACKAGES_PATH=$(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") \
    -D WITH_GSTREAMER=ON \
    -D WITH_OPENGL=ON \
    -D CMAKE_PREFIX_PATH=$QT5PATH \
    -D CMAKE_MODULE_PATH="$QT5PATH"/lib/cmake \
    -D BUILD_EXAMPLES=ON ../opencv
```

## Build and Install

```
make -j$(sysctl -n hw.physicalcpu)
make install

```

```
python3 -c "import cv2; print(cv2.__version__)"
```



```python
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
```