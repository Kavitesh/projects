def hex_to_int(hex_str):
    return int(hex_str, 16)

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
    time_low = hex_to_int(time_low)
    time_mid = hex_to_int(time_mid)
    time_hi_and_version = hex_to_int(time_hi_and_version)
    clock_seq_and_variant = hex_to_int(clock_seq_and_variant)
    node = hex_to_int(node)
    
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

# Example usage:
def main():
    uuid_str = 'a089a2f0-f049-11ed-bdbf-42010a0600a0'
    result = parse_uuid1(uuid_str)

    print(f"UUID: {uuid_str}")
    print(f"Timestamp: {result['timestamp']}")
    print(f"Clock Sequence: {result['clock_seq']}")
    print(f"Node ID: {result['node_id']} (MAC Address format: {':'.join(result['node_id'][i:i+2] for i in range(0, 12, 2))})")

if __name__ == "__main__":
    main()