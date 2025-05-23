# %%
# Ejercicio 4
from numpy.random import random
from numpy import sqrt
from scipy.stats import norm
from statutils.execution import update_mean, update_scuad

# c)
print("c)")

def sim_M():
    m = 2

    u0 = random()
    u1 = random()

    while u1 >= u0:
        m += 1

        u0 = u1
        u1 = random()

    return m

def squad_restricted():
    squad = 0
    mean = sim_M()
    n = 1

    while n < 100 or (sqrt(squad / n) >= 0.01):
        n += 1

        x = sim_M()

        oldmean = mean
        mean = update_mean(mean, x, n)
        squad = update_scuad(squad, mean, oldmean, n)

    return mean

print(f"e estimation: {squad_restricted()}")

# %%
# Intervalo de confianza
def ic_restricted(l=0.025, alpha=0.05):
    mean = sim_M()
    percentil = norm.ppf(1 - alpha / 2, 0, 1)
    squad = 0
    n = 1

    # NOTE: Esto verifica el ANCHO del intervalo de confianza
    while n < 100 or 2 * sqrt(squad / n) * percentil >= l:
        n += 1

        x = sim_M()

        oldmean = mean
        mean = update_mean(oldmean, x, n)
        squad = update_scuad(squad, mean, oldmean, n)

    return n, mean, (mean - l/2, mean + l/2)

iterations, mean, ic = ic_restricted()
print("Confidence interval:")
print(f"Total iterations: {iterations}")
print(f"e estimation: {mean}")
print(f"ic: {ic}")

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