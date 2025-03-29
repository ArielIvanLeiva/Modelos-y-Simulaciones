# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: 3.12.7
#     language: python
#     name: python3
# ---

# %%
# Ejercicio 1

def nthNums(suc_fun, seed, n):
    x = seed
    nums = [x]
    
    for i in range(n):
        x = suc_fun(x)
        nums.append(x)

    return nums



# %%
def suc(x):
    return ((x*x)%1000000)//100

def nthVon(seed, n):
    return nthNums(suc, seed, n)

# a)
seeds = [3792, 1004, 2100, 1234]

secuences = [nthVon(seed, 10) for seed in seeds]
secuences


# %%
# b)
def suc_gen(a, b, m, x):
    return (a*x+b)%m

def suc(x):
    return suc_gen(5, 4, 2**5, x)

seeds = [4, 50]
secuences = [nthNums(suc, seed, 10) for seed in seeds]
secuences

# El período de la primer secuencia es 8
# Y el de la segunda secuencia es 7, comenzando desde el segundo valor.

 # %%
 # Ejercicio 2
from numpy.random import rand

# b)
ns = [100, 1000, 10000, 100000, 1000000]
estimations = []
for n in ns:
    success = 0
    u = rand(n)
    for num in u:
        if num < 1/2:
            x = rand() + rand()
        else:
            x = rand() + rand() + rand()
        success += x >= 1

    estimations.append(success/n)

estimations    

 # %%
 # Ejercicio 3
from numpy.random import rand

# b)
ns = [100, 1000, 10000, 100000, 1000000]
estimations = []
for n in ns:
    success = 0
    u = rand(n)
    for num in u:
        if num < 1/3:
            x = rand() + rand()
        else:
            x = rand() + rand() + rand()
        success += x <= 2

    estimations.append(success/n)

estimations    

# %%
# Ejercicio 4
import numpy as np
from numpy.random import rand
from numpy import log, exp


# Para simular las v.a. exponenciales:
class Exponential:
    def __init__(self, lamb):
        self.lamb = lamb

    def pdf(self, x):
        return self.lamb * exp(-self.lamb * x)

    def cdf(self, x):
        return 1 - exp(-self.lamb * x)

    def inversecdf(self, y):
        return -log(1 - y) / self.lamb

    def sample(self, size=1):
        uniform = rand() if size == 1 else rand(size)
        return self.inversecdf(uniform)


# v.a's. asociadas al tiempo de espera en cada caja.
X1 = Exponential(1 / 3)
X2 = Exponential(1 / 4)
X3 = Exponential(1 / 5)


class WaitingTime:
    def sample(self, size, return_ids=False):
        samp = []
        ids = []

        for _ in range(size):
            X, id = self.desition()
            samp.append(X.sample())
            ids.append(id)

        if return_ids:
            return (samp[0], ids[0]) if size == 1 else (np.array(samp), np.array(ids))
        else:
            return samp[0] if size == 1 else np.array(samp)

    def desition(self) -> Exponential:
        """
        Returns the random variable associated with the lane desition of a random client.
        """

        x = rand()

        if 0 <= x < 0.40:
            return (X1, 1)
        elif 0.40 <= x < 0.72:
            return (X2, 2)
        elif 0.72 <= x < 1:
            return (X3, 3)



# %%
# Probabilidades "exacta":
# a) P(T < 4 minutos)
a_prob = X1.cdf(4) * 0.4 + X2.cdf(4) * 0.32 + X3.cdf(4) * 0.28
print(f"P(T < 4 minutos) = {a_prob}")

# b) P(Vaya a caja i | T > 4 minutos)
b_prob = [
    (1 - X.cdf(4)) * sel_prob / (1 - a_prob)
    for X, sel_prob in zip([X1, X2, X3], [0.4, 0.32, 0.28])
]
print(f"P(Vaya a caja i | T > 4 minutos) = {b_prob}")

# Ap4oximaciones via simulación (c)):

# a)
T = WaitingTime()
sample = T.sample(1000)
a_aprox = sum(1 for num in sample if num < 4) / len(sample)

print(f"\nP(T < 4 minutos) ~ {a_aprox}")

# b)
# Creo primero una muestra considerable de casos en los que T > 4 minutos
big_sample, ids = T.sample(int(1000 / (1 - a_prob)), return_ids=True)
sample = [(t, id) for t, id in zip(big_sample, ids) if t > 4]

b_aprox = []

for i in [1, 2, 3]:
    aprox = sum(1 for t, id in sample if id == i) / len(sample)
    b_aprox.append(aprox)

print(f"P(Vaya a caja i | T > 4 minutos) ~ {b_aprox}")

# %%
