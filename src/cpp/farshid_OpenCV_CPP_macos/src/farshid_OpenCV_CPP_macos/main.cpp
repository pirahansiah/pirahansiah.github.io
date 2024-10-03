#include <iostream>
#include <stdlib.h>
#include <opencv2/opencv.hpp>

using namespace std;
int main() {
    std::cerr<<"Dr. Farshid Pirahansiah 2024 September   \n \n \n";
    int width = 640;
    int height = 480;

    // Create an empty Mat (image) of size height x width with 3 color channels (RGB)
    cv::Mat randomImage(height, width, CV_8UC3);

    // Fill the image with random values
    cv::randu(randomImage, cv::Scalar::all(0), cv::Scalar::all(255));

    // Display the random image
    cv::imshow("Random Image", randomImage);

    // Wait for a key press indefinitely
    cv::waitKey(0);

    printf("farshid\n");    
    return 0;
}