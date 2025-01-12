import os

def str_to_bytes(some_string):
    return some_string.encode('utf-8')

def bytes_to_str(some_bytes):
    return some_bytes.decode('utf-8')

def xor_bytes(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, b2))

# Example usage:
def main():
    # Message to be encrypted
    message = "Hello, World!"
    message_bytes = str_to_bytes(message)
    
    # Generate a random key (same length as the message)
    key = os.urandom(len(message_bytes))
    
    # Encrypt the message
    encrypted_bytes = xor_bytes(message_bytes, key)
    encrypted_message = encrypted_bytes.hex()
    print(f"Encrypted Message (hex): {encrypted_message}")
    
    # Decrypt the message
    decrypted_bytes = xor_bytes(encrypted_bytes, key)
    decrypted_message = bytes_to_str(decrypted_bytes)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()