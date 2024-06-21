---
tags: i/convert, i/python, i/c , i/matlab
---


Python:
```py
x = 8
se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*x-1, 2*x-1))
```

C++:
```cpp
#incluse  <opencv.hpp>
int x=8;
cv::Mat se = cv::getStructuringElement(cv::MorphShapes::MORPH_ELLIPSE, cv::Size(2*x-1, 2*x-1));
```

Matlab:
```matlab
dst = imerode(src,se);
```

