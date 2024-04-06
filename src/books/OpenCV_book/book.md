## OpenCV 
* introduction
* chapter 0
	* ![[Introduction]]
	* ![[Install in Python]]
	* ![[Type in OpenCV]]
* chapter 1
	* ![[Foundations]]
* chapter 2
* chapter 3: some example projects, practical, useful, ...
	* [[image2video]]
	* [[Text2Video]]
	* [[image2pdf]]
* chapter 4
	* [[test]]
	* [[OpenCV_book/4/DL]]
	* [[OpenCV_book/4/Makefile|Makefile]]
	* [[md/optimization]]
	* 
* chapter 5
	* [[mindMap]]

Essential Python Tips And Tricks For advance computer vision Programmers
Essential Tips And Tricks For compiling code computer vision projects 


- How to optimize your code for speed and efficiency
- How to debug your code and fix errors
- How to use OpenCV with other libraries and frameworks
- How to troubleshoot common problems
- How to extend the functionality of OpenCV with custom code
https://sites.google.com/d/1oONostEwmGxk6AZgInugsHXr86PKYp_0/p/1akmTgveL8X6R1wV9Ot_xAyJlmFVZUGfx/edit


steps

parts detection

resize with keep aspects ratio

ML

perform detection

semantic segmentation

transfer to original coordinates

  

challenges

class imbalance

class definition 

use class in between 

inconstant annotations

  

color augmentation

RGB shift

random brightness and contrast

shapen

hue, saturation, value

  

Why manually data augmentation?

because we want to control data augmentation. for example change rotation angle to just a few or change color only in one range

  

Photogrammetry 3D models

Neural Radiance Fields (NERF), and Instant-NGP – Future of photogrammetry?

NeRF in the Wild: Neural Radiance Fields for Unconstrained


=========
- the image size and kernel size need to depended. the best way is to use the one variable to define the size of the image and kernel together.
    
- the coordinate of the image start at top left of the image/display
    

- in order to change it to the normal coordinate you can use
    

- grid of points; two matrix to X , Y coordinate
    
- subtract half of W, H from X, Y in order to have normal coordinate system for our image
    
- now we have cartesian coordinate 
    
-   
    
- cartesian coordinate to polar coordinate
    

- تبدیل فضای کارتزین به پولار در خیلی از برنامه های پردازش تصویر کارایی دارد. برای پیدا کردن ترشلد ها هم می توان استفاده کرد
    
- in MATLAB we can use ":"for example MatrixA(:) which means all entity of the matrix no mater how many dimensions we have but if we want to implemented in Python we can use numpy.flatten(). 
    
- in the MATLAB the round is different from python. if you want same result you need implement the rand function by yourself.
    
- imge_mask=np.ones_like(image_source)*255
    
- imge_mask=imge_mask.astype(np.uint8)
    
- imge_mask=imge_mask.flatten() ??? .ravel()
    
- .asarray
    
- np.logical_and( 1, 2)
    
- indexes=[index for index in range(len(array1)) if array1[index] == True]
    
- cv2.bitwise_not(yyy)


========
[Sharpness](https://en.wikipedia.org/wiki/Sharpness_(visual)) ,[Noise](https://en.wikipedia.org/wiki/Image_noise), [Dynamic range](https://en.wikipedia.org/wiki/Dynamic_range), [Tone reproduction](https://en.wikipedia.org/wiki/Tone_reproduction) , [Contrast](https://en.wikipedia.org/wiki/Contrast_(vision)), [Color](https://en.wikipedia.org/wiki/Color), [Distortion](https://en.wikipedia.org/wiki/Distortion_(optics)) , [DSLR lenses](https://en.wikipedia.org/wiki/Lenses_for_SLR_and_DSLR_cameras), [Vignetting](https://en.wikipedia.org/wiki/Vignetting), [Exposure](https://en.wikipedia.org/wiki/Exposure_(photography)), Lateral [chromatic aberration](https://en.wikipedia.org/wiki/Chromatic_aberration) (LCA), [Lens flare](https://en.wikipedia.org/wiki/Lens_flare), Color, [Artifacts](https://en.wikipedia.org/wiki/Compression_artifact)
===========
- OpenCV: A computer vision (CV) library filled with many different computer vision functions and other useful image and video processing and handling capabilities.
- MQTT: A publisher-subscriber protocol often used for IoT devices due to its lightweight nature. The paho-mqtt library is a common way of working with MQTT in Python.
- Publish-Subscribe Architecture: A messaging architecture whereby it is made up of publishers, that send messages to some central broker, without knowing of the subscribers themselves. These messages can be posted on some given “topic”, which the subscribers can then listen to without having to know the publisher itself, just the “topic”.
- Publisher: In a publish-subscribe architecture, the entity that is sending data to a broker on a certain “topic”.
- Subscriber: In a publish-subscribe architecture, the entity that is listening to data on a certain “topic” from a broker.
- Topic: In a publish-subscribe architecture, data is published to a given topic, and subscribers to that topic can then receive that data.
- FFmpeg: Software that can help convert or stream audio and video. In the course, the related ffserver software is used to stream to a web server, which can then be queried by a Node server for viewing in a web browser.
- Flask: A [Python framework](https://www.google.com/url?q=https%3A%2F%2Fwww.fullstackpython.com%2Fflask.html&sa=D&sntz=1&usg=AOvVaw0RsnQtaW38wrzRz9BN0Ud_) useful for web development and another potential option for video streaming to a web browser.
- Node Server: A web server built with Node.js that can handle HTTP requests and/or serve up a webpage for viewing in a browser.
---------
Edge, IoT

 

The OpenVINO™ Toolkit’s name comes from “Open Visual Inferencing and Neural Network Optimization”.
-------
