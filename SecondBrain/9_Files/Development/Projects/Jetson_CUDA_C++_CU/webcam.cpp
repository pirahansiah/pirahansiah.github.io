#include <opencv2/opencv.hpp>
#include <iostream>

int main() {
    // Open the default camera
    cv::VideoCapture cap(0);
    if (!cap.isOpened()) {
        std::cerr << "Error opening the video camera" << std::endl;
        return -1;
    }

    // Prepare to pipe to FFmpeg
    FILE* ffmpeg = popen("ffmpeg -f rawvideo -pix_fmt bgr24 -s 640x480 -r 30 -i - "
                         "-f mpegts -codec:v mpeg1video -b:v 800k -r 30 http://localhost:8081", "w");

    if (ffmpeg == NULL) {
        std::cerr << "Failed to run FFmpeg" << std::endl;
        return -1;
    }

    cv::Mat frame;
    while (true) {
        cap >> frame;  // Capture a frame
        if (frame.empty()) break;  // Check for end of video

        // Write frame to FFmpeg
        fwrite(frame.data, 1, frame.total() * frame.elemSize(), ffmpeg);
        fflush(ffmpeg);

        if (cv::waitKey(20) >= 0) break;  // Exit on keypress
    }

    pclose(ffmpeg);
    return 0;
}
