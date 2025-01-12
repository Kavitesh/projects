# RSA (Rivest-Shamir-Adleman)

RSA is a widely-used public-key cryptosystem for secure data transmission. It works by generating a pair of keys: a public key, which can be shared openly, and a private key, which is kept secret.

## Key Generation

1. **Select two large prime numbers, p and q.**
2. **Compute n=p×q.**  
   \( n \) is used as the modulus for both the public and private keys.
3. **Compute the totient (Euler's totient function), ϕ(n)=(p−1)×(q−1).**
4. **Choose an integer e such that \(1<e<ϕ(n)\) and e is coprime to \(ϕ(n)\).**  
   \( e \) is the public exponent.
5. **Compute d, the modular multiplicative inverse of e modulo \(ϕ(n)\).**  
   \( d \) is the private exponent.

## Encryption

1. Convert the plaintext message to an integer \( m \) such that \( 0 \leq m < n \).
2. Compute the ciphertext \( c \) using the public key \((e, n)\):  
  \( c = m^e \mod n \).

## Decryption

1. Compute the plaintext message \( m \) using the private key \((d, n)\):  
  \( m = c^d \mod n \).

## Python Implementation

You can find a small Python implementation of the RSA algorithm in the [`rsa_using_math.py`](./rsa_using_math.py) file. This script includes functions for key generation, encryption, and decryption.