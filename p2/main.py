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
# Ejercicio 8

# a)
# Parámetro del processo de Poisson homogéneo: 3 * 1/minutos
lamb = 3

for s in [5, 10, 20, 30]:
    # Como s está en segundos y lamb en minutos, convertimos s a minutos. mu es el parámetro de N(t) como v.a.
    prob = poisson.cdf(1, mu=(lamb * s/60))
    print(f"La probabilidad de que salga ileso si tarda {s} segundos es: {prob}")

# %%

# b)
# Parámetro del processo de Poisson homogéneo: 3 * 1/minutos
lamb = 3
s1 = 5

for s in [10, 20, 30]:
    # Como s está en segundos y lamb en minutos, convertimos s a minutos. mu es el parámetro de N(t) como v.a.
    prob = poisson.pmf(0, mu=(lamb * (s-s1)/60))
    print(f"La probabilidad de que salga ileso si tarda {s} segundos es: {prob}")

# %%
from scipy.stats import poisson

# Ejercicio 10

# Variables aleatorias asociadas a los procesos de los autos, colectivos y motos respectivamente.
NA = lambda t: poisson(t * 1/5) # 1/(5 minutos)
NC = lambda t: poisson(t * 1/10) # 1/(10 minutos)
NM = lambda t: poisson(t * 1/30) # 1/(30 minutos)

# a)
# Probablidad de que en los primeros 20 min hayan llegado 2 autos, 0 colectivos y 1 moto
NA(20).pmf(2)*NC(20).pmf(0)*NM(20).pmf(1)

# b)
# Proceso asociado al conteo de la cantidad de vehículos que poseen cambio en un tiempo t
N2 = lambda t: poisson(t * (1/5 + 1/10 + 1/30) * (1/4))

# Probabilidad de que ningún vehículo tenga cambio en los primeros 10 minutos
N2(10).pmf(0)