# %%
# Ejercicio 5
from scipy.stats import chi2, binom
from numpy import mean
from statutils.analysis import get_frecuencies

xs = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
Ns = list(get_frecuencies(xs, keys=range(8+1)).values())

p_estimation = mean(xs)/8
b = binom(n=8, p = p_estimation)
ps = [b.pmf(i) for i in range(8+1)]


def pearson_estimator(Ns, ps):
    # NOTE: Se asume que lo que se recibe son los valores ordenados por "tipo"
    
    n = sum(Ns)

    return sum((N-n*p)**2/(n*p) for N, p in zip(Ns, ps))

t = pearson_estimator(Ns, ps)

# NOTE: Se le resta 1 dos veces pues hay un parámetro desconocido
pvalue = 1-chi2(df=len(Ns) - 1 - 1).cdf(t)

print(f"Chi-squared p-value (NOTE: the sample is small, only 18 elements): {pvalue}")

# %%

def pvalue_estimation(p_estimation, Ns, m, t):
    num_of_greater = 0
    original_b = binom(n=8, p=p_estimation)
    
    for _ in range(m):
        sample = original_b.rvs(sum(Ns))

        # NOTE: El 8 proviene de la cantidad de valores que la binomial puede tomar
        sample_Ns = list(get_frecuencies(sample, range(8+1)).values())
        sample_p_estimation = mean(sample)/8
        sample_b = binom(n=8, p=sample_p_estimation)
        sample_ps = [sample_b.pmf(i) for i in range(8+1)]

        t0 = pearson_estimator(sample_Ns, sample_ps)
        num_of_greater += int(t0 >= t)
    
    return num_of_greater/m

print(f"b) p-value estimation: {pvalue_estimation(p_estimation, Ns, 1000, t)}")
