# Quantum Hello World using Qiskit

## Introduction
Quantum computing operates on qubits, which differ from classical bits because they can exist in a superposition of both 0 and 1 states simultaneously. This program demonstrates a **Hello World** equivalent using quantum superposition and measurement in Qiskit.

This quantum program demonstrates:
1. **Superposition** using the Hadamard gate.
2. **Quantum measurement**, collapsing the state into `0` or `1`.
3. **Random outcomes**, a key principle in quantum computing.

## Prerequisites
To run this program, you need to install Qiskit:
```bash
pip install qiskit
```

## Code Explanation
```python
from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
```
- **QuantumCircuit**: Used to create and manipulate quantum circuits.
- **Aer**: Qiskit's simulator backend for running quantum circuits.
- **transpile, assemble, execute**: Functions to optimize and run quantum circuits.

### Step 1: Create a Quantum Circuit
```python
qc = QuantumCircuit(1, 1)  # 1 qubit, 1 classical bit
```
This initializes a quantum circuit with **one qubit** and **one classical bit** for measurement.

### Step 2: Apply Hadamard Gate
```python
qc.h(0)  # Apply Hadamard gate to qubit 0
```
The Hadamard gate places the qubit in a **superposition state**, meaning it is both **0 and 1** at the same time with equal probability.

### Step 3: Measure the Qubit
```python
qc.measure(0, 0)  # Measure qubit and store result in classical bit
```
Measurement collapses the qubit into either **0 or 1**, randomly with equal probability.

### Step 4: Simulate the Quantum Circuit
```python
simulator = Aer.get_backend('aer_simulator')
compiled_circuit = transpile(qc, simulator)
job = simulator.run(assemble(compiled_circuit))
result = job.result()
```
- **Aer Simulator** executes the quantum circuit.
- **transpile()** optimizes the circuit for the simulator.
- **assemble()** prepares the circuit for execution.

### Step 5: Retrieve the Result
```python
counts = result.get_counts()
print("Quantum Hello World Output:", counts)
```
This prints the count of measurement outcomes (usually close to 50% `0` and 50% `1`).

## Expected Output
```
Quantum Hello World Output: {'0': 512, '1': 512}
```
(Running multiple times may yield slightly different results.)
