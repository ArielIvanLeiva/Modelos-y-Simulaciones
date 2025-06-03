# %%
# Ejercicio 9
from scipy.stats import expon
from numpy.random import uniform

# NOTE: No olvidar ordenar los datos
xs = sorted([1.6, 10.3, 3.5, 13.5, 18.4, 7.7, 24.3, 10.7, 8.4, 4.9, 7.9, 12, 16.2, 6.8, 14.7])
mean_estimation = sum(xs)/len(xs)
expected_expon = expon(loc=mean_estimation)

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
        
        sample_expon = expon(sample_mean_estimation)
        pvalue_count += int(ks_estimator(sample, sample_expon) >= d_ks)
   
    pvalue_estimation = pvalue_count/m

    return pvalue_estimation

d_ks = ks_estimator(xs, expected_expon)

print("Own estimation:")
print(f"Naive approach: statistic: {d_ks}, pvalue: {estimate_pvalue(xs, d_ks)}")
print(f"Better approach: statistic: {d_ks}, pvalue: {estimate_pvalue_better(xs, d_ks, expected_expon)}")

# Para usar scipy
# from scipy.stats import kstest
# kstest(xs, expected_expon.cdf)