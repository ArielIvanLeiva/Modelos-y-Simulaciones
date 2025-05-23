# %%
# Ejercicio 2
from numpy.random import random
import numpy as np
import sympy as sp
from statutils.execution import update_mean, update_scuad

# %%

def montecarlo_gen(fun, d=0.1):
    mean = fun(random())
    squad = 0
    n = 1

    while n < 100 or (np.sqrt(squad/n) >= d):
        n += 1

        x = fun(random())

        oldmean = mean
        mean = update_mean(mean, x, n)
        squad = update_scuad(squad, mean, oldmean, n)

    return mean

# %%
# i)
x = sp.Symbol("x")
I = sp.Integral(sp.exp(x) / sp.sqrt(2 * x), (x, 0, 1))

def f(u):
    return np.exp(u) / np.sqrt(2 * u)

# a) Explicada en papel.
def montecarloi(d=0.1):
    return montecarlo_gen(f, d)

# b)
estimation = montecarloi()

# %%
print(f"Estimation: {estimation}")
print(f"Real: {I.evalf()}")

# %%
# ii)
x = sp.Symbol("x")
I = sp.Integral(x**2 * sp.exp(-x**2),(x, -sp.oo, sp.oo))

def g(u):
    return np.log(1/u - 1)**2 * np.exp(-np.log(1/u - 1)**2) / (u * (1 - u))

def montecarloii(d=0.1):
    return montecarlo_gen(g, d)

# b)
estimation = montecarloii()

# %%
print(f"Estimation: {estimation}")
print(f"Real: {I.evalf()}")