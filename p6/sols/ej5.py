# %%
# Ejercicio 5
# c)
from numpy.random import random
from numpy import sqrt
from scipy.stats import norm
from statutils.execution import update_mean, update_scuad


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

    return mean, squad/n

mean, estimator_squad = squad_restricted()

print(f"c) e estimation: {mean}")
print(f"variance of the estimator: {estimator_squad}")

# %%
# Intervalo de confianza
def ic_restricted(l=0.1, alpha=0.05):
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

# %%
iterations, mean, ic = ic_restricted()
print("Confidence interval:")
print(f"Total iterations: {iterations}")
print(f"e estimation: {mean}")
print(f"ic (of length {ic[1] - ic[0]}): {ic}")

# %%
# Testeando el intervalo de confianza
ics = [ic_restricted()[2] for _ in range(1000)]

# %%
from numpy import e
from statutils.analysis import get_ic_confidence

confidence = get_ic_confidence(ics, e)
print(f"Estimated confidence: {confidence}")
print("Expected: 0.95")