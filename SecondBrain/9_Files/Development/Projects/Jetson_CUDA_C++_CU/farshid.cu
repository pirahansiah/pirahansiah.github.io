// #include <iostream>
// #include <cuda_runtime.h>
// #include <opencv2/opencv.hpp>
// #include <opencv2/highgui.hpp>
// #include <opencv2/dnn.hpp>

// using namespace std;
// using namespace cv;
// using namespace cv::cuda;

// int main() {
//     Mat src1(640, 480, CV_8UC4, Scalar::all(0));
//     rectangle(src1, Rect(50, 50, 300, 200), Scalar(0, 0, 255, 128), 30);    
//     GpuMat d_src1;
//     d_src1.upload(src1);    
//     Mat result;
//     d_src1.download(result);    
//     imshow("Result Image", result);
//     waitKey(0);
//     return 0;
// }


// #include <iostream>
// #include <cuda_runtime.h>
// #include <opencv2/opencv.hpp>
// #include <opencv2/highgui.hpp>
// #include <opencv2/dnn.hpp>

// using namespace std;
// using namespace cv;
// using namespace cv::cuda;

// int main() {
//     Mat src1(640, 480, CV_8UC4, Scalar::all(0));
//     rectangle(src1, Rect(50, 50, 300, 200), Scalar(0, 0, 255, 128), 30);
//     GpuMat d_src1;
//     d_src1.upload(src1);
//     vector<Rect> bboxes;
//     vector<float> scores;
//     vector<int> result;
//     // TODO: populate bboxes and scores with bounding box data
//     dnn::NMSBoxes(bboxes, scores, 0.4, 0.6, result);
//     GpuMat d_result;
//     d_result.upload(result);
//     Mat result_cpu;
//     d_result.download(result_cpu);
//     imshow("Result Image", src1);
//     waitKey(0);
//     return 0;
// }


#include <iostream>
#include <cuda_runtime.h>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/dnn.hpp>
#include <opencv2/cudaobjdetect.hpp>

using namespace std;
using namespace cv;
using namespace cv::cuda;

int main() {
    // Load the face and eye cascade classifiers
    cv::CascadeClassifier face_cascade;
    cv::CascadeClassifier eyes_cascade;

    if (!face_cascade.load("/home/tiziran/code/image_web/tiziran/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml")) {
        cout << "Error loading face cascade\n";
        return -1;
    }
    if (!eyes_cascade.load("/home/tiziran/code/image_web/tiziran/lib/python3.8/site-packages/cv2/data/haarcascade_eye.xml")) {
        cout << "Error loading eyes cascade\n";
        return -1;
    }

    // Open the default camera
    VideoCapture cap(0);
    if (!cap.isOpened()) {
        cout << "Error opening video capture\n";
        return -1;
    }

    Mat frame, gray_frame;
    GpuMat d_frame, d_gray_frame;
     while (cap.read(frame)) {
        // Convert frame to grayscale
        cvtColor(frame, gray_frame, COLOR_BGR2GRAY);
        d_frame.upload(frame);
        d_gray_frame.upload(gray_frame);

        // Detect faces
        std::vector<Rect> faces;
        face_cascade.detectMultiScale(gray_frame, faces);

        for (size_t i = 0; i < faces.size(); i++) {
            Point center(faces[i].x + faces[i].width / 2, faces[i].y + faces[i].height / 2);
            ellipse(frame, center, Size(faces[i].width / 2, faces[i].height / 2), 0, 0, 360, Scalar(255, 0, 255), 4);

            Mat faceROI = gray_frame(faces[i]);
            std::vector<Rect> eyes;
            eyes_cascade.detectMultiScale(faceROI, eyes);

            for (size_t j = 0; j < eyes.size(); j++) {
                Point eye_center(faces[i].x + eyes[j].x + eyes[j].width / 2, faces[i].y + eyes[j].y + eyes[j].height / 2);
                int radius = cvRound((eyes[j].width + eyes[j].height) * 0.25);
                circle(frame, eye_center, radius, Scalar(255, 0, 0), 4);
            }
        }

        // Save the frame with detections
        imwrite("output.jpg", frame);

        // Break the loop after saving one frame (for testing purposes)
        break;
    }

    return 0;
}
