# %%
# Ejercicio 10
import math
from scipy.stats import norm
from numpy.random import uniform
from numpy import var


# NOTE: No olvidar ordenar los datos
xs = sorted([91.9, 97.8, 111.4, 122.3, 105.4, 95.0, 103.8, 99.6, 96.6, 119.3, 104.8, 101.7])
mean_estimation = sum(xs)/len(xs)
stdev_estimation = math.sqrt(var(xs))
expected_norm = norm(loc=mean_estimation, scale=stdev_estimation)

def ks_estimator(xs, variable):
    # # NOTE: Este estimador está construido para una variable de distribución "variable"
    n = len(xs)

    max1 = max(j / n - variable.cdf(xs[j - 1]) for j in range(1, n + 1))
    max2 = max(variable.cdf(xs[j - 1]) - (j - 1) / n for j in range(1, n + 1))
    return max(max1, max2)
    

def estimate_pvalue(ys, d_ks):
    pvalue_count = 0
    n = len(ys)
    m = 10000
    
    for _ in range(m):
        uniforms = uniform(0, 1, n)
        uniforms.sort()
       
        d_j = 0
        
        for j in range(n):
            u_j = uniforms[j]
            d_j = max(d_j, (j + 1)/n - u_j, u_j - j/n)
        
        if d_j >= d_ks:
            pvalue_count += 1
    
    pvalue_estimation = pvalue_count/m
    
    return pvalue_estimation

def estimate_pvalue_better(ys, d_ks, original_variable):
    pvalue_count = 0
    n = len(ys)
    m = 1000
    
    for _ in range(m):
        # NOTE: NO OLVIDAR ORDENAR
        sample = sorted(original_variable.rvs(n))
        sample_mean_estimation = sum(sample)/n
        sample_stdev_estimation = math.sqrt(var(sample))
        
        sample_norm = norm(sample_mean_estimation, sample_stdev_estimation)
        pvalue_count += int(ks_estimator(sample, sample_norm) >= d_ks)
   
    pvalue_estimation = pvalue_count/m
    
    return pvalue_estimation

d_ks = ks_estimator(xs, expected_norm)

print("Own estimation:")
print(f"Naive approach: statistic: {d_ks}, pvalue: {estimate_pvalue(xs, d_ks)}")
print(f"Better approach: statistic: {d_ks}, pvalue: {estimate_pvalue_better(xs, d_ks, expected_norm)}")
