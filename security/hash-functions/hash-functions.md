# Hash Functions

## Introduction
A **hash function** is a mathematical function that converts an input (or 'message') into a fixed-length string of bytes. The output is typically a "digest" that uniquely represents the input data.

### Characteristics of a Good Hash Function
- **Deterministic**: The same input always produces the same output.
- **Fast Computation**: The function should return the hash in a reasonable time.
- **Preimage Resistance**: Given a hash value, it should be computationally infeasible to retrieve the original input.
- **Small Changes Result in Large Differences**: A tiny change in input should drastically change the output (**avalanche effect**).
- **Collision Resistance**: It should be hard to find two different inputs that produce the same hash.
- **Irreversibility**: It should not be possible to derive the original input from the hash.

## Common Hash Functions
1. **MD5 (Message Digest Algorithm 5)** - 128-bit output, not secure for cryptographic use.
2. **SHA-1 (Secure Hash Algorithm 1)** - 160-bit output, deprecated due to vulnerabilities.
3. **SHA-256 (Secure Hash Algorithm 256-bit)** - Commonly used in blockchain and security applications.
4. **SHA-3** - A newer standard offering stronger security properties.
5. **bcrypt, Argon2** - Used in password hashing with additional security features.

## Implementations

### Python Implementation
```python
import hashlib

def hash_sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

input_data = "hello world"
hash_value = hash_sha256(input_data)
print(f"SHA-256: {hash_value}")
```

### JavaScript Implementation
```javascript
const crypto = require('crypto');

function hashSHA256(data) {
    return crypto.createHash('sha256').update(data).digest('hex');
}

console.log("SHA-256:", hashSHA256("hello world"));
```

### Solidity Implementation
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HashExample {
    function hashSHA256(string memory data) public pure returns (bytes32) {
        return sha256(abi.encodePacked(data));
    }
}
```

## Applications of Hash Functions
- **Data Integrity**: Used in checksums to verify file integrity.
- **Cryptographic Security**: Used in digital signatures and authentication.
- **Blockchain & Cryptocurrencies**: Hash functions secure transactions.
- **Password Storage**: Hashing ensures passwords are not stored in plaintext.

## Conclusion
Hash functions play a crucial role in security, cryptography, and data integrity. While some older hash functions are now considered insecure, modern algorithms like SHA-256 and Argon2 provide robust security measures for various applications.

