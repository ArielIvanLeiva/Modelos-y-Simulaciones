# %%
# Ejercicio 3
from numpy.random import uniform

ys = sorted([0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74])

def ks_estimator(ys):
    # NOTE: Este es el estimador para la uniforme en el [0, 1]
    max1 = max(j/len(ys) - ys[j-1] for j in range(1, len(ys)+1))
    max2 = max(ys[j-1]-(j-1)/len(ys) for j in range(1, len(ys)+1))
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
def get_uniform_pvalues(m):
    l = []
    for _ in range(m):
        ys = sorted(uniform(0, 1, 10))
        d_ks = ks_estimator(ys)
        l.append(estimate_pvalue(ys, d_ks))

    return l

from statutils.analysis import probability_of
print(f"Consistency test result: {probability_of(get_uniform_pvalues(100), lambda x: x < 0.05)}")
print("Expected: arround 0.05")
# %%
