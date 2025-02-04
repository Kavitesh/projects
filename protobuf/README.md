# Protobuf Hello World

This is a simple example of using Protocol Buffers (protobuf) for serializing and deserializing messages in Python. It defines a `HelloWorld` message structure and demonstrates how to work with it in Python.

## Prerequisites

Before starting, make sure you have the following installed:

- **Python 3.x**
- **Protocol Buffers Compiler (protoc)**

## Installation Steps

### 1. Install Python (if not already installed)

If Python is not installed, download and install it from [the official Python website](https://www.python.org/downloads/).

### 2. Install Protocol Buffers Compiler (protoc)

Protocol Buffers requires the `protoc` compiler to generate code. Here are installation steps for various systems:

#### On macOS (via Homebrew)
```sh
brew install protobuf
```

#### On Ubuntu/Debian-based systems
```sh
sudo apt update
sudo apt install -y protobuf-compiler
```

#### On Windows

- Download the latest version of `protoc` from the [protobuf releases page](https://github.com/protocolbuffers/protobuf/releases).
- Extract the downloaded archive and add the `bin` folder to your system `PATH` environment variable.

### 3. Clone the Repository

Clone this repository to your local machine:
```sh
git clone https://github.com/Kavitesh/projects.git
cd protobuf
```

### 4. Install Python Dependencies

Install the required Python libraries:

```sh
pip install -r requirements.txt
```

The `requirements.txt` file includes the `protobuf` Python package.

### 5. Generate Python Code from `.proto` File

Generate the Python code from the `helloworld.proto` file by running the following `protoc` command:

```sh
protoc --python_out=. helloworld.proto
```

This will create a file called `helloworld_pb2.py` which contains the Python bindings for your Protobuf messages.

### 6. Run the Example

Run the Python script to serialize and deserialize a `HelloWorld` message:

```sh
python example.py
```

You should see the output:
```
Hello, World!
```

---

## File Structure

```
protobuf-helloworld/
│
├── helloworld.proto        # Protocol Buffers schema definition
├── helloworld_pb2.py       # Generated Python code from .proto
├── example.py              # Python example that uses the generated code
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

