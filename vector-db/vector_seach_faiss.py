import faiss
import numpy as np

# Define vector dimension
d = 3  
index = faiss.IndexFlatL2(d)  # L2 (Euclidean) distance index

# Insert multiple vectors
vectors = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0],
    [2.5, 3.5, 4.5],
    [6.0, 7.0, 8.0]
], dtype='float32')

index.add(vectors)  # Add vectors to FAISS index

# Define a query vector
query = np.array([[3.0, 4.0, 5.0]], dtype='float32')

# Search for the nearest 2 neighbors
D, I = index.search(query, k=2)

# Print results
print("Query Vector:", query[0])
print("Nearest Neighbor Indices:", I[0])
print("Distances:", D[0])

# Retrieve the actual nearest vectors
nearest_vectors = vectors[I[0]]
print("Nearest Neighbor Vectors:\n", nearest_vectors)
