## Introduction 
Computer vision is the study of processing and analyzing images and videos for information. 

OpenCV handles tasks like filtering, object detection, face recognition, and deep learning. It works with TensorFlow, PyTorch, and Caffe. OpenCV is free and open source, compatible with Linux, Windows, and Mac OS X. 

OpenVINO optimizes deep learning models from various frameworks, deploys them on Intel hardware, and enhances performance and efficiency for computer vision applications on Intel devices.

## The history of OpenCV is as follows
- Beta: OpenCV had its initial beta release in 1999, followed by five beta releases between 2001 and 2005.
- 1.0.0: The first stable version of OpenCV, version 1.0.0, was released in 2006.
- 2.0.0: The second major version, 2.0.0, was released in 2009 and was implemented in C++.
- 3.0.0: The third major version, 3.0.0, was released in 2015. It was known for being the fastest and most stable version at that time.
- 4.0.0: In 2018, OpenCV released version 4.0.0, which introduced deep learning capabilities.
- 4.5.x: In 2021, OpenCV released the 4.5.x series, which brought enhancements in 3D capabilities and support for the RISC-V architecture.
- 5.0.0: The upcoming major version, 5.0.0, is scheduled to be released in 2023.

These milestones highlight the progression of OpenCV, showcasing its evolution and incorporation of various features and improvements over the years.




---
created: 2022-09-21T09:09:34+02:00
updated: 2023-05-06T22:53:15+02:00
---
![[cover.pdf]]
2023
Basic of Image Processing Programming by OpenCV using Python
Farshid PirahanSiah


## Impressive Computer Vision with Python!
Basic of Image Processing Programming by OpenCV 5 using Python 3.11
Understand the concepts of image processing with Python and create applications using OpenCV 5. 

The Image Processing field is one of the most interesting and exciting subjects of computer science and robotic. This field focuses on how computers perceive and process image and video data. The technologies of this field are essential for our future. With computer vision we are able to make unreadable texts readable. We are also able to recognize faces and other objects in real time. We can apply filters, transformations and lots of effects. If you want to be a part of this movement instead of being overrun by it, you should learn these skills as fast as possible!

introduces C++ programming language, IDEs for Windows, and digital image processing. It also illustrates the theoretical foundations of Image processing followed by advanced operations in image processing. You'll then review image processing.


  Updated for OpenCV 5, this book covers the latest on depth cameras, 3D navigation, deep neural networks, and Cloud computing, helping you solve real-world computer vision problems with practical code

#### Key Features

-   Build powerful computer vision applications in concise code with OpenCV 5 and Python 3
-   Learn the fundamental concepts of image processing, object classification, and 2D and 3D tracking
-   Train, use, and understand machine learning models, and deploy them in the Cloud

#### Book Description

Computer vision is a rapidly evolving science in the field of artificial intelligence, encompassing diverse use cases and techniques. This book will not only help those who are getting started with computer vision but also experts in the domain. You'll be able to put theory into practice by building apps with OpenCV 5 and Python 3.

You'll start by setting up OpenCV 5 with Python 3 on various platforms. Next, you'll learn how to perform basic operations such as reading, writing, manipulating, and displaying images, videos, and camera feeds. From taking you through image processing, video analysis, depth estimation, and segmentation, to helping you gain practice by building a GUI app, this book ensures you'll have opportunities for hands-on activities. You'll tackle two popular challenges: face detection and face recognition. You'll also learn about object classification and machine learning, which will enable you to create and use object detectors and even track moving objects in real time. Later, you'll develop your skills in augmented reality and real-world 3D navigation. Finally, you'll cover ANNs and DNNs, learning how to develop apps for recognizing handwritten digits and classifying a person's gender and age, and you'll deploy your solutions to the Cloud.

By the end of this book, you'll have the skills you need to execute real-world computer vision projects.

#### What you will learn

