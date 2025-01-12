import time
import random

def int_to_hex(value, length):
    return f'{value:0{length}x}'

def generate_uuid_v1(timestamp, clock_seq, node):
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

# Example usage:
def main():
    # Example Inputs:
    timestamp = 139031362535006960  # Example timestamp in 100-nanosecond intervals since UUID epoch
    clock_seq = 15807               # Example 14-bit clock sequence
    node = 0x42010a0600a0           # Example 48-bit node ID (MAC address)
    node_str = int_to_hex(node,12)

    # Generate and print the UUID Version 1 using provided inputs
    custom_uuid_v1 = generate_uuid_v1(timestamp, clock_seq, node)    
    print(f"UUID: {custom_uuid_v1}")
    print(f"Timestamp: {timestamp}")
    print(f"Clock Sequence: {clock_seq}")
    print(f"Node ID: {node_str} (MAC Address format: {':'.join(node_str[i:i+2] for i in range(0, 12, 2))})")

if __name__ == "__main__":
    main()