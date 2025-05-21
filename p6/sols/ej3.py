# %%
# Ejercicio 3
from numpy.random import random
import numpy as np
from scipy.stats import norm
import sympy as sp
from iterUtils import update_mean, update_scuad

def montecarlo_gen(fun, sl=0.001, alpha=0.05):
    mean = fun(random())
    percentil = norm.ppf(1-alpha/2, 0, 1)
    squad = 0
    n = 1
    
    # NOTE: Esto verifica unicamente el SEMI-ancho
    while n < 100 or np.sqrt(squad/n) * percentil >= sl:
        n += 1
        
        x = fun(random())
        
        oldmean = mean
        mean = update_mean(oldmean, x, n)
        squad = update_scuad(squad, mean, oldmean, n)

    return mean


# a)
# %%
# i)

x = sp.Symbol("x")
I = sp.Integral(sp.sin(x) / x, (x, sp.pi, 2*sp.pi))

def f(u):
    return np.sin(np.pi * u + np.pi)/(u + 1)

# a) Explicada en papel.
def montecarloi(sl=0.001, alpha=0.05):
    return montecarlo_gen(f, sl, alpha)

# b)
estimation = montecarloi()

# %%
print(f"Estimation: {estimation}")
print(f"Real: {I.evalf()}")


# %%
# ii)
x = sp.Symbol("x")
I = sp.Integral(3 / (3+ x**4),(x, 0, sp.oo))

def g(u):
    return 3/((3 + (1/ u - 1)**4) * u**2) 

def montecarloii(sl=0.001, alpha=0.05):
    return montecarlo_gen(g, sl, alpha)

# b)
estimation = montecarloii()

# %%
print(f"Estimation: {estimation}")
print(f"Real: {I.evalf()}")


# %%
# Testeando la verdadera confiabilidad del intervalo de i
from statistics import mean

def probability_of(sample, predicate):
    return mean(int(predicate(x)) for x in sample)

sample = [montecarloi() for _ in range(100)]

# %%
I = sp.Integral(sp.sin(x) / x, (x, sp.pi, 2*sp.pi))
Ival = float(I.evalf())

print(probability_of(sample, lambda x: (abs(x - Ival) < 0.001 )))
print(f"Expected: 0.95")
# %%