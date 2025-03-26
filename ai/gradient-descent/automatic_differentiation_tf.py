import tensorflow as tf

# Define variables
w = tf.Variable(2.0)
b = tf.Variable(3.0)

# Compute gradients using GradientTape
with tf.GradientTape() as tape:
    y = w**2 + b  # Function to differentiate

gradients = tape.gradient(y, [w, b])  # Compute gradients
print(f"dw: {gradients[0].numpy()}, db: {gradients[1].numpy()}")  # dw = 4, db = 1
