from qiskit import QuantumCircuit, transpile, assemble, execute, Aer

# Create a quantum circuit with one qubit and one classical bit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate to create superposition
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Choose appropriate simulator
simulator = Aer.get_backend('aer_simulator')

# Compile and run the circuit
compiled_circuit = transpile(qc, simulator)
job = simulator.run(assemble(compiled_circuit))
result = job.result()

# Get and print measurement outcome
counts = result.get_counts()
print("Quantum Hello World Output:", counts)
