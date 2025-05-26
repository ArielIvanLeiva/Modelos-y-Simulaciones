# %%
# Ejercicio 2
from scipy.stats import chi2, binom

# a)
Ns = [158, 172, 164, 181, 160, 165]
ps = [1/6 for _ in range(6)]

def pearson_estimator(Ns, ps):
    # NOTE: Se asume que lo que se recibe son los valores ordenados por "tipo"
    
    n = sum(Ns)
    return sum((N-n*p)**2/(n*p) for N, p in zip(Ns, ps))

t = pearson_estimator(Ns, ps)

pvalue = 1-chi2(df=len(Ns)-1).cdf(t)

print(f"Chi-squared p-value: {pvalue}")

# %%
# b)

def pvalue_estimation(Ns, ps, m, t):
    num_of_greater = 0
    n = sum(Ns)
    
    for _ in range(m):
        Ms = []
        remaining_n = n
        cummulated_p = 0
        
        for p in ps:
            # NOTE: Sé que esto se podría optimizar para que no se evalúe la última binomial
            sample = binom(remaining_n, p/(1 - cummulated_p)).rvs()
            Ms.append(sample)

            remaining_n -= sample
            cummulated_p += p

        t0 = pearson_estimator(Ms, ps)
        num_of_greater += int(t0 >= t)
    
    return num_of_greater/m

print(f"b) p-value estimation: {pvalue_estimation(Ns, ps, 1000, t)}")

# %%
# b) Versión optimizada (usando la distribución multinomial)

from scipy.stats import multinomial
from statutils.analysis import probability_of

def pvalue_estimation(Ns, ps, m, t):
    n = sum(Ns)
    
    samples = multinomial(n, list(ps)).rvs(m)

    return probability_of(samples, lambda Ms: pearson_estimator(Ms, ps) >= t)

print(f"b) p-value estimation (optimized): {pvalue_estimation(Ns, ps, 1000, t)}")
