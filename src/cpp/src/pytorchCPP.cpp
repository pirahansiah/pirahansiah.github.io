#include <iostream>
#include <stdlib.h>
//#include <torch/torch.h>
//#include "opencv2/opencv.hpp"

using namespace std;

int main() {
//    torch::Tensor tensor = torch::rand({2, 3});
//    cv::Mat image = cv::imread("image.jpg");
    
    char *heap = (char*)malloc(11);
    heap[11] = 1; // Accessing heap[11] is out-of-bounds
    printf("Hello, World!\n");
    free(heap); // Freeing the allocated memory
    return 0;
}




// #include <iostream>
// #include <torch/torch.h>
// #include "network.h"

// using namespace std;
// using namespace torch;
// int main() {
//     Net network (50,10);
//     cout<<network;
//     // std::cout<<"farshid pirahansiah";
//     // std::cout << "PyTorch version: " << TORCH_VERSION << std::endl;
//     // torch::DeviceType device_type;
//     // if (torch::cuda::is_available()) {    
//     //     device_type = torch::kCUDA;
//     // } else {        
//     //     device_type = torch::kCPU;
//     // }
//     // torch::Tensor x = torch::randn({3, 4}, device_type);
//     // cout<<x;

//     char *heap = malloc(10);
//     heap[10]=1;
//     Tensor x, output;
//     x=torch::randn({2,50});
//     output=network->forward(x);
//     cout<<output<<endl;
//     return 0;
// }