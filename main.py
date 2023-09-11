# code peter shor's algorithm in oop style

import math

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer
from qiskit.tools.monitor import job_monitor
from qiskit.tools.visualization import plot_histogram


# find prime factors of N
class quantum_shor:
    def __init__(self, N):
        self.N = N
        self.n = math.ceil(math.log(N, 2))
        self.m = 2 * self.n
        self.qr = QuantumRegister(self.m, 'qr')
        self.cr = ClassicalRegister(self.m, 'cr')
        self.circuit = QuantumCircuit(self.qr, self.cr)
        self.circuit.h(self.qr[0:self.n])
        self.circuit.x(self.qr[self.n])
        self.circuit.barrier()
        self.circuit.draw(output='mpl')
        self.circuit.measure(self.qr, self.cr)
        self.circuit.draw(output='mpl')
        self.circuit.barrier()
        self.circuit.draw(output='mpl')
        self.circuit.measure(self.qr[0:self.n], self.cr[0:self.n])
        self.circuit.draw(output='mpl')
        self.circuit.barrier()
        self.circuit.draw(output='mpl')
        self.circuit.measure(self.qr[self.n:self.m], self.cr[self.n:self.m])
        self.circuit.draw(output='mpl')
        self.circuit.barrier()
        self.circuit.draw(output='mpl')
        self.circuit.measure(self.qr[0:self.n], self.cr[0:self.n])
        self.circuit.draw(output='mpl')
        self.circuit.barrier()
        self.circuit.draw(output='mpl')
        self.circuit.measure(self.qr[self.n:self.m], self.cr[self.n:self.m])
        self.circuit.draw(output='mpl')
        self.circuit.barrier()
        self.circuit.draw(output='mpl')
        self.circuit.measure(self.qr[0:self.n], self.cr[0:self.n])
        self.circuit.draw(output='mpl')
        self.circuit.barrier()
        self.circuit.draw(output='mpl')
        self.circuit.measure(self.qr[self.n:self.m], self.cr[self.n:self.m])
        self.circuit.draw(output='mpl')
        self.circuit.barrier()
        self.circuit.draw(output='mpl')

    def run(self):
        backend = Aer.get_backend('qasm_simulator')
        job = execute(self.circuit, backend, shots=1000)
        job_monitor(job)
        result = job.result()
        counts = result.get_counts(self.circuit)
        print(counts)
        plot_histogram(counts)
        plt.show()

    def get_factors(self):
        backend = Aer.get_backend('qasm_simulator')
        job = execute(self.circuit, backend, shots=1000)
        job_monitor(job)
        result = job.result()
        counts = result.get_counts(self.circuit)
        print(counts)
        plot_histogram(counts)
        plt.show()

            # find the period
            # find the factors
            # return the factors

    def get_period(self):
        backend = Aer.get_backend('qasm_simulator')
        job = execute(self.circuit, backend, shots=1000)
        job_monitor(job)
        result = job.result()
        counts = result.get_counts(self.circuit)
        print(counts)
        plot_histogram(counts)
        plt.show()

    # show the circuit
    def show(self):
        self.circuit.draw(output='mpl')
        plt.show()

    # def main function
    def main(self):
        self.run()
        self.get_period()
        self.get_factors()
        self.show()

# main function


if __name__ == '__main__':
    N = 15
    shor = quantum_shor(N)
    shor.main()
