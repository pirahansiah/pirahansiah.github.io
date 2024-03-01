/*
brew install jpeg libpng libtiff openexr
brew install opencv 
//g++ -o fp1 fp1.cpp `pkg-config --cflags --libs opencv4`
export PKG_CONFIG_PATH="/usr/local/Cellar/opencv/4.9.0_3/lib/pkgconfig:$PKG_CONFIG_PATH"
pkg-config --cflags opencv4

*/

#include <opencv2/opencv.hpp>
#include <iostream>

int main(void)
{
    std::cout << "Hello, World! ffffff" << std::endl;
}

