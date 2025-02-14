import tenseal as ts

# 1️ Create encryption context
context = ts.context(
    scheme=ts.SCHEME_TYPE.CKKS, 
    poly_modulus_degree=8192, 
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.global_scale = 2**40
context.generate_galois_keys()

# 2 Encrypt a number
enc_value = ts.ckks_vector(context, [42])

# 3️ Perform encrypted computation (e.g., add 8)
enc_result = enc_value + 8

# 4️ Decrypt result
decrypted_result = enc_result.decrypt()
print("Decrypted Result:", decrypted_result[0])
