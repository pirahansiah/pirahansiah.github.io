#include <iostream>
#include <cuda_runtime.h>

int main() {
    int driverVersion = 0, runtimeVersion = 0;
    cudaDriverGetVersion(&driverVersion);
    cudaRuntimeGetVersion(&runtimeVersion);

    std::cout << "CUDA Driver Version: " << driverVersion/1000 << "." << (driverVersion%100)/10 << std::endl;
    std::cout << "CUDA Runtime Version: " << runtimeVersion/1000 << "." << (runtimeVersion%100)/10 << std::endl;

    return 0;
}