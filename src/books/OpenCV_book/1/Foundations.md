# Basic

* OpenCV *imread* Function:
	* Channels are stored in BGR order by default.
	* Consider using the IMREAD_UNCHANGED flag to preserve the original image.
	* It is recommended to use a specific type, such as float32, to avoid potential issues.
	* Example usage: code 001,002,003,004, 005
	
* OpenCV *imshow* Function:
	- If the image type is not an integer, it may needs to be converted to an integer type or normalized before displaying.
	- To view the result, you must use the waitKey(x) function, where 'x' represents the delay time in milliseconds. Using waitKey(0) will cause the window to wait until any key is pressed.
	- In larger projects, it is advisable to define a boolean variable to control the display of images throughout the program. This approach is useful for debugging purposes.
	- Example usage: code 001,002,003,004, 005
	
* OpenCV *imwrite* Function:
	 - Example usage: code 006
	 - Saving Images in Uncompressed Format: When working with images, it is recommended to save them in an uncompressed format whenever possible. This helps preserve the original quality and ensures that no additional compression artifacts are introduced. To save images in an uncompressed format using OpenCV, you can follow these tips:
		 1. Choose an appropriate file format: Select a file format that supports uncompressed storage, such as TIFF (Tagged Image File Format) or BMP (Bitmap Image File). These formats store image data without any lossy compression.
		 2. Use the appropriate parameters: When saving the image, make sure to specify the appropriate parameters to ensure uncompressed storage. For example, in OpenCV, when using the imwrite() function, you can pass the appropriate parameters such as `cv2.IMWRITE_TIFF_COMPRESSION` or `cv2.IMWRITE_PNG_COMPRESSION` to specify the compression level. Set these parameters to their lowest values (e.g., 0 or None) to ensure uncompressed storage.
		 3. Preserve the original data: Before saving the image, ensure that the image data is in the desired format and has not undergone any compression or modification. If necessary, convert the image to the desired format or adjust its data type to ensure uncompressed storage.
		 By following these guidelines, you can save images in an uncompressed format and maintain the original quality of the image data. This is especially important when working with critical applications that require high-fidelity images or when processing images for further analysis or research purposes.
		 
* OpenCV *resize* Function:
	*  Example usage: code 007
	* The OpenCV `resize` function allows you to resize an image using different methods. You have the option to specify the desired size using `cv2.resize` or adjust the scaling factors `fx` and `fy`. There are three interpolation methods available: `INTER_CUBIC`, `INTER_LINEAR`, and `INTER_AREA`. It's worth noting that while `CUBIC` provides the best quality in most cases, it is slower compared to the other methods.

## Color space

Example usage: code 009
Different color spaces have specific advantages and use cases. OpenCV's `cv2.cvtColor()` function allows conversion between color spaces. Understanding color space characteristics enhances image processing and computer vision. Examples include:

- Grayscale: Simplify processing, reduce complexity.
- BGR: Apply filters, e.g., Gaussian blur for noise reduction.
- RGB: Adjust color balance, correct cast, manipulate channels.
- HSV: Track objects by color, isolate hues in video frames.
- YUV: Separate luma and chroma, used in compression.
- LAB: Split lightness from color, aids in analysis and detection.
- CMYK: Printing, subtractive colors from white background.
- HSL: Segmentation, enhancement, saturation control.
- XYZ: Device-independent color space, color science, matching.
- L_a_b*: Uniform color space, correction, segmentation, retrieval.
- YCrCb: Luma and chroma difference, video compression, processing.
- HSV + Alpha: Transparency addition, alpha channel for blending.

These examples showcase the versatility and applicability of various color spaces in different image processing and computer vision scenarios.

## balance white
Example usage: code 010
We use balance white with OpenCV to perform automatic color correction on images. The goal of color correction is to make the colors of objects in an image appear consistent regardless of the lighting conditions or the camera settings. One way to achieve color correction is to use a color matching card, which is a reference card that contains gradated colors of varying hues, shades, blacks, whites, and grays. By matching the histogram of the card to another image, we can adjust the colors of the image to match the reference card.

The balance white function that you wrote is based on the grayworld assumption, which is a simple method of color correction that assumes that the average color of an image is gray. By shifting the average values of each color channel to match a gray value, we can remove any color cast from the image and make it look more natural. However, this method may not work well for images that have a dominant color or are not well exposed.

