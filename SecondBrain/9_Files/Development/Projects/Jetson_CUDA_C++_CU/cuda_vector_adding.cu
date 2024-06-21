/*
export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
//nvcc -std=c++11 -o cuda1 cuda_vector_adding.cu $(pkg-config --cflags --libs opencv4)
nvcc -std=c++11 -o cuda1 cuda_vector_adding.cu $(pkg-config --cflags --libs opencv4) -Xcudafe "--diag_suppress=overloaded_virtual"
*/
#include <iostream>
#include <cuda_runtime.h>
#include <opencv2/opencv.hpp>
#include <iostream>
#include <cuda_runtime.h>
#include <opencv2/core/opengl.hpp>
#include <opencv2/highgui.hpp>
//#include <opencv2/cudaimgproc.hpp>

using namespace std;
using namespace cv;
using namespace cv::cuda;

__global__ void matrixMultiply(float *A, float *B, float *C, int N) {
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;
    float sum = 0.0f;

    if (row < N && col < N) {
        for (int i = 0; i < N; i++) {
            sum += A[row * N + i] * B[i * N + col];
        }
        C[row * N + col] = sum;
    }
}
int main() {
    std::cout << cv::getBuildInformation() << std::endl;
    cout << "This program demonstrates using alphaComp" << endl;
    cout << "Press SPACE to change compositing operation" << endl;
    cout << "Press ESC to exit" << endl;

    namedWindow("First Image", WINDOW_NORMAL);
    namedWindow("Second Image", WINDOW_NORMAL);
    namedWindow("Result", WINDOW_OPENGL);

    setGlDevice();

    Mat src1(640, 480, CV_8UC4, Scalar::all(0));
    Mat src2(640, 480, CV_8UC4, Scalar::all(0));

    rectangle(src1, Rect(50, 50, 200, 200), Scalar(0, 0, 255, 128), 30);
    rectangle(src2, Rect(100, 100, 200, 200), Scalar(255, 0, 0, 128), 30);

    GpuMat d_src1(src1);
    GpuMat d_src2(src2);

    GpuMat d_res;

    imshow("First Image", src1);
    imshow("Second Image", src2);
    std::cout << cv::getBuildInformation() << std::endl;
    cv::waitKey(0);
/*
    int alpha_op = ALPHA_OVER;

    const char* op_names[] =
    {
        "ALPHA_OVER", "ALPHA_IN", "ALPHA_OUT", "ALPHA_ATOP", "ALPHA_XOR", "ALPHA_PLUS", "ALPHA_OVER_PREMUL", "ALPHA_IN_PREMUL", "ALPHA_OUT_PREMUL",
        "ALPHA_ATOP_PREMUL", "ALPHA_XOR_PREMUL", "ALPHA_PLUS_PREMUL", "ALPHA_PREMUL"
    };
/*
    for(;;)
    {
        cout << op_names[alpha_op] << endl;

        alphaComp(d_src1, d_src2, d_res, alpha_op);

        imshow("Result", d_res);

        char key = static_cast<char>(waitKey());

        if (key == 27)
            break;

        if (key == 32)
        {
            ++alpha_op;

            if (alpha_op > ALPHA_PREMUL)
                alpha_op = ALPHA_OVER;
        }
    }
*/
    /////
    cv::Mat image = cv::Mat::zeros(256, 256, CV_8UC3);
    image.setTo(cv::Scalar(255, 0, 0));  // Blue color

    // Create a window for display.
    cv::namedWindow("Display window", cv::WINDOW_AUTOSIZE);

    // Show our image inside it.
    cv::imshow("Display window", image);

    // Wait for a keystroke in the window
    cv::waitKey(0);




    std::string videoPath="/home/tiziran/farshid/depthai-python/examples/LLM.mp4";
    

    // Create a VideoCapture object
    cv::VideoCapture cap(videoPath);

    // Check if video opened successfully
    if (!cap.isOpened()) {
        std::cerr << "Error: Could not open video." << std::endl;
        return -1;
    }

    // Get various properties of the video
    double width = cap.get(cv::CAP_PROP_FRAME_WIDTH);
    double height = cap.get(cv::CAP_PROP_FRAME_HEIGHT);
    double fps = cap.get(cv::CAP_PROP_FPS);
    double totalFrames = cap.get(cv::CAP_PROP_FRAME_COUNT);
    int codecCode = static_cast<int>(cap.get(cv::CAP_PROP_FOURCC));
    char codecChars[5] = {0};
    codecChars[0] = codecCode & 0xFF;
    codecChars[1] = (codecCode >> 8) & 0xFF;
    codecChars[2] = (codecCode >> 16) & 0xFF;
    codecChars[3] = (codecCode >> 24) & 0xFF;
    std::string codec(codecChars);

    // Print the details
    std::cout << "Video Width: " << width << std::endl;
    std::cout << "Video Height: " << height << std::endl;
    std::cout << "Frame Rate (FPS): " << fps << std::endl;
    std::cout << "Total Number of Frames: " << totalFrames << std::endl;
    std::cout << "Codec: " << codec << std::endl;

    // Release the video capture object
    cap.release();


    int nDevices;
    cudaGetDeviceCount(&nDevices);
    for (int i = 0; i < nDevices; i++) {
        cudaDeviceProp prop;
        cudaGetDeviceProperties(&prop, i);
        std::cout << "Device Number: " << i << std::endl;
        std::cout << "  Device name: " << prop.name << std::endl;
        std::cout << "  Memory Clock Rate (KHz): " << prop.memoryClockRate << std::endl;
        std::cout << "  Memory Bus Width (bits): " << prop.memoryBusWidth << std::endl;
        std::cout << "  Peak Memory Bandwidth (GB/s): "
                  << 2.0 * prop.memoryClockRate * (prop.memoryBusWidth / 8) / 1.0e6 << std::endl;
    }
    return 0;
}