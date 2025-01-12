
def xor_bytes(b1: bytes, b2: bytes) -> bytes:
    '''Performs a bitwise XOR operation on two byte sequences.'''
    return bytes(a ^ b for a, b in zip(b1, b2))

def xor_bytes_simple(b1: bytes, b2: bytes) -> bytes:
    '''Simpler implementation''' 
    # Create a list of XOR results for each pair of bytes
    xored_list = []
    for a, b in zip(b1, b2):
        xored_list.append(a ^ b)
    
    # Convert the list of XOR results to a bytes object
    xored_bytes = bytes(xored_list)
    
    return xored_bytes

# Example usage:
def main():
    bytes1  = bytes([0b01, 0b10, 0b11])
    bytes2  = b"\x01\x01\x00"
    xored_bytes = xor_bytes(bytes1, bytes2)

    print(f"First byte sequence {bytes1}")
    print(f"Second byte sequence {bytes2}")
    print(f"XORed {xored_bytes}")

if __name__ == "__main__":
    main()