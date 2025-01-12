import random
import uuid

def generate_uuid_v4():
    # Generate 16 random bytes
    random_bytes = [random.randint(0, 255) for _ in range(16)]

    # Set the version (4 bits) to 0100 (UUIDv4)
    random_bytes[6] = (random_bytes[6] & 0x0F) | 0x40

    # Set the variant (2-3 bits) to 10xx (RFC 4122)
    random_bytes[8] = (random_bytes[8] & 0x3F) | 0x80

    # Convert the byte array to a string format UUID
    uuid_str = '{:02x}{:02x}{:02x}{:02x}-{:02x}{:02x}-{:02x}{:02x}-{:02x}{:02x}-{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}'.format(
        *random_bytes
    )
    return uuid_str

def decode_uuid_v4(uuid_str):
    parts = uuid_str.split('-')
    uuid_bytes = [
        int(parts[0][0:2], 16), int(parts[0][2:4], 16), int(parts[0][4:6], 16), int(parts[0][6:8], 16),
        int(parts[1][0:2], 16), int(parts[1][2:4], 16),
        int(parts[2][0:2], 16), int(parts[2][2:4], 16),
        int(parts[3][0:2], 16), int(parts[3][2:4], 16),
        int(parts[4][0:2], 16), int(parts[4][2:4], 16), int(parts[4][4:6], 16), int(parts[4][6:8], 16), int(parts[4][8:10], 16), int(parts[4][10:12], 16)
    ]

    version = (uuid_bytes[6] & 0xF0) >> 4
    variant = (uuid_bytes[8] & 0xC0) >> 6

    return {
        'uuid': uuid_str,
        'version': version,
        'variant': variant,
        'random_bytes': uuid_bytes
    }
    
def main():
    # Generate a UUID v4
    generated_uuid_v4 = generate_uuid_v4()
    print(f"Generated UUID v4: {generated_uuid_v4}")

    # Decode the generated UUID v4
    decoded_uuid_v4 = decode_uuid_v4(generated_uuid_v4)
    print("\nDecoded UUID v4:")
    print(f"Version: {decoded_uuid_v4['version']}")
    print(f"Variant: {decoded_uuid_v4['variant']}")
    print(f"Random Bytes: {decoded_uuid_v4['random_bytes']}")

if __name__ == "__main__":
    main()

