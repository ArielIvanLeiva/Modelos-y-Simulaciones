# %%
# Ejercicio 4
from numpy.random import uniform
from scipy.stats import expon

ys = sorted(
    [86.0, 133.0, 75.0, 22.0, 11.0, 144.0, 78.0, 122.0, 8.0, 146.0, 33.0, 41.0, 99.0]
)

def ks_estimator(ys):
    exp_rv = expon(scale=50)
    # NOTE: Este es el estimador para una variable exponencial con media 50
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

# %%
# Testeando la consistencia del test
from statutils.analysis import probability_of

def get_expon_pvalues(m):
    l = []
    for _ in range(m):
        ys = sorted(expon(scale=50).rvs(13))
        d_ks = ks_estimator(ys)
        l.append(estimate_pvalue(ys, d_ks))

    return l

print(f"Consistency test result: {probability_of(get_expon_pvalues(100), lambda x: x < 0.05)}")
print("Expected: arround 0.05")
# %%
