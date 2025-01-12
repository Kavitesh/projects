
# Helper Functions 
There are some frequent functions that are used when writing cryptography related code, here is a list:

- Text to Bytes Conversion [`text_to_bytes.py`](./text_to_bytes.py) : Most algorithms work with byte data so text needs to be converted.
- Number to Bytes Conversion [`number_to_bytes.py`](./number_to_bytes.py) : Many algorithms are based on mathematical calculations so convertion from bytes to numbers is required.
- Bytes to Hex String Conversion [`bytes_to_hex.py`](./bytes_to_hex.py) : Hexadecimal format is human readable and compatible with different os so it is used when we have to save and transfer binary keys.
- XOR [`xor.py`](./xor.py) : XOR is a very important operation when working at bit level, also bases for one-time pads