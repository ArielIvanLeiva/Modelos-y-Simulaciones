# %%
# Ejercicio 7
from numpy.random import uniform
from scipy.stats import expon
from numpy import log

ys = sorted(
    -log(1-uniform(size=30))
)

def cummulative_prob(ys, x):
    i = 0
    
    while i < len(ys) and x >= ys[i]:
        i += 1

    if i < len(ys):
        return i/len(ys)
    else:
        return 1

def ks_estimator(ys):
    exp_rv = expon(scale=1)
    # NOTE: Este es el estimador para una variable exponencial con media 1
    max1 = max(j/len(ys) - exp_rv.cdf(ys[j-1]) for j in range(1, len(ys)+1))
    max2 = max(exp_rv.cdf(ys[j-1])-(j-1)/len(ys) for j in range(1, len(ys)+1))
    return max(max1, max2)

d_ks = ks_estimator(ys)

def estimate_pvalue(ys, t):
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
        
        if d_j >= t:
            pvalue_count += 1
    
    pvalue_estimation = pvalue_count/m
    
    return pvalue_estimation

print(f"pvalue estimation: {estimate_pvalue(ys, d_ks)}")
