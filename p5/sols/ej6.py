# %%
# Ejercicio 6
from numpy.random import rand

def inv_sample(n, size):
    return rand(size)**(1/n)

def alt_sample(n, size):
    return [max(rand(n)) for _ in range(size)]

def reject_sample(n, size):
    samp = []
    
    for _ in range(size):
        u = rand()
        y = rand()
        
        while(u > y**(n-1)):
            u = rand()
            y = rand()
            
        samp.append(y)

    return samp

# %%
from timeit import timeit

n = 12
executions = 100000

inv_time = timeit(lambda: inv_sample(n, executions), number=10)/(executions*10)
alt_time = timeit(lambda: alt_sample(n, executions), number=10)/(executions*10)
reject_time = timeit(lambda: reject_sample(n, executions), number=10)/(executions*10)

# %%
print(f"inv time: {inv_time}")
print(f"alt time: {alt_time}")
print(f"reject time: {reject_time}")

# %%
# For testing

from matplotlib import pyplot as plt

inv_samp = inv_sample(n, executions)
alt_samp = alt_sample(n, executions)
reject_samp = reject_sample(n, executions)

plt.hist(inv_samp)
plt.hist(alt_samp)
plt.hist(reject_samp)