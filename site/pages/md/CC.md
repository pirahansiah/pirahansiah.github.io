![[a.excalidraw.svg]]

![[ChatGPT]]

# My research about camera calibration:

Geometric Analysis, Calibration Patterns, MATLAB, Python, C++, OpenCV, Subpixel Precision. A C++ implemented algorithm was used for high-speed, high-accuracy corner detection within calibration patterns, focusing on rotation and orientation. The process was refined by subpixel accuracy and noise reduction techniques.

## Camera Calibration

In computer vision methods, image information from cameras can yield geometric information pertaining to three-dimensional objects. The correlation between the topographical point and camera image pixel is necessary for camera calibration. Hence, the camera's parameters, which constitute the geometric model of camera imaging, are utilized to establish the association among the 3D geometric location of one point and its consistent point in an image. Typically, experiments are conducted to obtain the aforementioned parameters and relevant evaluation, which is a process called camera calibration.
Image information from cameras can be well utilized to extract the geometric information of a 3D object. The procedure of estimating the parameters of the pinhole camera model is called camera calibration. The more accurate the estimated parameters, the better the compensation that can be performed for the next stage of the application. In the data collection stage, a camera will take photos of camera calibration objects. The current methods simply create images upon the detection of the calibration pattern. Nevertheless, the consensus in rare cases is that accurate camera calibration involves pure rotation and requires sharp images. Recent breakthrough methods, such as Zhang's method, use a fixed threshold to elucidate points of difference between the frames and pre-setting variables, where slope information for image frame selection in the camera calibration phase has been neglected.
There are three main categories of camera calibration methods whereby a number of algorithms have been proposed for each category's methods, namely known object-based camera calibration, camera auto-calibration method, and stereo vision-based camera calibration. Fig. 1 shows the classification of camera calibration methods and also highlights the popular methods in camera calibration.
Camera resectioning (Geometric camera calibration) estimates the parameters of a lens and image sensor of a camera. These factors are used for correcting lens distortion, measuring the size of an object in world units, determining the location of the camera in a scene. These tasks are used in applications such as machine vision, image processing to identify and calculate objects or distances. They are also used in robots, navigation systems, and 3-D scene reconstruction. Without any knowledge of the calibration of the cameras, it is impossible to do better than projective reconstruction.
Noninvasive scene measurement tasks require a calibrated camera model. Camera calibration is the process of approximating the parameters of a pinhole camera model for a given photograph or video.


## Camera Calibration Methods:

• Active Vision Calibration: Utilizes active vision to obtain images for calibration by observing camera frames from specific positions. It solves camera parameters linearly through known motion track images. This approach includes calibration based on three-orthogonal translational motion and orthogonal rotation methods based on planar homography.
• Calibration with Known Object: Traditional methods use objects like chessboards or other calibration patterns. Techniques include linear transformation calibration, dual-plane calibration, and Zhang's calibration method. Zhang's method is notable for using multiple images of a plane from different angles to extract camera parameters against radial distortion.

## Key Concepts in Camera Calibration:

• Internal and External Parameters: Calibration involves estimating these parameters to correct for lens distortion, measure object sizes, and position the camera within a scene.
• Self-Calibration: This method doesn't rely on specific calibration objects but utilizes the camera's movement through a scene to determine parameters.
• Accuracy and Evaluation: The accuracy of calibration depends on the construction tolerances of the calibration pattern and the quality of images used for calibration. Reprojection error is used as a qualitative measure of calibration accuracy.
Challenges and Innovations:
• Image Quality: The quality of calibration images plays a crucial role. Techniques like the structural similarity (SSIM) index and peak signal-to-noise ratio (PSNR) are used to assess image quality.
• Optimization Techniques: Various optimization techniques are employed to improve the accuracy and efficiency of camera calibration, including mathematical optimization and linear programming.

## Applications:

• Stereo Vision: Camera calibration is fundamental for stereo vision systems, where it determines the accuracy of 3D scene reconstructions.
• Robotics and Autonomous Vehicles: Calibration is critical for navigation and object recognition tasks in robotics and autonomous vehicle applications.

## Reference:

• Book chapter titled “Camera Calibration and Video Stabilization Framework for Robot Localization” in the book entitled “Control Engineering in Robotics and Industrial Automation," which will be published (24/07/2021) in Springer.
• Pattern Image Significance for Camera Calibration, IEEE Student Conference on Research and Development (SCOReD 2017) [ http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8305440&isnumber=8305342]
• Auto-Calibration for Multi-Modal Robot Vision based on Image Quality Assessment,

https://pirahansiah.com/site/pages/CC  