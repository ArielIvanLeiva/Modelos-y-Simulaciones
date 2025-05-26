# %%
# Ejercicio 1
from scipy.stats import chi2, binom

# a)
Nd = {"blancas": 141, "rosas": 291, "rojas": 132}
pd = {"blancas": 1/4, "rosas": 1/2, "rojas": 1/4}

def pearson_estimator(Ns, ps):
    # NOTE: Se asume que lo que se recibe son los valores ordenados por "tipo"
    
    n = sum(Ns)
    return sum((N-n*p)**2/(n*p) for N, p in zip(Ns, ps))

t = pearson_estimator(Nd.values(), pd.values())

pvalue = 1-chi2(df=len(Nd)-1).cdf(t)

print(f"Pearson test p-value: {pvalue}")

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

print(f"b) Estimación del p-valor: {pvalue_estimation(Nd.values(), pd.values(), 1000, t)}")

# %%
# b) Versión optimizada (usando la distribución multinomial)

from scipy.stats import multinomial
from statutils.analysis import probability_of

def pvalue_estimation(Ns, ps, m, t):
    n = sum(Ns)
    
    samples = multinomial(n, list(pd.values())).rvs(m)

    return probability_of(samples, lambda Ms: pearson_estimator(Ms, ps) >= t)

print(f"b) Estimación del p-valor (optimizada): {pvalue_estimation(Nd.values(), pd.values(), 1000, t)}")