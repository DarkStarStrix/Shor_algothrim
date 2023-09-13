# code rsa encryption in oop style and use shor's algorithm to break it

import math
import random

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer
from qiskit.tools.monitor import job_monitor
from qiskit.tools.visualization import plot_histogram

# code rsa encryption in oop style and use shor's algorithm to break it


def is_prime(p):
    for i in range(2, p):
        if p % i == 0:
            return False
    return True


def is_coprime(e, phi):
    if math.gcd(e, phi) == 1:
        return True
    return False


def generate_prime():
    while True:
        p = random.randint(2**10, 2**11)
        if is_prime(p):
            return p


class rsa:
    def __init__(self):
        self.p = generate_prime()
        self.q = generate_prime()
        self.N = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = self.generate_e()
        self.d = self.generate_d()
        self.n = math.ceil(math.log(self.N, 2))
        self.m = 2 * self.n
        self.qr = QuantumRegister(self.m, "qr")
        self.cr = ClassicalRegister(self.m, "cr")
        self.circuit = QuantumCircuit(self.qr, self.cr)
        self.circuit.h(self.qr[0: self.n])
        self.circuit.x(self.qr[self.n])
        self.circuit.barrier()
        self.circuit.draw(output="mpl")
        self.circuit.measure(self.qr, self.cr)
        self.circuit.draw(output="mpl")
        self.circuit.barrier()
        self.circuit.draw(output="mpl")
        self.circuit.measure(self.qr[0: self.n], self.cr[0: self.n])
        self.circuit.draw(output="mpl")
        self.circuit.barrier()
        self.circuit.draw(output="mpl")
        self.circuit.measure(self.qr[self.n: self.m], self.cr[self.n: self.m])
        self.circuit.draw(output="mpl")
        self.circuit.barrier()
        self.circuit.draw(output="mpl")
        self.circuit.measure(self.qr[0: self.n], self.cr[0: self.n])
        self.circuit.draw(output="mpl")
        self.circuit.barrier()
        self.circuit.draw(output="mpl")
        self.circuit.measure(self.qr[self.n: self.m], self.cr[self.n: self.m])
        self.circuit.draw(output="mpl")
        self.circuit.barrier()
        self.circuit.draw(output="mpl")
        self.circuit.measure(self.qr[0: self.n], self.cr[0: self.n])
        self.circuit.draw(output="mpl")
        self.circuit.barrier()
        self.circuit.draw(output="mpl")
        self.circuit.measure(self.qr[self.n: self.m], self.cr[self.n: self.m])
        self.circuit.draw(output="mpl")
        self.circuit.barrier()

    def generate_e(self):
        while True:
            e = random.randint(2, self.phi)
            if is_coprime(e, self.phi):
                return e

    def generate_d(self):
        for d in range(1, self.phi):
            if (d * self.e) % self.phi == 1:
                return d

    def encrypt(self, m):
        return (m**self.e) % self.N

    def decrypt(self, c):
        return (c**self.d) % self.N

    def run(self):
        backend = Aer.get_backend("qasm_simulator")
        job = execute(self.circuit, backend, shots=1000)
        job_monitor(job)
        result = job.result()
        counts = result.get_counts(self.circuit)
        print(counts)
        plot_histogram(counts)
        plt.show()

    def get_factors(self):
        backend = Aer.get_backend("qasm_simulator")
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
        backend = Aer.get_backend("qasm_simulator")
        job = execute(self.circuit, backend, shots=1000)
        job_monitor(job)
        result = job.result()
        counts = result.get_counts(self.circuit)
        print(counts)
        plot_histogram(counts)
        plt.show()

        # find the period
        # return the period

    def show(self):
        print("p: ", self.p)
        print("q: ", self.q)
        print("N: ", self.N)
        print("phi: ", self.phi)
        print("e: ", self.e)
        print("d: ", self.d)
        print("n: ", self.n)
        print("m: ", self.m)


if __name__ == "__main__":
    rsa = rsa()
    rsa.run()
    rsa.get_period()
    rsa.get_factors()
    rsa.show()