There are other methods of color correction that use more sophisticated algorithms and machine learning models to achieve better results. [For example, you can check out this tutorial on how to perform automatic color correction with OpenCV using a color matching card](https://pyimagesearch.com/2021/02/15/automatic-color-correction-with-opencv-and-python/)[1](https://pyimagesearch.com/2021/02/15/automatic-color-correction-with-opencv-and-python/). [You can also learn how to train a learning-based white balance algorithm using OpenCV and a dataset of images with ground-truth illuminants](https://docs.opencv.org/4.x/dc/dcb/tutorial_xphoto_training_white_balance.html)[2](https://docs.opencv.org/4.x/dc/dcb/tutorial_xphoto_training_white_balance.html)

## histogram
```python
    N, bin = np.histogram(im[filter].flatten(), np.arange(256))
    f = np.ones((9))
    f /= len(f)
    Nf = np.convolve(N, f, mode='same')

```

## image filter
```python
    filter = np.logical_and(R < im.shape[0] / 4, im < 150)

```

## morphology
```python
x = 8
se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*x-1, 2*x-1))
dst = cv2.morphologyEx(src, cv2.MORPH_CLOSE, se)
```

```python
x = 8
se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*x-1, 2*x-1))
dst = cv2.morphologyEx(src, cv2.MORPH_CLOSE, se)

opening = cv2.morphologyEx(im, cv2.MORPH_OPEN, se)

```

## np.convolve

```python
    N, bin = np.histogram(im[filter].flatten(), np.arange(256))
    f = np.ones((9))
    f /= len(f)
    Nf = np.convolve(N, f, mode='same')

```

## mesh grid cart2pol
 *1 
 ```python
import numpy as np
def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)  

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)


Y, X = np.mgrid[0:im.shape[0], 0 : im.shape[1]]
X -= int(im.shape[1] / 2)
Y -= int(im.shape[0] / 2)
R, Th = cart2pol(X, Y)

```
* 2
```python
    Y, X = np.mgrid[0:im.shape[0], 0:im.shape[1]]
    X -= int(im.shape[1]/2)
    Y -= int(im.shape[0]/2)
    R, Th = cart2pol(X, Y)
```



## sub-pixel, floating points, more precise, real-valued coordinates, Changing the contrast and brightness of an image in CV_32FC3 with OpenCV
Example usage: code 011,012

## sub-pixel, floating points, mesh grid, remap, more precise, real-valued coordinates, moving image pixel, Shift image content with OpenCV
Example usage: code 013
A mesh is a data structure that represents a surface by dividing it into a collection of smaller, connected elements. Meshes are used in a variety of applications, including computer graphics, 3D printing, and finite element analysis.

There are several reasons why meshes are used. First, they are a more efficient way to represent a surface than a single, large array. This is because meshes can be stored and manipulated more easily, and they require less memory. Second, meshes can be used to represent a wider variety of surfaces than a single, large array. This is because meshes can be subdivided to represent curved surfaces, while a single, large array can only represent flat surfaces.

Here are some of the ways that meshes are used:

- **Computer graphics:** Meshes are used to represent 3D objects in computer graphics. They are used to create models of people, animals, objects, and environments.
- **3D printing:** Meshes are used to create 3D printed objects. The mesh is sliced into thin layers, and each layer is printed on top of the previous layer.
- **Finite element analysis:** Meshes are used in finite element analysis to model the behavior of structures under load. The mesh is used to divide the structure into smaller elements, and each element is analyzed to determine its stress and strain.



## gain
Example usage: code 014

multiplying an image by a gain factor

## copy small to big
Example usage: code 015

```pythonthon 
roi[:, :] = smallImage
```




## tips 


1 sub-pixel, floating points, more precise, real-valued coordinates, Changing the contrast and brightness of an image in CV_32FC3 with OpenCV


2 Cross correlation (CC): TM_CCORR

Mean shifted cross correlation (Pearson correlation coefficient): TM_CCOEFF

Normalization: TM_SQDIFF_NORMED, TM_CCORR_NORMED, TM_CCOEFF_NORMED

maximum absolute difference metric (MaxAD), which is also known as the uniform distance metric computeECC() and findTransformECC().

Sum of absolute differences (SAD)

Cross correlation (CC)

  

find identical regions of an image that match a template, select by giving a threshold 

 2D convolution

It simply slides the template image over the input image (as in 2D convolution) and compares the template and patch of input image under the template image. 

Template matching 

> cv2.TM_CCOEFF

> cv2.TM_CCOEFF_NORMED

> cv2.TM_CCORR

> cv2.TM_CCORR_NORMED

< cv2.TM_SQDIFF

< cv2.TM_SQDIFF_NORMED

cv2.minMaxLoc()


3


## read matlab mat file to python
```python
from scipy import io
res = io.loadmat(r'MatlabResults\results2.mat', struct_as_record=False, squeeze_me=True)
data = io.loadmat(r'MatlabResults\4.mat')
for k in res.keys():
    print(k, res[k])
```
## add path
```python
import sys
sys.path.append(r'C:   )
```



## create mat
```python
bin_im = bin_im.astype(np.uint8)*255
```


## findcontours
```python
contours, hierarchy = cv2.findContours(opening, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
```



## save text
```python
np.savetxt("01-src.txt", im, fmt='%d', delimiter=', ', newline='\n', header='', footer='', comments='# ')
```



## DLL
```python
import ctypes
my_dll = r"C:\fffffff.dll"
lib = ctypes.windll.LoadLibrary(my_dll)
```



## remove background 
```python
im = im - im.min()
```

## time
```python
e1 = cv2.getTickCount()
######    
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
```



## 
```python

```


## 
```python

```



## 
```python

```



## 
```python

```



## 
```python

```
