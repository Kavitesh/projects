import tenseal as ts

poly_mod_degree = 4096
coeff_mod_bit_sizes = [40, 20, 40]
# create TenSEALContext
context = ts.context(ts.SCHEME_TYPE.CKKS, poly_mod_degree, -1, coeff_mod_bit_sizes)
# scale of ciphertext to use
context.global_scale = 2 ** 20
context.generate_galois_keys()
context.generate_relin_keys()

# Save keys to files
with open("private_key.tenseal", "wb") as f:
    f.write(context.serialize(save_secret_key=True))
with open("public_key.tenseal", "wb") as f:
    f.write(context.serialize(save_secret_key=False))
