# %%
# Ejercicio 8
import math
import random
from numpy.random import uniform
import pandas as pd

def rt(df):
    x = random.gauss(0.0, 1.0)
    y = 2.0 * random.gammavariate(0.5 * df, 2.0)

    return x / (math.sqrt(y / df))


def normal_cdf(x):
    return math.erf(x / math.sqrt(2)) / 2 + 0.5

ns = [10, 20, 100, 1000]

# NOTE: No olvidar ordenar los datos
samples = {n: sorted([rt(11) for _ in range(n)]) for n in ns}


def ks_estimator(xs):
    # # NOTE: Este estimador está construido para una suposición de distribución normal estándard
    n = len(xs)

    max1 = max(j / n - normal_cdf(xs[j - 1]) for j in range(1, n + 1))
    max2 = max(normal_cdf(xs[j - 1]) - (j - 1) / n for j in range(1, n + 1))
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

data = pd.DataFrame(columns=["Statistic", "pvalue"])

for n, xs in samples.items():
    d_ks = ks_estimator(samples[n])
    pvalue_estimation = estimate_pvalue(xs, d_ks)
    data.loc[len(data)] = [d_ks, pvalue_estimation]

print("Own estimation:")
print(data)
# %%
from scipy.stats import kstest, norm

scipy_data = pd.DataFrame(columns=["Statistic", "pvalue"])

# Comparando resultados con los de scipy
print("Scipy estimation:")
for n, xs in samples.items():
    test = kstest(xs, norm().cdf)
    scipy_data.loc[len(scipy_data)] = [test.statistic, test.pvalue]

print(scipy_data)