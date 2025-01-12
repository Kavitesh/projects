# One-Time Pad 

A one-time pad (OTP) is a theoretically unbreakable encryption technique if used correctly. 
It involves using a random key that is as long as the message itself. Each character of the plaintext is combined with a character from the key using bitwise XOR (exclusive or).


## Key Generation

1. Generate a random key only condition is that is has same length as the message.

## Encryption

1. The message and the key are converted to their binary forms.
2. A bitwise XOR operation is performed on the binary message and binary key to produce the encrypted binary message.
3. The encrypted binary message is then converted back to a readable string format for display.

## Decryption

1. The encrypted binary message is XORed with the same binary key to retrieve the original binary message.
2. The binary message is converted back to the original plaintext message.

## Python Implementation

You can find a small Python implementation of the RSA algorithm in the [`one_time_pad.py`](./one_time_pad.py) file. This script includes functions for key generation, encryption, and decryption. 
For helper functions please check [`helper_functions`](../helper_functions/helper_functions.md)