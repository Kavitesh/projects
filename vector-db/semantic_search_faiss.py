import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load a pre-trained sentence embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample dataset: product descriptions (or FAQs, articles, etc.)
documents = [
    "How to reset my password?",
    "Where can I find the latest software updates?",
    "Steps to troubleshoot a slow internet connection.",
    "How do I contact customer support?",
    "Guidelines for securing my online account."
]

# Convert text into embeddings (vectors)
document_vectors = model.encode(documents, convert_to_numpy=True)

# Create a FAISS index for efficient similarity search
d = document_vectors.shape[1]  # Vector dimension
index = faiss.IndexFlatL2(d)
index.add(document_vectors)  # Store embeddings in FAISS

# User's search query
query_text = "I forgot my login password"
query_vector = model.encode([query_text], convert_to_numpy=True)

# Search for top 2 most similar documents
D, I = index.search(query_vector, k=2)

# Print results
print(f"\nQuery: {query_text}")
for i in range(2):
    print(f"Match {i+1}: {documents[I[0][i]]} (Distance: {D[0][i]:.4f})")
