# %%
# Ejercicio 9
import timeit
from statistics import mean
from numpy.random import random
from numpy import log

def get_rel_frecuencies(sample, keys=range(1, 10 + 1)):
    frecuencies = {i: 0 for i in keys}

    for x in sample:
        if x in frecuencies.keys():
            frecuencies[x] += 1

    return {i: value / len(sample) for i, value in frecuencies.items()}


# %%
class Geom():
    def __init__(self, p):
        assert 0 <= p <= 1, f"p = {p}, wich is not a probability"

        self.p = p

    # a)
    def inv_method(self):
        p = self.p
        u = random()
        
        return int(log(1-u)/log(1-p)) + 1
    
    # b)
    def full_sim_method(self):
        u = random()
        tries = 0
        p = self.p
        
        while u >= p:
            tries += 1
            u = random()
            
        return tries + 1

# %%
X = Geom(0.8)
Y = Geom(0.2)

num_of_executions = 10000

def get_analysis(X: Geom, name):
    print(f"Analysis for {name} (Geom({X.p})):")
    
    inv_time = timeit.timeit(X.inv_method, number=num_of_executions)/num_of_executions
    full_sim_time = timeit.timeit(X.full_sim_method, number=num_of_executions)/num_of_executions

    inv_sample = iter(X.inv_method() for _ in range(num_of_executions))
    inv_mean = mean(inv_sample)

    full_sim_sample = iter(X.full_sim_method() for _ in range(num_of_executions))
    full_sim_mean = mean(full_sim_sample)

    print(f"Average time/value from {num_of_executions} executions:")
    print(f"Inverse transform method: \n\ttime: {inv_time},  value: {inv_mean}")
    print(f"Full simulation: \n\ttime: {full_sim_time},  value: {full_sim_mean}")
    print(f"Real expected value: E({name}) = {1/X.p}\n")

get_analysis(X, "X")
get_analysis(Y, "Y")

# %%
#get_rel_frecuencies([X.full_sim_method() for _ in range(100000)])
#get_rel_frecuencies([X.inv_method() for _ in range(100000)])

