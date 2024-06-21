#include <iostream>
#include <cuda_runtime.h>

__global__ void vectorAdd(const float *A, const float *B, float *C, int numElements){
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    if(i<numElements){
        C[i]=A[i]+B[i];
    }
}
int main(void)
{
    std::cout<<"Farshid PirahanSiah Cuda for LLM + Vision for jetson nano";
    return 0;
}
#include <iostream>
#include <cuda_runtime.h>
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