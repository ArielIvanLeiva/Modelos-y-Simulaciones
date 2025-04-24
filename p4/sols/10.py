# %%
# Ejercicio 10
from numpy.random import random
from numpy import log


def get_rel_frecuencies(sample, keys=range(1, 10 + 1)):
    frecuencies = {i: 0 for i in keys}

    for x in sample:
        if x in frecuencies.keys():
            frecuencies[x] += 1

    return {i: value / len(sample) for i, value in frecuencies.items()}


class Geom:
    def __init__(self, p):
        assert 0 <= p <= 1, f"p = {p}, wich is not a probability"

        self.p = p

    def inv_method(self):
        p = self.p
        u = random()

        return int(log(1 - u) / log(1 - p)) + 1


# a)
# Notemos que X puede pensarse como composición de dos v.a's geométricas:
X1 = Geom(1 / 2)
X2 = Geom(1 / 3)

# P(X = i) = (1/2) * P(X1 = i) + (1 - 1/2) * P(X2 = i)
# = (1/2) * ((1/2) * (1/2)**(i-1)) + (1/2) * ((1/3) * (1 - 1/3)**(i-1))


def composition(X1: Geom, X2: Geom, alpha):
    u = random()

    if u < alpha:
        return X1.inv_method()
    else:
        return X2.inv_method()


# %%
sample = [composition(X1, X2, 0.5) for _ in range(100000)]

# get_rel_frecuencies(sample, keys=range(0,100))
