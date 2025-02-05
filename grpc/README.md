# Protobuf gRPC Hello World

This is a simple **Hello World** project using **Protocol Buffers (protobuf)** with **gRPC** in Python. It defines a basic RPC service that responds with a greeting message.

## Project Structure

```
.
├── hello.proto       # Protocol Buffers definition file
├── hello_pb2.py      # Generated protobuf message classes (after compilation)
├── hello_pb2_grpc.py # Generated gRPC service classes (after compilation)
├── server.py         # gRPC server implementation
├── client.py         # gRPC client implementation
├── README.md         # Project documentation
```

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- gRPC and Protocol Buffers compiler (`protoc`)
- Required Python packages:

  ```sh
  pip install grpcio grpcio-tools
  ```

## Step 1: Define the `.proto` file

The `hello.proto` file defines the `HelloService` with a `SayHello` RPC method:

```proto
syntax = "proto3";

package hello;

message HelloRequest {
  string name = 1;
}

message HelloResponse {
  string message = 1;
}

service HelloService {
  rpc SayHello (HelloRequest) returns (HelloResponse);
}
```

## Step 2: Compile the `.proto` file

Run the following command to generate the Python files:

```sh
protoc --proto_path=. --python_out=. --grpc_python_out=. hello.proto
```

If there is no protoc installed just use Python wrapper 
```sh
python -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. hello.proto
```
## Step 3: Run the Server

Start the gRPC server by running:

```sh
python server.py
```

The server will start on `localhost:50051`.

## Step 4: Run the Client

In another terminal, run the client:

```sh
python client.py
```

You should see the following output:

```
Response: Hello, World!
```

## Explanation

- **server.py**: Implements the `HelloService` gRPC server and listens for incoming requests.
- **client.py**: Sends a request to the server and prints the response.
- **hello.proto**: Defines the gRPC service and message format.




