import pandas as pd
import numpy as np
import tenseal as ts

# Step 1: Load dataset from CSV
df = pd.read_csv("user_ratings.csv")
user_ids = df["UserID"].values
ratings = df.drop(columns=["UserID"]).values  # Remove UserID column

# Step 2: Initialize user and item embeddings
users, items = ratings.shape
np.random.seed(42)
user_embeddings = np.random.rand(users, 2)  # 2 latent factors per user
item_embeddings = np.random.rand(items, 2)  # 2 latent factors per item

# Step 3: Create Homomorphic Encryption context
context = ts.context(
    ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.global_scale = 2**40
context.generate_galois_keys()

# Step 4: Encrypt user embeddings
encrypted_users = [ts.ckks_vector(context, user.tolist()) for user in user_embeddings]

# Step 5: Compute encrypted predictions
# Proper dot product of each encrypted user vector with each item embedding
encrypted_predictions = [
    [enc_user.dot(item.tolist()) for item in item_embeddings] for enc_user in encrypted_users
]

# Step 6: Decrypt and display predictions
decrypted_predictions = [[pred.decrypt() for pred in user_preds] for user_preds in encrypted_predictions]

print("Predicted Ratings (With Homomorphic Encryption):")
for i, preds in enumerate(decrypted_predictions):
    print(f"User {user_ids[i]}: {preds}")
