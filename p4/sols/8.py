# %%
# Ejercicio 8
from numpy.random import random
from numpy import exp
from math import factorial
from statistics import mean

def get_rel_frecuencies(sample, keys=range(1, 10 + 1)):
    frecuencies = {i: 0 for i in keys}

    for x in sample:
        if x in frecuencies.keys():
            frecuencies[x] += 1

    return {i: value / len(sample) for i, value in frecuencies.items()}

# a)
def inv_method(lam, k):
    l = exp(-lam)*sum(lam**j / factorial(j) for j in range(k+1))
    p0 = exp(-lam)/l
    F = p0
    max_index = min(int(lam), k)

    for j in range(1, max_index + 1):
        p0 *= lam / j
        F += p0

    u = random()
    if u >= F:
        j = max_index + 1

        while u >= F:
            p0 *= lam / j
            F += p0
            j += 1

        return j - 1
    else:
        j = max_index

        while u < F:
            F -= p0
            p0 *= j / lam
            j -= 1

        return j + 1

lam = 0.7
k = 10
l = exp(-lam)*sum(lam**j / factorial(j) for j in range(k+1))
p = [exp(-lam)*lam**j / (factorial(j) * l) for j in range(k+1)]

def reject_method(lam, k):
    max_index = min(int(lam), k)
    c = (k+1) * (exp(-lam) * (lam**max_index)/factorial(max_index))/l

    y = int((k+1) * random())
    u = random()
    
    while u >= (k+1) * p[y]/c:
        y = int((k+1) * random())
        u = random()
        
    return y
        

#get_rel_frecuencies([reject_method(0.7, 10) for _ in range(40000)], range(11))
#get_rel_frecuencies([inv_method(0.7, 10) for _ in range(40000)], range(11))

# %%
inv_sample = iter(inv_method(0.7, 10) for _ in range(1000))
inv_estimation = mean(x > 2 for x in inv_sample)

reject_sample = iter(inv_method(0.7, 10) for _ in range(1000))
rejection_estimation = mean(x > 2 for x in reject_sample)
real_value = sum(p[i] for i in range(3, k+1))

print("Estimations of P(X > 2):")
print(f"Inverse Transform: {inv_estimation}")
print(f"Acceptance-rejection method: {rejection_estimation}")
print(f"Real value: {real_value}")

# %%
