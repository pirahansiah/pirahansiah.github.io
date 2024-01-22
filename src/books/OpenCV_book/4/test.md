
# cvtest: Computer Vision Test

## Unit Test, Integration Test, System Test, Acceptance Test for Computer Vision and Deep Learning

Do you want to test your output of computer vision application which is video or images?

## Standard test for computer vision application

There isn't any standard test for computer vision program. I wrote many test by myself and I would like to share some of them here. For example, I write a program to test docker and check the processing time, memory usage, CPU usage, etc. In computer vision application sometime you need to check the output which is the image. How do you want to check it. I write some program to check the output which is the image and compare the ground truth. I check some well known methods such as PSNR, SSIM, Image quality, distortion, brightness, sharpness, etc. Furthermore, I check much different hardware and write some test for computer vision application base on different hardware architecture and Evaluation hardware.

Do you want to know your program Automatically adjusting brightness of image in the right way?, How do you know using generic sharpening kernel to remove blurriness is working?, How to do check FPS process?, Which OCR system work better for your input image?

[https://github.com/pirahansiah/cvtest/blob/main/README.md](https://github.com/pirahansiah/cvtest/blob/main/README.md) 

  

check S3 bucket in AWS for image and video files and versioning 

Check Docker load balancer, memory usage, ...

GPU

In general I would create a wrapper/adapter that only exposes the needed functionality of such an external dependency. Apart from being able to easer adapt to changes of the external dependency, we can also mock the adapter in our tests and let it do things we could not do so easily with the dependency itself. For our example, we could it have return a predefined image in our test and it is also easier to test if our code behaves properly in presence of failures (that are usually hard to trigger with the real thing.






functional requirements: The module must 

- test opencv input/output image
    
- allow to check grand truth image and output image
    
- maintain a library of all comparison SSIM, PSNR, ...
    
- allow to choose different comparison algorithms: PSNR, SSIM, ...
    

non functional requirements: the module should be ... (maintainability, reliability, usability, availability)

- simple library attached to project
    
- fast
    
- update-able 
    

FURPS requirements:

- functionality:  SSIM, PSNR,
    
- usability: attached to the project as a class test
    
- reliability: assert in C++ 
    
- performance: real-time 
    
- support-ability: simple class with all functions 
    

use cases: 

- title: developer test image processing functions by see ground truth image and output image differences 
    
- primary actor: computer vision developer 
    
- success scenario: check and see differences between ground truth image and output image by different matrix such as SSIM, PSNR, ... 
    

  

user story: 

as a computer vision developer i want to test my output image so that I can see ground truth image and my output image differences

