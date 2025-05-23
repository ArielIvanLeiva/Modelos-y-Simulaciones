# %%
# Ejercicio 4
from numpy.random import random
from numpy import sqrt
from scipy.stats import norm
from statutils.execution import update_mean, update_scuad

def sim_N():
    sum = random()
    n = 1
    
    while sum <= 1:
        n += 1
        sum += random()
    
    return n 

# a) y b)
def fixed_executions(size=1000):
    mean = sim_N()
    squad = 0
    n = 1
    
    while n <= size:
        n += 1
        
        x = sim_N()
        
        oldmean = mean
        mean = update_mean(oldmean, x, n)
        squad = update_scuad(squad, mean, oldmean, n)
    
    return mean, squad/n

mean, squad = fixed_executions(1000)

print(f"a) e estimation from 1000 repetitions: {mean}")
print(f"b) estimator sample variance from 1000 repetitions: {squad}")
        
# %%
# Intervalo de confianza
def ic_restricted(l=0.025, alpha=0.05):
    mean = sim_N()
    percentil = norm.ppf(1 - alpha / 2, 0, 1)
    squad = 0
    n = 1

    # NOTE: Esto verifica el ANCHO del intervalo de confianza
    while n < 100 or 2 * sqrt(squad / n) * percentil >= l:
        n += 1

        x = sim_N()

        oldmean = mean
        mean = update_mean(oldmean, x, n)
        squad = update_scuad(squad, mean, oldmean, n)

    return n, mean, (mean - l/2, mean + l/2)

iterations, mean, ic = ic_restricted()
print("Confidence interval:")
print(f"Total iterations: {iterations}")
print(f"e estimation: {mean}")
print(f"ic (of length {ic[1] - ic[0]}): {ic}")

# %%
# Testeando la verdadera confiabilidad del intervalo (de dos formas equivalentes)
sample = [ic_restricted() for _ in range(200)]

# %%
from numpy import e
from statutils.analysis import get_ic_confidence
from statutils.analysis import probability_of

ics = [result[2] for result in sample]
confidence = get_ic_confidence(ics, e)

print("Confiability test results:")
print(f"Test 1: {confidence}")
print(f"Test 2: {probability_of(sample, lambda x: (abs(x[1] - e) < 0.025/2 ))}")
print(f"Expected: 0.95")
# %%