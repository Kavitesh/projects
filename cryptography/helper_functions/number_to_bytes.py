'''
Why Convert Numbers to Bytes and Back?
Data Storage: Binary formats are often used for efficient storage and transmission of data.

Interoperability: Converting to and from bytes ensures compatibility with systems that use binary data formats (e.g., databases, network protocols).

Serialization: Bytes are used for serializing data to save state or send over a network.

Encryption: Many encryption algorithms work with byte data, so converting integers to bytes is necessary for cryptographic operations.

Byte Order
Big-Endian: Most significant byte is at the beginning.
Little-Endian: Least significant byte is at the beginning.
'''
def number_to_bytes(number: int, byteorder: str = 'big') -> bytes:
    """Converts a large integer to bytes."""
    # Calculate the byte length needed to represent the number
    byte_length = (number.bit_length() + 7) // 8
    return number.to_bytes(byte_length, byteorder)

def bytes_to_number(byte_data: bytes, byteorder: str = 'big') -> int:
    """Converts bytes back to a large integer."""
    return int.from_bytes(byte_data, byteorder)

def small_numbers_to_bytes(numbers: list[int]) -> bytes:
    """Converts an array of integers(0 to 255) to bytes."""
    return bytes(numbers)

def bytes_to_small_numbers(byte_data: bytes) -> list[int]:
    """Converts bytes back to an array of integers(0 to 255)."""
    return list(byte_data)

def number_to_bits(some_number: int) -> str:
    """Converts a number to its binary representation in bits."""
    return bin(some_number)[2:]

# Example usage:
def main():
    # Example large number
    large_number = 123456789012345678901234567890

    # Convert to bytes and back
    byte_data = number_to_bytes(large_number)
    reconstructed_number = bytes_to_number(byte_data)    
    binary_view_of_bytes = ''.join(f'{byte:08b}' for byte in byte_data)
    binary_view_of_number = number_to_bits(large_number)

    # Output results
    print(f"Original Number: {large_number}")
    print(f"Byte Representation: {byte_data.hex()}")
    print(f"Reconstructed Number: {reconstructed_number}")
    print(f"Binary view of number: 0000000{binary_view_of_number}")
    print(f"Binary view of bytes:  {binary_view_of_bytes} \n")


    # Example array of integers
    number_array = [10, 20, 30, 255]

    # Convert the array of integers to bytes
    byte_data = small_numbers_to_bytes(number_array)
    print(f"Original Array: {number_array}")
    print(f"Byte Representation: {byte_data}")

    # Convert bytes back to the array of integers
    reconstructed_numbers = bytes_to_small_numbers(byte_data)
    print(f"Reconstructed Array: {reconstructed_numbers}")

if __name__ == "__main__":
    main()
