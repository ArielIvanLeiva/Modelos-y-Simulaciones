# %%
# Ejercicio 5
from numpy.random import random
from math import comb
import timeit

n = 10
p = 0.3


# I)
class InverseTranform:
    def __init__(self, values, p):
        assert len(values) == len(
            p
        ), "Mismatch between number of values and probabilities"
        assert (sum(p) - 1) < 0.00000000001, "Probabilities doesn't add up to one"

        self.dictionary = dict(sorted(zip(values, p), key=lambda x: x[1])[::-1])

        self.cummulative = {}
        summation = 0

        for x, px in self.dictionary.items():
            summation += px
            self.cummulative[x] = summation

    def p(self, x):
        return self.dictionary.get(x, 0)

    def sample(self):
        u = random()

        for x, sx in self.cummulative.items():
            if u <= sx:
                return x


def get_rel_frecuencies(sample, keys=range(1, 10 + 1)):
    frecuencies = {i: 0 for i in keys}

    for x in sample:
        if x in frecuencies.keys():
            frecuencies[x] += 1

    return {i: value / len(sample) for i, value in frecuencies.items()}


probs = [comb(n, k) * (p**k) * ((1 - p) ** (n - k)) for k in range(n + 1)]

Bin = InverseTranform(range(n + 1), probs)


# %%
# II)
def binomial_sample(n, p):
    assertions = 0

    for i in range(n):
        u = random()

        if u <= p:
            assertions += 1

    return assertions


# %%
# a)
num_of_executions = 10000
inv_time = timeit.timeit(Bin.sample, number=num_of_executions)/num_of_executions
full_sim_time = timeit.timeit(lambda: binomial_sample(n, p), number=num_of_executions)/num_of_executions

print(f"Average time of {num_of_executions} executions: ")
print(f"Inverse Transform method: {inv_time}")
print(f"Full simulation method: {full_sim_time}")

# %%
# b)
num_of_executions = 1000000

inv_sample = [Bin.sample() for _ in range(num_of_executions)]
inv_frecs = get_rel_frecuencies(inv_sample, keys=range(n + 1))

full_sim_sample = [binomial_sample(n, p) for _ in range(num_of_executions)]
full_sim_frecs = get_rel_frecuencies(full_sim_sample, keys=range(n + 1))

inv_mode = max(inv_frecs.items(), key=lambda x: x[1])[0]
full_sim_mode = max(full_sim_frecs.items(), key=lambda x: x[1])[0]

# %%
# c)
print(f"Inverse Transform mode: {inv_mode}")
print(f"Full simulation mode: {full_sim_mode}")
print()
print(f"p(0) and p(10) estimations:")
print(f"Inverse Transform estimations: p(0) = {inv_frecs[0]}, p(10) = {inv_frecs[10]}")
print(f"Full simulation estimations: p(0) = {full_sim_frecs[0]}, p(10) = {full_sim_frecs[10]}")
print()
print(f"p(0) and p(10) theorical: p(0) = {Bin.p(0)}, p(1) = {Bin.p(10)}")

# %%
