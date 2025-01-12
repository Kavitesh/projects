import time
import random

def int_to_hex(value, length):
    return f'{value:0{length}x}'

def generate_uuid_v1(timestamp=None, clock_seq=None, node=None):
    # If no timestamp is provided, use the current time
    if timestamp is None:
        uuid_epoch_start = 122192928000000000
        timestamp = int(time.time() * 1e7) + uuid_epoch_start

    # If no clock sequence is provided, generate a random 14-bit clock sequence
    if clock_seq is None:
        clock_seq = random.getrandbits(14)

    # If no node ID is provided, generate a random 48-bit node ID
    if node is None:
        node = random.getrandbits(48)

    # Split the timestamp into its three components
    time_low = timestamp & 0xFFFFFFFF
    time_mid = (timestamp >> 32) & 0xFFFF
    time_hi = (timestamp >> 48) & 0x0FFF
    
    # Set the version to 1
    time_hi_and_version = time_hi | (1 << 12)
    
    # Set the variant (10xx)
    clock_seq_and_variant = clock_seq | 0x8000
    
    # Combine all components into the UUID format
    uuid_str = (
        f'{int_to_hex(time_low, 8)}-'
        f'{int_to_hex(time_mid, 4)}-'
        f'{int_to_hex(time_hi_and_version, 4)}-'
        f'{int_to_hex(clock_seq_and_variant, 4)}-'
        f'{int_to_hex(node, 12)}'
    )
    
    return uuid_str

def parse_uuid1(uuid_str):
    # Split the UUID into its components
    components = uuid_str.split('-')
    
    # Extract the parts of the UUID
    time_low = components[0]
    time_mid = components[1]
    time_hi_and_version = components[2]
    clock_seq_and_variant = components[3]
    node = components[4]

    # Convert hex parts to integers
    time_low = int(time_low, 16)
    time_mid = int(time_mid, 16)
    time_hi_and_version = int(time_hi_and_version, 16)
    clock_seq_and_variant = int(clock_seq_and_variant, 16)
    node = int(node, 16)
    
    # Extract the 12-bit high field of the timestamp
    time_hi = time_hi_and_version & 0x0FFF

    # Reconstruct the 60-bit timestamp
    timestamp = (time_hi << 48) | (time_mid << 32) | time_low
    
    # Extract the 14-bit clock sequence (clock_seq_and_variant's 14 least significant bits)
    clock_seq = clock_seq_and_variant & 0x3FFF
    
    # Format the node (48 bits) back to a MAC address-like format
    node_id = f'{node:012x}'

    return {
        'timestamp': timestamp,
        'clock_seq': clock_seq,
        'node_id': node_id
    }
    
def compare_uuid_generation():
    # Fixed values for the inputs
    fixed_timestamp = 139031362535006960  # Example timestamp in 100-nanosecond intervals since UUID epoch
    fixed_clock_seq = 15807               # Example 14-bit clock sequence
    fixed_node = 0x42010a0600a0           # Example 48-bit node ID (MAC address)

    # Generate the UUID using the fixed inputs
    generated_uuid = generate_uuid_v1(fixed_timestamp, fixed_clock_seq, fixed_node)
    print(f"Generated UUID: {generated_uuid}")

    # Decode the generated UUID
    decoded_uuid = parse_uuid1(generated_uuid)

    # Compare input values with decoded values
    print("\nComparing Input and Output:")
    print(f"Input Timestamp: {fixed_timestamp}")
    print(f"Decoded Timestamp: {decoded_uuid['timestamp']}")
    
    print(f"Input Clock Sequence: {fixed_clock_seq}")
    print(f"Decoded Clock Sequence: {decoded_uuid['clock_seq']}")
    
    print(f"Input Node ID: {hex(fixed_node)}")
    print(f"Decoded Node ID: {hex(int(decoded_uuid['node_id'], 16))}")
    print(f"Decoded Node ID (MAC Address format): {':'.join(decoded_uuid['node_id'][i:i+2] for i in range(0, 12, 2))}")
    
# Example usage:
def main():
    compare_uuid_generation()

if __name__ == "__main__":
    main()