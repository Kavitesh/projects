'''
Converting private keys from bytes to hexadecimal (hex) format before writing them to files is a common practice in cryptography and data storage. This process has several benefits:

1. Human Readability
Hexadecimal Representation: Hexadecimal encoding converts binary data into a more readable format. Each byte of data is represented as a two-character hex string. This makes it easier for humans to inspect, debug, and manually handle cryptographic keys or other binary data.
2. File Storage and Text Handling
Text Files: Many systems and applications are better suited to handling text files rather than binary files. Hexadecimal encoding allows binary data to be stored in text-based formats (e.g., .txt, .pem, .key files) that are more universally compatible with text editors and systems that handle text-based data.
3. Data Integrity
Avoiding Binary Issues: Binary data may contain byte values that are not easily represented or could be misinterpreted by some systems or text processing tools. Hexadecimal representation ensures that all data is converted into a standard, printable format that avoids issues related to non-printable or special characters.
4. Compatibility
Standard Formats: Many cryptographic standards and tools expect keys and other binary data to be in hexadecimal format. For example, PEM (Privacy-Enhanced Mail) and DER (Distinguished Encoding Rules) formats for keys and certificates often use hexadecimal encoding.
5. Ease of Transfer
Data Transfer: Hexadecimal strings are easier to include in URLs, configuration files, and other environments where binary data might cause problems or be modified.
'''
def hex_to_bytes(hex_string: str) -> bytes:
    return bytes.fromhex(hex_string)

def bytes_to_hex(some_bytes: bytes) -> str:
    return some_bytes.hex()

def write_key_to_file(private_key_bytes: bytes, filename: str):
    """Writes the private key in hexadecimal format to a file."""
    with open(filename, 'w') as file:
        hex_representation = bytes_to_hex(private_key_bytes)
        file.write(hex_representation)

def read_key_from_file(filename: str) -> bytes:
    """Reads the private key from a file and converts it from hexadecimal format back to bytes."""
    with open(filename, 'r') as file:
        hex_representation = file.read().strip()
        return hex_to_bytes(hex_representation)
    
# Example usage:
def main():
    private_key_bytes = b'\x01\x02\x03\x04\x05\x06\x07\x08af'
    write_key_to_file(private_key_bytes, 'private_key.txt')

    private_key_bytes = read_key_from_file('private_key.txt')
    print(private_key_bytes)  # Output: b'\x01\x02\x03\x04\x05\x06\x07\x08af'

if __name__ == "__main__":
    main()