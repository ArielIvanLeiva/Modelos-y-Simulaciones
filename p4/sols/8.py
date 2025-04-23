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


class XVariable():
    
    def __init__(self, lam, k):
        self.lam = lam
        self.k = k
        self.norm_const = exp(-lam)*sum(lam**j / factorial(j) for j in range(k+1))
        self.p = [exp(-lam)*lam**j / (factorial(j) * self.norm_const) for j in range(k+1)]
        
    # a)
    def inv_method(self):
        lam = self.lam
        k = self.k
        norm_const = self.norm_const
        
        p0 = exp(-lam)/norm_const
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


    def reject_method(self):
        lam = self.lam
        k = self.k
        norm_const = self.norm_const
        p = self.p
        
        max_index = min(int(lam), k)
        c = (k+1) * (exp(-lam) * (lam**max_index)/factorial(max_index))/norm_const

        y = int((k+1) * random())
        u = random()
        
        while u >= (k+1) * p[y]/c:
            y = int((k+1) * random())
            u = random()
            
        return y


# %%
lam = 0.7
k = 10
norm_const = exp(-lam)*sum(lam**j / factorial(j) for j in range(k+1))
q = [exp(-lam)*lam**j / (factorial(j) * norm_const) for j in range(k+1)]

X = XVariable(lam, k)

inv_sample = iter(X.inv_method() for _ in range(1000))
inv_estimation = mean(x > 2 for x in inv_sample)

reject_sample = iter(X.inv_method() for _ in range(1000))
rejection_estimation = mean(x > 2 for x in reject_sample)
real_value = sum(q[i] for i in range(3, k+1))

print("Estimations of P(X > 2):")
print(f"Inverse Transform: {inv_estimation}")
print(f"Acceptance-rejection method: {rejection_estimation}")
print(f"Real value: {real_value}")

#get_rel_frecuencies([X.reject_method() for _ in range(40000)], range(11))
#get_rel_frecuencies([X.inv_method() for _ in range(40000)], range(11))
# %%
# c)
def get_optimal_c(p, q):
    c = 1
    
    for px, qx in zip(p, q):
        c = max(c, px/qx)
        
    return c

def reject_method_gen(lam, a, b):
    lam = lam
    norm_const = exp(-lam)*sum(lam**j / factorial(j) for j in range(a, b+1))
    p = [exp(-lam)*lam**j / (factorial(j) * norm_const) for j in range(a, b+1)]
    c = get_optimal_c(p, X.p)

    y = X.reject_method()
    u = random()
    
    while (y-a not in range(0, len(p))) or u >=  p[y-a]/(X.p[y]*c):
        y = X.reject_method()
        u = random()
        
    return y

#get_rel_frecuencies([reject_method_gen(0.7, 5, 10) for _ in range(1000)], range(11))
# %%
