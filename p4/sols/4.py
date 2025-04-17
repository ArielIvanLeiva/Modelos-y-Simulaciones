# %%
# Ejercicio 4
from numpy.random import random
import timeit

p = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]

def rejection(c):
    y = int(10  * random() + 1)
    u = random()
    
    while u >= p[y-1]/(c * 0.1):
        y = int(10  * random() + 1)
        u = random()

    return y


class InverseTranform():
    def __init__(self, values, p):
        assert len(values) == len(p), "Mismatch between number of values and probabilities"
        assert sum(p) == 1, "Probabilities doesn't add up to one"

        self.dictionary = dict(sorted(zip(values, p), key=lambda x: x[1])[::-1])
        
        self.cummulative = {}
        summation = 0
        
        for x, px in self.dictionary.items():
            summation += px
            self.cummulative[x] = summation
        
    def p(self, x):
        return self.dictionary.get(x, 0)

    def sample(self):
        u = random()
        
        for x, sx in self.cummulative.items():
            if (u <= sx):
                return x

def get_rel_frecuencies(sample, keys=range(1, 10+1)):
    frecuencies = {i: 0 for i in keys}
    
    for x in sample:
        if x in frecuencies.keys():
            frecuencies[x] += 1
        
    return {i: value/len(sample) for i, value in frecuencies.items()}

# a) Rechazo óptimo (utilizando una uniforme discreta)
c = len(p)*max(p)
def optimal_rejection():
    return rejection(c)

print(get_rel_frecuencies([optimal_rejection() for _ in range(1000)]))

# %%

# b)
def dumb_rejection():
    return rejection(3)

print(get_rel_frecuencies([dumb_rejection() for _ in range(1000)]))

# %%
# c) Método de la tranformada inversa
Inversion = InverseTranform(range(1, 10+1), p)
print(get_rel_frecuencies([Inversion.sample() for _ in range(1000)]))

# d) Método de la urna
A = []
for i, prob in enumerate(p):
    A = A + [i+1 for _ in range(round(100*prob))]

def urn_sample():
    return A[int(100*random())]

# %%
# Comparación de eficiencia
num_of_executions = 1000000
print(f"Average time in {num_of_executions} executions:")

# NOTA: Seguramente el micro/ o el interprete de python 
# optimizan la ejecución de la segunda función que usa a rejection(), pues al cambiar el orden cambian ligeramente los resultados
dumb_rej_time = timeit.timeit(dumb_rejection, number=num_of_executions)/num_of_executions
optimal_rej_time = timeit.timeit(optimal_rejection, number=num_of_executions)/num_of_executions
inversion_time = timeit.timeit(Inversion.sample, number=num_of_executions)/num_of_executions
urn_time = timeit.timeit(urn_sample, number=num_of_executions)/num_of_executions

print(f"Optimal Rejection: {optimal_rej_time}")
print(f"Dumb Rejection (c = 3): {dumb_rej_time}")
print(f"Inverse Transform: {inversion_time}")
print(f"Urn: {urn_time}")