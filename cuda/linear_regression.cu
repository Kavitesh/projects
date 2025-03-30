#include <iostream>
#include <cuda_runtime.h>

#define N 4      // Number of data points
#define LR 0.01  // Learning rate
#define EPOCHS 100

// CUDA kernel for forward pass: Compute y_pred = w*x + b
__global__ void forwardPass(float *x, float *w, float *b, float *y_pred, int n) {
    int i = threadIdx.x;
    if (i < n) {
        y_pred[i] = (*w) * x[i] + (*b);
    }
}

// CUDA kernel for calculating gradients
__global__ void computeGradients(float *x, float *y, float *y_pred, float *w_grad, float *b_grad, int n) {
    int i = threadIdx.x;
    if (i < n) {
        atomicAdd(w_grad, 2 * x[i] * (y_pred[i] - y[i]) / n);
        atomicAdd(b_grad, 2 * (y_pred[i] - y[i]) / n);
    }
}

// CUDA kernel for updating weights using gradient descent
__global__ void updateWeights(float *w, float *b, float *w_grad, float *b_grad, float lr) {
    *w -= lr * (*w_grad);
    *b -= lr * (*b_grad);
}

int main() {
    float h_x[N] = {1, 2, 3, 4};   // Inputs
    float h_y[N] = {2, 4, 6, 8};   // Targets
    float h_w = 0.0, h_b = 0.0;    // Model parameters (w, b)
    
    float *d_x, *d_y, *d_w, *d_b, *d_y_pred, *d_w_grad, *d_b_grad;

    // Allocate memory on GPU
    cudaMalloc(&d_x, N * sizeof(float));
    cudaMalloc(&d_y, N * sizeof(float));
    cudaMalloc(&d_w, sizeof(float));
    cudaMalloc(&d_b, sizeof(float));
    cudaMalloc(&d_y_pred, N * sizeof(float));
    cudaMalloc(&d_w_grad, sizeof(float));
    cudaMalloc(&d_b_grad, sizeof(float));

    // Copy data to GPU
    cudaMemcpy(d_x, h_x, N * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_y, h_y, N * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_w, &h_w, sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, &h_b, sizeof(float), cudaMemcpyHostToDevice);

    // Training loop
    for (int epoch = 0; epoch < EPOCHS; epoch++) {
        float h_w_grad = 0, h_b_grad = 0;
        cudaMemcpy(d_w_grad, &h_w_grad, sizeof(float), cudaMemcpyHostToDevice);
        cudaMemcpy(d_b_grad, &h_b_grad, sizeof(float), cudaMemcpyHostToDevice);

        forwardPass<<<1, N>>>(d_x, d_w, d_b, d_y_pred, N);
        computeGradients<<<1, N>>>(d_x, d_y, d_y_pred, d_w_grad, d_b_grad, N);
        updateWeights<<<1, 1>>>(d_w, d_b, d_w_grad, d_b_grad, LR);

        cudaMemcpy(&h_w, d_w, sizeof(float), cudaMemcpyDeviceToHost);
        cudaMemcpy(&h_b, d_b, sizeof(float), cudaMemcpyDeviceToHost);

        if (epoch % 20 == 0) {
            std::cout << "Epoch " << epoch << " - w: " << h_w << ", b: " << h_b << std::endl;
        }
    }

    // Cleanup
    cudaFree(d_x);
    cudaFree(d_y);
    cudaFree(d_w);
    cudaFree(d_b);
    cudaFree(d_y_pred);
    cudaFree(d_w_grad);
    cudaFree(d_b_grad);

    std::cout << "Final Model: y = " << h_w << "x + " << h_b << std::endl;
    return 0;
}
