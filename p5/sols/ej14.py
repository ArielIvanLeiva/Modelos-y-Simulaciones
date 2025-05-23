# %%
# Ejercicio 14
from numpy.random import rand
from numpy import log


class PoissonGen:
    def __init__(self, lam):
        self.lam = lam

    def sample_gen2(self, t, p):
        arrivals = []

        time_past = 0
        events = 0
        while time_past <= t:
            x = self.exp_sample()
            time_past += x

            if time_past <= t:
                u = rand()

                if u < p(t) / self.lam:
                    events += 1
                    arrivals.append((events, time_past))

        return (events, arrivals)
    
    def sample_gen(self, T, p):
        arrivals = []
        events = 0

        t = self.exp_sample()
        while t <= T:
            u = rand()

            if u < p(t) / self.lam:
                events += 1
                arrivals.append((events, t))
            
            x = self.exp_sample()
            t += x

        return (events, arrivals)

    def exp_sample(self):
        return -log(1 - rand()) / self.lam

# a)
# i)
def f1(x):
    return 3 + 4/(x+1)

# f1(1) = 7, el máximo de la función en el [0, 3]
lam = 7
P1 = PoissonGen(7)
p1_sample = lambda t: P1.sample_gen(t, f1)

# %%
from statutils.analysis import probability_of

n = 100000
t = 3
sample = [p1_sample(t) for _ in range(n)]
print(probability_of(sample, lambda x: x[0] <= 6))

import sympy as sp
x = sp.Symbol("x")

lm = float(sp.Integral(f1(x),(x, 0, t)).evalf())
import numpy as np
from math import factorial
from scipy.stats import poisson
poisson(mu=lm).cdf(6)