-   Install and familiarize yourself with OpenCV 5's Python 3 bindings
-   Understand image processing and video analysis
-   Use a depth camera to distinguish foreground and background regions
-   Detect and identify objects, and track their motion in videos
-   Train and use your own models to match images and classify objects
-   Detect and recognize faces, and classify their gender and age
-   Build augmented reality applications, and navigate the real 3D world
-   Train neural networks and deploy them as Cloud-based solutions

#### Who This Book Is For

This OpenCV book is a good fit for Python programmers who want to get started with computer vision and machine learning. This book will also be useful for Computer vision and AI/ML developers who want to expand their OpenCV skills as well as experts who want to stay up-to-date with OpenCV 5.

#### Table of Contents

1.  Setting Up OpenCV
2.  Handling Files, Cameras, and GUIs
3.  Processing Images with OpenCV
4.  Depth Estimation and Segmentation
5.  Detecting and Recognizing Faces
6.  Retrieving Images and Searching Using Image Descriptors
7.  Building Custom Object Detector
8.  Tracking Objects
9.  Camera Models and Augmented Reality
10.  3D Reconstruction and Navigation
11.  NeuraNetworks with OpenCV - an Introduction
12.  OpenCV Applications at Scale

### After Reading This Book You Will Have The Following Skills:

  
• Understanding computer vision and visual computing  
• Understanding color schemes (RGB, BGR, HSV)  
• Making unreadable texts readable again with thresholding  
• Extracting essential information out of images and videos  
• Edge detection  
• Template matching and feature matching  
• Movement detection in videos  
• Professional object recognition with OpenCV  
  
  What You'll Learn  

-   Get started with Raspberry Pi and Python
-   Understand Image Processing with Pillow
-   See how image processing is processed using Numpy and Matplotlib
-   Use Pi camera and webcam



### Master Computer Vision with Python and OpenCV!


Who This Book Is ForRaspberry Pi and IoT enthusiasts, and Python and Open Source professionals

In this seventh volume of The Python Bible, we will build on the skills and knowledge of the previous volumes. You will receive a well-written and detailed book that will help you to become a computer vision expert in Python. You will learn to do many impressive things like making poorly lit texts readable, movement detection in videos and professional object recognition. In this book you will learn step-by-step, how to realize these projects.


---
# Introduction 
Computer vision is the transformation of data from a still or video camera into either a decision or a new representation. All such transformations are done for achieving some particular goal.  OpenCV can work with many different deep learning frameworks to run as an inference engine.  
OpenCV (Open Source Computer Vision) is a library, real-time computer vision, developed by Intel, free, support deep learning frameworks TensorFlow, PyThorch, Caffe. OpenCV is an open source computer vision library and runs under Linux, Windows and Mac OS X. (see http://opensource.org).  

## History of OpenCV
* Beta  1999; (5 betas 2001-2005)
* 1.0.0 version was released in 2006
* 2.0.0 version was released in 2009 (C++)
* 3.0.0 version was released in 2015 (fastest, stable)
* 4.0.0 version was released in 2018 (deep learning)
* 4.5.x version was released in 2021 (3D, RISC-V)
* 5.0.0 beta was released in 2022

## OpenCV Point representation 
x=columns =width and y=rows = height

```cpp
0/0---column--->
 |
 |
row
 |
 |
 v
```

```cpp
0/0---X--->
 |
 |
 Y
 |
 |
 v
```
  ![[Pasted image 20221130155345.png]]
  ![[Pasted image 20221130164517.png]]
![[Pasted image 20221201152045.png]]
BGR order if you used cv2. imread()

## Type in OpenCV
  
* CV_8U - 8-bit unsigned integers ( 0..255 )
* CV_8S - 8-bit signed integers ( -128..127 )
* CV_16U - 16-bit unsigned integers ( 0..65535 )
* CV_16S - 16-bit signed integers ( -32768..32767 )
* CV_32S - 32-bit signed integers ( -2147483648..2147483647 )
* CV_32F - 32-bit floating-point numbers ( -FLT_MAX..FLT_MAX, INF, NAN )
* CV_64F - 64-bit floating-point numbers ( -DBL_MAX..DBL_MAX, INF, NAN )
