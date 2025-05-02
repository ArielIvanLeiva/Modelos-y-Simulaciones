# %%
# Ejercicio 7
from numpy.random import rand
from numpy import e, exp, mean, log
from statsUtils import get_samples, get_execution_times, probability_of

def inv_sample(size):
    return exp(rand(size))

def reject_sample(size):
    samp = []
    
    for _ in range(size):
        u = rand()
        y = (e-1)*rand()+1
        
        while(u > 1/y):
            u = rand()
            y = (e-1)*rand()+1
        
        samp.append(y)
        
    return samp

# %%
num_of_executions = 10000

inv_samp, reject_samp = get_samples([inv_sample, reject_sample], size=num_of_executions)
inv_time, reject_time = get_execution_times([inv_sample, reject_sample], size=num_of_executions)

# %%
# b)
print(f"inv average time: {inv_time}")
print(f"reject average time: {reject_time}")
print()
print(f"inv mean estimation: {mean(inv_samp)}")
print(f"reject mean estimation: {mean(reject_samp)}")
print(f"Real mean value: {e-1}")

# %%
# c)
print(f"inv P(X <= 2) estimation: {probability_of(inv_samp, lambda x: x <= 2)}")
print(f"reject P(X <= 2) estimation: {probability_of(reject_samp, lambda x: x <= 2)}")
print(f"Real P(X <= 2) value: {log(2)}")