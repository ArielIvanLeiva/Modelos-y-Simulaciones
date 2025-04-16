# Display utility function
# %%
from IPython.display import display, Math
def dp(text):
    display(Math(text))
# %%
# Ejercicio 2
from numpy.random import random
from numpy import exp
import sympy as sp
import timeit


# %%
# a)
N = 10000

def get_estimation(n=100):
    est = 0

    for _ in range(1, n+1):
        u = N*random()
        est += exp(u/N)
    
    return N*est/n
        

# %%
# b)

b_estimation = get_estimation(n=100)
print(f"b) Estimation: {b_estimation}")

# %%
# c)
k = sp.Symbol("k")
expr = sp.Sum(sp.exp(k/N),(k, 1, N))

dp(r"\text{Estimated value:}" + sp.latex(expr))

def get_real_value():
    summation = 0

    for i in range(1, N+1):
        summation += exp(i/N)
    
    return summation

def get_partial_sum(high=100):
    summation = 0
    
    for k in range(1, high+1):
        summation += exp(k/N)
    
    return summation

partial_sum = get_partial_sum(high=100)
real_value = get_real_value()

print(f"Estimation value: {b_estimation}")
print(f"Partial Sum value: {partial_sum}")
print(f"Real value: {real_value}")

number_of_executions = 100

b_estimation_time = timeit.timeit(lambda: get_estimation(), number=number_of_executions)/number_of_executions
real_value_time = timeit.timeit(lambda: get_real_value(), number=number_of_executions)/number_of_executions
partial_sum_time = timeit.timeit(lambda: get_partial_sum(), number=number_of_executions)/number_of_executions

print()
print(f"Average execution time Times (from a {number_of_executions} executions per function sample):")
print(f"Estimation Time: {b_estimation_time}")
print(f"Real value Time: {real_value_time}")
print(f"Partial sum Time: {partial_sum_time}")
print(f"Real Value Time/Estimation Time: {real_value_time/b_estimation_time}")