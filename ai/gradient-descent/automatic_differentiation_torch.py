import torch

# Define variables
w = torch.tensor(2.0, requires_grad=True)
b = torch.tensor(3.0, requires_grad=True)

# Compute function
y = w**2 + b  # Function to differentiate
y.backward()  # Compute gradients

print(f"dw: {w.grad.item()}, db: {b.grad.item()}")  # dw = 4, db = 1
