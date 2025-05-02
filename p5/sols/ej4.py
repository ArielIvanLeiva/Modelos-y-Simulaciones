# %%
# Ejercicio 4
from numpy import log
from numpy.random import random
from statsUtils import get_density_frecuencies
from statistics import mean

def sample():
    u0 = random()
    
    exponent = -log(1-u0)
    u1 = random()
    return u1**(1/exponent)

n = 100000
samp = [sample() for _ in range(n)]

# %%
# Para testear
# mean(int(x <= 0.3) for x in samp)
#frecs = get_density_frecuencies(samp)