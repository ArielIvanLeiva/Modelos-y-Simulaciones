# %%
# Ejercicio 6
from numpy.random import random
from numpy import sqrt
from scipy.stats import norm
from statutils.execution import update_mean, update_scuad

def sim_bernoulli():
    x = 2 * random() - 1
    y = 2 * random() - 1

    return x**2 + y**2 <= 1

# a)

def estimate_fraction(d=0.01):
    mean = sim_bernoulli()
    squad = 0
    
    n = 1
    
    while n < 100 or sqrt(squad/n) >= d:
        n += 1
        
        x = sim_bernoulli()
        
        oldmean = mean
        mean = update_mean(oldmean, x, n)
        squad = update_scuad(squad, mean, oldmean, n)

    return mean

p = estimate_fraction()
print("a)")
print(f"Estimation of the fraction: {p}")

# %%
# b)
def estimate_pi(l=0.1, alpha=0.05):
    mean = sim_bernoulli()
    squad = 0
    percentil = norm.ppf(1-alpha/2)
    n = 1
    
    # NOTE: Esta verificación de condición está pensada para este caso particular
    while n < 100 or 2*sqrt(squad/n) * percentil >= l/4:
        n += 1
        
        x = sim_bernoulli()
        
        oldmean = mean
        mean = update_mean(oldmean, x, n)
        squad = update_scuad(squad, mean, oldmean, n)

    # NOTE: Este retorno de valores está pensado para este caso particular
    return n, 4*mean, (4*(mean - (l/4)/2), 4*(mean + (l/4)/2))

iterations, estimation, ic = estimate_pi()

print("b)")
print(f"iterations: {iterations}")
print(f"pi estimation: {estimation}")
print(f"ic (of length {ic[1] - ic[0]}): {ic}")

# %%
# Testeando la confiabilidad del intervalo
from numpy import pi

ics = [estimate_pi()[2] for _ in range(200)]

# %%
from statutils.analysis import get_ic_confidence

confidence = get_ic_confidence(ics, pi)
print(f"Estimated confidence: {confidence}")
print("Expected: 0.95")
