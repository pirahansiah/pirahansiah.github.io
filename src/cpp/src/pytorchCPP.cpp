#include <torch/torch.h>
#include <iostream>
#include "network.h"

using namespace std;
using namespace torch;
int main() {
    Net network (50,10);
    cout<<network;
    // std::cout<<"farshid pirahansiah";
    // std::cout << "PyTorch version: " << TORCH_VERSION << std::endl;
    // torch::DeviceType device_type;
    // if (torch::cuda::is_available()) {    
    //     device_type = torch::kCUDA;
    // } else {        
    //     device_type = torch::kCPU;
    // }
    // torch::Tensor x = torch::randn({3, 4}, device_type);
    // cout<<x;
    Tensor x, output;
    x=torch::randn({2,50});
    output=network->forward(x);
    cout<<output<<endl;
    return 0;
}