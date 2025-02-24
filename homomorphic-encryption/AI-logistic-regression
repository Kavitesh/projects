import tenseal as ts
import numpy as np

# Generate Homomorphic Encryption context
context = ts.context(
    ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.global_scale = 2**40
context.generate_galois_keys()

# Encryptor & Decryptor
encryptor = context.encryptor()
decryptor = context.decryptor()

# Sample dataset (X: features, y: labels)
X = np.array([[0.1, 0.5], [0.3, 0.7], [0.8, 0.2]])
y = np.array([0, 1, 1])

# Encrypt dataset
enc_X = [ts.ckks_vector(context, row) for row in X]
enc_y = ts.ckks_vector(context, y.tolist())

# Initialize model weights
weights = np.random.rand(X.shape[1])

# Encrypt weights
enc_weights = ts.ckks_vector(context, weights.tolist())

# Gradient Descent (Encrypted)
learning_rate = 0.1
for epoch in range(5):
    enc_gradient = [enc_X[i] * (enc_X[i].dot(enc_weights) - enc_y[i]) for i in range(len(X))]
    enc_gradient_sum = sum(enc_gradient)
    
    # Update weights
    enc_weights -= learning_rate * enc_gradient_sum

# Decrypt trained weights
trained_weights = decryptor.decrypt(enc_weights).tolist()
print("Decrypted Trained Weights:", trained_weights)
