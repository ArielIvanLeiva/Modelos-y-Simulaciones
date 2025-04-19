# %%
# Ejercicio 7
from numpy.random import random
from numpy import exp
from statistics import mean

def get_rel_frecuencies(sample, keys=range(1, 10 + 1)):
    frecuencies = {i: 0 for i in keys}

    for x in sample:
        if x in frecuencies.keys():
            frecuencies[x] += 1

    return {i: value / len(sample) for i, value in frecuencies.items()}

def inv_poisson(lam):
    p = exp(-lam)    
    F = p
    u = random()
    j = 0
    
    while u >= F:
        j += 1
        p *= lam/j
        F += p
        
    return j

#get_rel_frecuencies([inv_poisson(10) for _ in range(1000000)], range(10))
# %%
def optimized_poisson(lam):
    p = exp(-lam)
    F = p
    
    for j in range(1, int(lam) + 1):
        p *= lam/j
        F += p
    
    u = random()

    if (u >= F):
        j = int(lam) + 1
        
        while(u >= F):
            p *= lam/j
            F += p
            j += 1
            
        return j-1
    else:
        j = int(lam)
        
        while(u < F):
            F -= p
            p *= j/lam
            j -= 1
            
        return j+1
    
#get_rel_frecuencies([optimized_poisson(10) for _ in range(1000000)], range(10))

# %%
inv_estimation = mean(inv_poisson(10) > 2 for _ in range(1000))
optimized_estimation = mean(optimized_poisson(10) > 2 for _ in range(1000))

print("Estimations of P(Y > 2):")
print(f"Naïve Inverse Transform: {inv_estimation}")
print(f"Optimized Inverse Transform: {optimized_estimation}")