import random

# Generate dummy data (y = 2x + 3 with some noise)
data = [(x, 2*x + 3 + random.uniform(-1, 1)) for x in range(10)]

# Initialize parameters
m, b = random.random(), random.random()
learning_rate = 0.01
epochs = 1000

# Stochastic Gradient Descent
for epoch in range(epochs):
    x, y_true = random.choice(data)  # Pick one random data point
    y_pred = m * x + b  # Compute prediction
    error = y_pred - y_true  # Compute error
    
    # Compute gradients
    dm = 2 * error * x  
    db = 2 * error  
    
    # Update parameters
    m -= learning_rate * dm
    b -= learning_rate * db

    if epoch % 10 == 0:
        print(f"Epoch {epoch}: m={m:.4f}, b={b:.4f}")

print(f"Final Equation: y = {m:.4f}x + {b:.4f}")
