# %%
# Ejercicio 7
from scipy.stats import poisson

# a)
# Parámetro del processo de Poisson homogéneo: 3 * 1/minutos
lamb = 3

for s in [2, 5, 10, 20]:
    # Como s está en segundos y lamb en minutos, convertimos s a minutos. mu es el parámetro de N(t) como v.a.
    prob = poisson.pmf(0, mu=(lamb * s/60))
    print(f"La probabilidad de que salga ileso si tarda {s} segundos es: {prob}")

#%%
# b)
# Parámetro del processo de Poisson homogéneo: 3 * 1/minutos
lamb = 3

for s in [2, 5, 10, 20]:
    # Ahora el cada v.a. del subproceso distribuye Poisson con parámetro lambda*0.8*t
    prob = poisson.pmf(0, mu=(lamb * 0.8 * s/60))
    print(f"La probabilidad de que salga ileso si tarda {s} segundos y hay 80% de chances de que si pasa un auto mientras cruza lo atropelle es: {prob}")


# %%

