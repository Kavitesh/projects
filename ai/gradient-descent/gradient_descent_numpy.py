import numpy as np

# Sample training data (y = 2x + 3)
x_train = np.array([1.0, 2.0, 3.0, 4.0]).reshape(-1, 1)  # Shape: (4,1)
y_train = np.array([5.0, 7.0, 9.0, 11.0]).reshape(-1, 1)  # Expected output

# Initialize weight and bias randomly
w = np.random.randn(1)  # Weight
b = np.random.randn(1)  # Bias

# Define the learning rate and number of epochs
learning_rate = 0.01
epochs = 100

# Training loop
for epoch in range(epochs):
    y_pred = w * x_train + b  # Forward pass (prediction)

    # Compute Mean Squared Error (MSE) loss
    loss = np.mean((y_pred - y_train) ** 2)

    # Compute gradients manually (derivatives)
    dw = np.mean(2 * (y_pred - y_train) * x_train)  # dL/dw
    db = np.mean(2 * (y_pred - y_train))  # dL/db

    # Update parameters using Gradient Descent
    w -= learning_rate * dw
    b -= learning_rate * db

    if epoch % 10 == 0:  # Print every 10 epochs
        print(f"Epoch {epoch}: Loss = {loss:.4f}, w = {w[0]:.4f}, b = {b[0]:.4f}")

# Test the trained model
x_test = np.array([5.0])  # New input
y_test_pred = w * x_test + b  # Make prediction
print(f"Prediction for x=5: {y_test_pred[0]:.4f}")  # Expected: 13.0
