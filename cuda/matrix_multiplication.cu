#include <iostream>
#include <cuda_runtime.h>

#define N 3  // Matrix size N x N

// CUDA Kernel for matrix multiplication
__global__ void matrixMul(int *A, int *B, int *C, int n) {
    int row = threadIdx.y;
    int col = threadIdx.x;
    int sum = 0;
    for (int k = 0; k < n; k++) {
        sum += A[row * n + k] * B[k * n + col];
    }
    C[row * n + col] = sum;
}

int main() {
    int h_A[N*N], h_B[N*N], h_C[N*N];  
    int *d_A, *d_B, *d_C;

    // Initialize matrices A and B
    for (int i = 0; i < N * N; i++) {
        h_A[i] = i + 1;
        h_B[i] = (i + 1) * 2;
    }

    // Allocate memory on GPU
    cudaMalloc(&d_A, N * N * sizeof(int));
    cudaMalloc(&d_B, N * N * sizeof(int));
    cudaMalloc(&d_C, N * N * sizeof(int));

    // Copy matrices to device
    cudaMemcpy(d_A, h_A, N * N * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B, N * N * sizeof(int), cudaMemcpyHostToDevice);

    // Launch kernel with a 2D block of threads
    dim3 threadsPerBlock(N, N);
    matrixMul<<<1, threadsPerBlock>>>(d_A, d_B, d_C, N);

    // Copy result back to host
    cudaMemcpy(h_C, d_C, N * N * sizeof(int), cudaMemcpyDeviceToHost);

    // Print result
    std::cout << "Matrix C (Result):\n";
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            std::cout << h_C[i * N + j] << " ";
        }
        std::cout << "\n";
    }

    // Free GPU memory
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);

    return 0;
}
