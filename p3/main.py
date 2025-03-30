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
    return ((x * x) % 1000000) // 100


def nthVon(seed, n):
    return nthNums(suc, seed, n)


# a)
seeds = [3792, 1004, 2100, 1234]

secuences = [nthVon(seed, 10) for seed in seeds]
secuences


# %%
# b)
def suc_gen(a, b, m, x):
    return (a * x + b) % m


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
        if num < 1 / 2:
            x = rand() + rand()
        else:
            x = rand() + rand() + rand()
        success += x >= 1

    estimations.append(success / n)

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
        if num < 1 / 3:
            x = rand() + rand()
        else:
            x = rand() + rand() + rand()
        success += x <= 2

    estimations.append(success / n)

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
# Ejercicio 5

import inspect
from numpy.random import uniform
from numpy import log
from statistics import mean
import pandas as pd
import sympy as sp
from IPython.display import display, Math

ns = [100, 1000, 10000, 100000, 1000000]
df = pd.DataFrame(index=ns, columns=[f"({l})" for l in list("abcdef")])


def get_aprox(f, sizes):
    parameter_size = len(inspect.signature(f).parameters)
    monte_aproximations = []
    for n in sizes:
        inputs = [uniform(size=n) for _ in range(parameter_size)]
        monte_aprox = mean(f(*inputs))
        monte_aproximations.append(monte_aprox)

    return monte_aproximations[0] if len(sizes) == 1 else monte_aproximations

def print_equality(I, y):
    latex_str = r"{} = {} \sim {}".format(sp.latex(I), sp.latex(y), sp.latex(I.doit().evalf()))
    display(Math(latex_str))


x = sp.symbols("x")
y = sp.symbols("y")

# a)
fexpr = (1 - x**2) ** (3 / 2)
f = sp.lambdify(x, fexpr)
I = sp.Integral(fexpr, (x, 0, 1))

print("a)")
print_equality(I, 3 * sp.pi / 16)

df["(a)"] = get_aprox(f, ns)

# b)
fexpr = x / (x**2 - 1)
I = sp.Integral(fexpr, (x, 2, 3))
f = sp.lambdify(x, fexpr.subs(x, x + 2))

print("b)")
print_equality(I, sp.ln(sp.Rational(8, 3)) / 2)

df["(b)"] = get_aprox(f, ns)

# c)
fexpr = x / ((1 + x**2) ** 2)
I = sp.Integral(fexpr, (x, 0, sp.oo))
f = sp.lambdify(x, fexpr.subs(x, 1 / x - 1) / (x**2))

print("c)")
print_equality(I, sp.Rational(1, 2))

df["(c)"] = get_aprox(f, ns)

# d)
fexpr = sp.exp(-(x**2))
I = sp.Integral(fexpr, (x, -sp.oo, sp.oo))
f = sp.lambdify(x, fexpr.subs(x, -sp.ln(1 / x - 1)) / (x * (1 - x))) 

print("d)")
print_equality(I, sp.sqrt(sp.pi))

df["(d)"] = get_aprox(f, ns)
df

# e)
fexpr = sp.exp((x + y)**2)
I = sp.Integral(fexpr, (x, 0, 1), (y, 0, 1))
f = sp.lambdify((x, y), fexpr) 

print("e)")
print_equality(I, I.doit())

df["(e)"] = get_aprox(f, ns)

# f)
def lt(y, x):
    return y < x

fexpr = sp.exp(-(x + y))
I = sp.Integral(fexpr, (y, 0, x), (x, 0, sp.oo))

adjusted_fexpr = (fexpr * sp.Piecewise((1, lt(y, x)), (0, True)))
adjusted_fexpr = adjusted_fexpr.subs({x: (1/x)-1, y: (1/y)-1}) / (x**2 * y**2)
f = sp.lambdify((x, y), adjusted_fexpr)

print("f)")
print_equality(I, I.doit())

df["(f)"] = get_aprox(f, ns)

df
