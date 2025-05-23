# %%
# Ejercicio 3
import numpy as np
import sympy as sp
from numpy.random import random
from scipy.stats import norm
from statutils.execution import update_mean, update_scuad
import pandas as pd

def montecarlo_gen(fun, sl=0.001, alpha=0.05, checkpoints={}):
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
        
        if n in checkpoints.keys():
            checkpoints[n] = [mean, np.sqrt(squad), (mean - sl, mean + sl)]

    return mean, {n: [mean, np.sqrt(squad), (mean - sl, mean + sl)]}

def setup_df(analysis_dict):
    cols = ['I', 'S', 'IC']
    df = pd.DataFrame.from_dict(analysis_dict, orient='index', columns=cols)

    return df

def pretty_print_analysis(df):
    df_copy = df.copy()
    df_copy = df_copy.round(4)
    df_copy['IC'] = df_copy['IC'].apply(lambda t: (round(t[0], 4), round(t[1], 4)))
    
    print(df_copy)

# a)
# %%
# i)

x = sp.Symbol("x")
I = sp.Integral(sp.sin(x) / x, (x, sp.pi, 2*sp.pi))

def f(u):
    return np.sin(np.pi * u + np.pi)/(u + 1)

# a) Explicada en papel.
def montecarloi(sl=0.001, alpha=0.05, checkpoints={}):
    return montecarlo_gen(f, sl, alpha, checkpoints)

# b)
checkpoints = {1000: (), 5000: (), 7000: ()}
estimation, last_results = montecarloi(checkpoints=checkpoints)
checkpoints.update(last_results)

# %%
print(f"Estimation: {estimation}")
print(f"Real: {I.evalf()}\n")

df = setup_df(checkpoints)
pretty_print_analysis(df)
# %%
# ii)
x = sp.Symbol("x")
I = sp.Integral(3 / (3+ x**4),(x, 0, sp.oo))

def g(u):
    return 3/((3 + (1/ u - 1)**4) * u**2) 

def montecarloii(sl=0.001, alpha=0.05, checkpoints=[]):
    return montecarlo_gen(g, sl, alpha, checkpoints=checkpoints)

# b)
checkpoints = {1000: (), 5000: (), 7000: ()}
estimation, last_results = montecarloii(checkpoints=checkpoints)
checkpoints.update(last_results)

# %%
print(f"Estimation: {estimation}")
print(f"Real: {I.evalf()}")

df = setup_df(checkpoints)
pretty_print_analysis(df)

# %%
# Testeando la verdadera confiabilidad del intervalo de i
sample = [montecarloi() for _ in range(100)]

# %%
from statutils.analysis import probability_of

I = sp.Integral(sp.sin(x) / x, (x, sp.pi, 2*sp.pi))
Ival = float(I.evalf())

print(probability_of(sample, lambda x: (abs(x[0] - Ival) < 0.001 )))
print(f"Expected: 0.95")
# %%