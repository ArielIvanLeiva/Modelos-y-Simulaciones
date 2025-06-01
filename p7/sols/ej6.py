# %%
# Ejercicio 6
import pandas as pd
from scipy.stats import chi2, multinomial

Ns = [188, 138, 87, 65, 48, 32, 30, 34, 13, 2]
ps = [0.31, 0.22, 0.12, 0.10, 0.08, 0.06, 0.04, 0.04, 0.02, 0.01]

# a)
data = pd.DataFrame(zip(Ns, ps), columns=["Frecuencies", "Area"], index=range(1, 10 + 1))

# b) Considerando a X como la v.a. que representa los resultados de girar la rueda,
# H0: P(X = i) = ps[i]

# c)
# Si T es el estimador de Pearson,
# pvalor = P(T >= t)

# d)
def pearson_estimator(Ns, ps):
    # NOTE: Se asume que lo que se recibe son los valores ordenados por "tipo"
    n = sum(Ns)
    
    return sum((N - n*p)**2/(n*p) for N, p in zip(Ns, ps))

t = pearson_estimator(Ns, ps)
pvalue = 1 - chi2(df=len(Ns)-1).cdf(t)

print(f"d) Chi-squared p-value: {pvalue}")

# e)
def estimate_pvalue(Ns, ps, m, t):
    assertions = 0
    mul = multinomial(p=ps, n=sum(Ns))
    
    for _ in range(m):
        Ms = mul.rvs()[0]

        t0 = pearson_estimator(Ms, ps)
        assertions += int(t0 >= t)
    
    return assertions/m

print(f"e) p-value estimation: {estimate_pvalue(Ns, ps, 1000, t)}")