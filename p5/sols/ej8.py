# %%
# Ejercicio 8
from numpy.random import rand
from numpy import sqrt, array, mean
from statutils.execution import get_samples, get_execution_times
from statutils.analysis import probability_of

def f(x):
    if 0 <= x < 1:
        return x
    elif 1 <= x < 2:
        return 2-x
    else:
        return 0

# b)
# i)
def naive_sample(size):
    return rand(size) + rand(size)

# ii)
def inv_sample(size):
    samp = []
    
    for _ in range(size):
        u = rand()

        if (u <= 1/2):
            samp.append(sqrt(2*u))
        else:
            samp.append(2-sqrt(2*(1-u)))
            
    return array(samp)

# iii)
def reject_sample(size):
    samp = []
    
    for _ in range(size):
        u = rand()
        y = 2*rand()
        
        while(u > f(y)):
            u = rand()
            y = 2*rand()
        
        samp.append(y)
        
    return samp

# c)
# %%
size = 10000

naive_samp, inv_samp, reject_samp = get_samples([naive_sample, inv_sample, reject_sample], size)
naive_time, inv_time, reject_time = get_execution_times([naive_sample, inv_sample, reject_sample], size)

# %%
print(f"naive average time: {naive_time*1000:.4f}ms")
print(f"inv average time: {inv_time*1000:.4f}ms")
print(f"reject average time: {reject_time*1000:.4f}ms")
print()
print(f"naive mean estimation: {mean(naive_samp)}")
print(f"inv mean estimation: {mean(inv_samp)}")
print(f"reject mean estimation: {mean(reject_samp)}")
print()

# %%
# d)
print(f"naive P(X > 1.5) estimation: {probability_of(naive_samp, lambda x: x > 1.5)}")
print(f"inv P(X > 1.5) estimation: {probability_of(inv_samp, lambda x: x > 1.5)}")
print(f"reject P(X > 1.5) estimation: {probability_of(reject_samp, lambda x: x > 1.5)}")
print("P(X > 1.5) = 0.125")