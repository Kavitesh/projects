from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime
import random
import math

def generate_keys(bit_length=1024):
    # Generate two large prime numbers
    p = getPrime(bit_length)
    q = getPrime(bit_length)
    
    # Compute n and phi(n)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose an integer e
    e = 65537  # Commonly used prime number for e
    while math.gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    
    # Compute d
    d = pow(e, -1, phi)
    
    # Public and private keys
    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key

def encrypt(public_key, plaintext):
    e, n = public_key
    # Convert plaintext to integer
    m = bytes_to_long(plaintext.encode())
    # Encrypt
    c = pow(m, e, n)
    return c

def decrypt(private_key, ciphertext):
    d, n = private_key
    # Decrypt
    m = pow(ciphertext, d, n)
    # Convert integer back to plaintext
    plaintext_bytes = long_to_bytes(m)
    plaintext = plaintext_bytes.decode('utf-8', errors='ignore')
    return plaintext
    
# Example usage:
def main():
    public_key, private_key = generate_keys(bit_length=512)
    
    message = "Hello, RSA!"
    print("Original message:", message)
    
    ciphertext = encrypt(public_key, message)
    print("Encrypted message:", ciphertext)
    
    decrypted_message = decrypt(private_key, ciphertext)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()