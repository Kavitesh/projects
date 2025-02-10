import tenseal as ts
import datetime

# Initialize Homomorphic Encryption context
context = ts.context(
    scheme=ts.SCHEME_TYPE.BFV,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.generate_galois_keys()
context.generate_relin_keys()

# Secret key is required for decryption
context.global_scale = 2**40
context.make_context_public()

# Define a GDPR retention period (e.g., 2 years)
RETENTION_YEARS = 2
now = int(datetime.datetime.now().timestamp())  # Current timestamp
retention_cutoff = now - (RETENTION_YEARS * 365 * 24 * 60 * 60)  # Retention threshold

# Encrypt a sample user's data creation timestamp (e.g., from a database)
user_data_creation_timestamp = now - (3 * 365 * 24 * 60 * 60)  # 3 years ago
encrypted_timestamp = ts.bfv_vector(context, [user_data_creation_timestamp])

# Encrypt the retention cutoff
encrypted_retention_cutoff = ts.bfv_vector(context, [retention_cutoff])

# Perform GDPR compliance check on encrypted data (comparison via subtraction)
encrypted_result = encrypted_timestamp - encrypted_retention_cutoff  # If result > 0, it's non-compliant

# Decrypt the result
decrypted_result = encrypted_result.decrypt()  # Only decryption needed for compliance check
is_non_compliant = decrypted_result[0] > 0

# Print result (without exposing actual timestamps)
print(f"Data is GDPR compliant: {not is_non_compliant}")  # False (Non-compliant)

