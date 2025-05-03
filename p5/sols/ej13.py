# %%
# Ejercicio 13
from ej12 import Poisson
from numpy.random import rand

P = Poisson(5)
def sample(t):
    n_events, _ = P.sample(t)

    random_samp = (40 - 20 + 1) * rand(n_events) + 20
    enthusiats_events = sum([int(x) for x in random_samp])

    return enthusiats_events


#  Luego la cantidad que deseamos simular se calcula usando:
sample(1)
