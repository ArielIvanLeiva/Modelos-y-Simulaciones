# %%
# Ejercicio 8
from numpy import mean
from numpy.random import randint
from itertools import product
from statutils.execution import update_mean

# a)
def variance_estimator(xs):
    n = len(xs)
    sample_mean = mean(xs)
    summation = 0
    
    for x in xs:
        summation += (x - sample_mean)**2
    
    estimation = summation/(n - 1)
    
    return estimation


def ideal_bootstrap_mean(estimator, xs):
    n = len(xs)
    summation = 0
    
    for bts_sample in product(xs, repeat=n):
        summation += estimator(bts_sample)

    estimation = summation/(n ** n)   
    
    return estimation
    

def ideal_bootstrap_variance(estimator, xs):
    n = len(xs)
    summation = 0
    
    estimator_e_mean = ideal_bootstrap_mean(estimator, xs)
    
    for bts_sample in product(xs, repeat=n):
        summation += (estimator(list(bts_sample)) - estimator_e_mean)**2

    estimation = summation/(n ** n)

    return estimation

# a)

var_estimation = ideal_bootstrap_variance(variance_estimator, [1, 3])
print(f"a) Bootstrap ideal variance estimation: {var_estimation}")
print(f"(for xs={[1,3]})\n")

# b)
def montecarlo_bootstrap_variance(estimator, xs, m):
    n = len(xs)
    summation = 0
    
    estimator_mean_estimation = 0

    for i in range(m):
        indexes = randint(0, n, size=n)
        bts_sample = [xs[i] for i in indexes]
        
        estimator_mean_estimation = update_mean(estimator_mean_estimation, estimator(bts_sample), i+1)
        summation += (estimator(list(bts_sample)) - estimator_mean_estimation)**2

    estimation = summation/(m-1)

    return estimation

xs = [5, 4, 9, 6, 21, 17, 11, 20, 7, 10, 21, 15, 13, 16, 8]
montecarlo_estimation = montecarlo_bootstrap_variance(variance_estimator, xs, 1000)
print(f"b) Montecarlo bootstrap estimation: {montecarlo_estimation}")
print(f"(for xs={xs})\n")
# %%
# Un poco de testing
xs = [1,2,3,2,5,7]
ideal_estimation = ideal_bootstrap_variance(variance_estimator, xs)
montecarlo_estimation = montecarlo_bootstrap_variance(variance_estimator, xs, 3000)
print("Testing:")
print(f"Ideal estimation for xs={xs}: {ideal_estimation}")
print(f"Montecarlo estimation for xs={xs}: {montecarlo_estimation}")