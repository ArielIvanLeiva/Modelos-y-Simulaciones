# %%
from numpy.random import random
from math import comb
import timeit

# Ejercicio 6
def get_rel_frecuencies(sample, keys=range(1, 10 + 1)):
    frecuencies = {i: 0 for i in keys}

    for x in sample:
        if x in frecuencies.keys():
            frecuencies[x] += 1

    return {i: value / len(sample) for i, value in frecuencies.items()}

# get cummulative sum, malpensadx
def get_cum(p):
    cum = []

    cum_sum = 0
    for x, prob in p:
        cum_sum += prob
        cum.append((x, cum_sum))

    return cum


p = [0.15, 0.20, 0.10, 0.35, 0.20]
probs = zip(range(len(p)), p)
probs = sorted(probs, key=lambda x: x[1])[::-1]
F = get_cum(probs)

# %%
# I)
def get_sample(F):
    u = random()
    for x, prob in F:
        if u <= prob:
            return x

def inv_sample():
    return get_sample(F)

# %%
def optimized_bin(n, p):
    p0 = (1-p)**n
    F = p0
    
    max_bin = int(n * max(p, (1-p)))
    
    for j in range(1, max_bin + 1):
        p0 *= ((n-j+1)/j) * (p / (1-p))
        F += p0

    u = random()
    if (u >= F):
        j = max_bin + 1
        
        while(u >= F):
            p0 *= ((n-j+1)/j) * (p / (1-p))
            F += p0
            j += 1
            
        return j-1
    else:
        j = max_bin
        
        while(u < F):
            F -= p0
            p0 *= j/((n-j+1) * (p / (1-p)))
            j -= 1
            
        return j+1


q = [comb(4, k) * (0.45**k) * ((1 - 0.45) ** (4 - k)) for k in range(4 + 1)]
probs = sorted(zip(range(4+1), q), key=lambda x: x[1])[::-1]

c = 1
for k in range(len(q)):
    c = max(c, p[k]/q[k])

y_cum = get_cum(probs)
def y_sample():
    #return get_sample(y_cum) Could have been another possibility
    return optimized_bin(4, 0.45)

def reject_sample(c):
    y = y_sample()
    u = random()
    
    while(u >= p[y]/(q[y]*c)):
        y = y_sample()
        u = random()
        
    return y
    
# For testing
#get_rel_frecuencies([y_sample() for _ in range(10000)], range(5))
#get_rel_frecuencies([reject_sample(c) for _ in range(100000)], range(5))
#get_rel_frecuencies([inv_sample() for _ in range(100000)], range(5))
#get_rel_frecuencies([optimized_bin(4, 0.45) for _ in range(100000)], range(5))
# %%
# III)
num_of_executions = 10000
reject_time = timeit.timeit(lambda: reject_sample(c), number=num_of_executions)/num_of_executions
inv_time = timeit.timeit(inv_sample, number=num_of_executions)/num_of_executions

print(f"Average time of {num_of_executions} executions: ")
print(f"Inverse Transform method: {inv_time}")
print(f"Acceptance-rejection method: {reject_time}")