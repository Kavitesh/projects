# CUDA Vector Addition

## Overview
This project demonstrates a simple CUDA program that performs vector addition on the GPU. It utilizes parallel computing to add two arrays element-wise.

## Prerequisites
- NVIDIA GPU with CUDA support
- CUDA Toolkit installed
- `nvcc` compiler available in the system path

## How It Works
1. **Memory Allocation**: The program allocates memory on the GPU for three integer arrays.
2. **Data Transfer**: Input vectors are copied from the host (CPU) to the device (GPU).
3. **Kernel Execution**: A CUDA kernel function runs in parallel, where each thread adds a single element of the vectors.
4. **Copy Back Results**: The computed results are copied from GPU memory back to the host.
5. **Output Results**: The final vector sum is printed on the console.

## Code Breakdown
### CUDA Kernel Function
```cpp
__global__ void vectorAdd(int *a, int *b, int *c, int n) {
    int i = threadIdx.x;
    if (i < n) {
        c[i] = a[i] + b[i];
    }
}
```
- This function executes on the GPU, where each thread computes `c[i] = a[i] + b[i]`.
- `threadIdx.x` is the unique thread ID used to determine which element to process.

### Launching the Kernel
```cpp
vectorAdd<<<1, N>>>(d_a, d_b, d_c, N);
```
- `<<<1, N>>>` means launching one block with `N` threads.
- Each thread handles one element of the arrays.

## Compilation and Execution
### Compile the program:
```sh
nvcc vector_addition.cu -o vector_add
```
### Run the program:
```sh
./vector_addition
```
### Expected Output:
```sh
0 + 0 = 0
1 + 2 = 3
2 + 4 = 6
3 + 6 = 9
...
```

## Key Concepts Demonstrated
- CUDA memory management (`cudaMalloc`, `cudaMemcpy`, `cudaFree`)
- Parallel execution using threads
- Launching kernels with thread blocks


