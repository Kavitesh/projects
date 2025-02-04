import helloworld_pb2

# Create a HelloWorld message
msg = helloworld_pb2.HelloWorld(greeting="Hello", name="World")

# Serialize to binary
serialized_msg = msg.SerializeToString()

# Deserialize
deserialized_msg = helloworld_pb2.HelloWorld()
deserialized_msg.ParseFromString(serialized_msg)

# Print the message
print(f"{deserialized_msg.greeting}, {deserialized_msg.name}!")
