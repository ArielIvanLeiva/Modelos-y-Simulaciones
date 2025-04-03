# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: 3.12.7
#     language: python
#     name: python3
# ---

# %%
# Ejercicio 1

def nthNums(suc_fun, seed, n):
    x = seed
    nums = [x]

    for i in range(n):
        x = suc_fun(x)
        nums.append(x)

    return nums


# %%
def suc(x):
    return ((x * x) % 1000000) // 100


def nthVon(seed, n):
    return nthNums(suc, seed, n)


# a)
seeds = [3792, 1004, 2100, 1234]

secuences = [nthVon(seed, 10) for seed in seeds]
secuences


# %%
# b)
def suc_gen(a, c, m, x):
    return (a * x + c) % m

def calc_period(secuence):
    first = secuence[0]
    period = 0

    for i, x in enumerate(secuence[1:]):
        if x == first:
            period = i
            break

    return period

a = 5
c = 31
m = 2**5

def suc_y(x):
    return suc_gen(a, c, m, x)


seed = 4
secuence_x = nthNums(suc_y, seed, 1024)
period = calc_period(secuence_x)

print(f"b) {a}y+{c} mod {m} period: {period}")

# Generador multiplicativo
a = 12
c = 0
m = 31

for p in [2, 3, 5]:
    num = (p, a ** (30/p) % m)
    print(num)
    assert a ** (30/p) % m != 1

def suc_x(x):
    return suc_gen(a, c, m, x)

secuence_y = nthNums(suc_x, seed, 1024)
period = calc_period(secuence_y)

print(f"b) {a}y mod {m} period: {period}")

# Suma de generadores
import numpy as np
secuence_z = (np.array(secuence_x) + np.array(secuence_y))%(2**5)

period = calc_period(secuence_z)

print(f"Sum period: {period}")

# Ploteo
import matplotlib.pyplot as plt

fig, axs = plt.subplots(3)
axs[0].plot(secuence_x[:-1], secuence_x[1:], 'o', color='red')
axs[1].plot(secuence_y[:-1], secuence_y[1:], 'o', color='blue')
axs[2].plot(secuence_z[:-1], secuence_z[1:], 'o', color='yellow')

plt.show()

# c)
# Hecho en papel :)

# %%
# d)
import numpy as np

def is_inside(point, m):
    return sum((coord-m/2)**2 for coord in point) < (m/10)**2

# Randu

m_randu = 2**31

def randu(x):
    return suc_gen(2**16 + 3, 0, m_randu, x)
    #return randint(0,m_randu)

u1 = randu(123123)

def randu_3d_sample(n, seed=u1):
    return np.array(nthNums(randu, seed, n))
    
k = 2**17*3-1
randu_points = randu_3d_sample(k).reshape((-1,3))
randu_estimation = sum(1 for p in randu_points if is_inside(p, m_randu))/len(randu_points)

print(f"Estimated (randu): {randu_estimation}")

# Alternative
a = 7**5
m = 2**31-1

def suc(x):
    return suc_gen(a, 0, m, x)

alt_points = np.array(nthNums(suc, seed, k)).reshape((-1, 3))
alt_estimation = sum(1 for p in alt_points if is_inside(p, m))/len(alt_points)

# El valor resultante de la alternativa es más cercano al real
print(f"Estimated (alternative): {alt_estimation}")

print(f'"Real": {(4/3) * np.pi * (1/10)**3}')


# %%
# Ejercicio 2
from numpy.random import rand

# b)
ns = [100, 1000, 10000, 100000, 1000000]
estimations = []
for n in ns:
    success = 0
    u = rand(n)
    for num in u:
        if num < 1 / 2:
            x = rand() + rand()
        else:
            x = rand() + rand() + rand()
        success += x >= 1

    estimations.append(success / n)

estimations

# %%
# Ejercicio 3
from numpy.random import rand

# b)
ns = [100, 1000, 10000, 100000, 1000000]
estimations = []
for n in ns:
    success = 0
    u = rand(n)
    for num in u:
        if num < 1 / 3:
            x = rand() + rand()
        else:
            x = rand() + rand() + rand()
        success += x <= 2

    estimations.append(success / n)

estimations

# %%
# Ejercicio 4
import numpy as np
from numpy.random import rand
from numpy import log, exp


# Para simular las v.a. exponenciales:
class Exponential:
    def __init__(self, lamb):
        self.lamb = lamb

    def pdf(self, x):
        return self.lamb * exp(-self.lamb * x)

    def cdf(self, x):
        return 1 - exp(-self.lamb * x)

    def inversecdf(self, y):
        return -log(1 - y) / self.lamb

    def sample(self, size=1):
        uniform = rand() if size == 1 else rand(size)
        return self.inversecdf(uniform)


# v.a's. asociadas al tiempo de espera en cada caja.
X1 = Exponential(1 / 3)
X2 = Exponential(1 / 4)
X3 = Exponential(1 / 5)


class WaitingTime:
    def sample(self, size, return_ids=False):
        samp = []
        ids = []

        for _ in range(size):
            X, id = self.desition()
            samp.append(X.sample())
            ids.append(id)

        if return_ids:
            return (samp[0], ids[0]) if size == 1 else (np.array(samp), np.array(ids))
        else:
            return samp[0] if size == 1 else np.array(samp)

    def desition(self) -> Exponential:
        """
        Returns the random variable associated with the lane desition of a random client.
        """

        x = rand()

        if 0 <= x < 0.40:
            return (X1, 1)
        elif 0.40 <= x < 0.72:
            return (X2, 2)
        elif 0.72 <= x < 1:
            return (X3, 3)


# %%
# Probabilidades "exacta":
# a) P(T < 4 minutos)
a_prob = X1.cdf(4) * 0.4 + X2.cdf(4) * 0.32 + X3.cdf(4) * 0.28
print(f"P(T < 4 minutos) = {a_prob}")

# b) P(Vaya a caja i | T > 4 minutos)
b_prob = [
    (1 - X.cdf(4)) * sel_prob / (1 - a_prob)
    for X, sel_prob in zip([X1, X2, X3], [0.4, 0.32, 0.28])
]
print(f"P(Vaya a caja i | T > 4 minutos) = {b_prob}")

# Ap4oximaciones via simulación (c)):

# a)
T = WaitingTime()
sample = T.sample(1000)
a_est = sum(1 for num in sample if num < 4) / len(sample)

print(f"\nP(T < 4 minutos) ~ {a_est}")

# b)
# Creo primero una muestra considerable de casos en los que T > 4 minutos
big_sample, ids = T.sample(int(1000 / (1 - a_prob)), return_ids=True)
sample = [(t, id) for t, id in zip(big_sample, ids) if t > 4]

b_est = []

for i in [1, 2, 3]:
    estimation = sum(1 for t, id in sample if id == i) / len(sample)
    b_est.append(estimation)

print(f"P(Vaya a caja i | T > 4 minutos) ~ {b_est}")

# %%
# Ejercicio 5

import inspect
from numpy.random import uniform
from numpy import log
from statistics import mean
import pandas as pd
import sympy as sp
from IPython.display import display, Math

ns = [100, 1000, 10000, 100000, 1000000]
df = pd.DataFrame(index=ns, columns=[f"({l})" for l in list("abcdef")])


def get_est(f, sizes):
    parameter_size = len(inspect.signature(f).parameters)
    monte_estimations = []
    for n in sizes:
        inputs = [uniform(size=n) for _ in range(parameter_size)]
        monte_est = mean(f(*inputs))
        monte_estimations.append(monte_est)

    return monte_estimations[0] if len(sizes) == 1 else monte_estimations

def print_equality(I, y):
    latex_str = r"{} = {} \sim {}".format(sp.latex(I), sp.latex(y), sp.latex(I.doit().evalf()))
    display(Math(latex_str))


x = sp.symbols("x")
y = sp.symbols("y")

# a)
fexpr = (1 - x**2) ** (3 / 2)
f = sp.lambdify(x, fexpr)
I = sp.Integral(fexpr, (x, 0, 1))

print("a)")
print_equality(I, 3 * sp.pi / 16)

df["(a)"] = get_est(f, ns)

# b)
fexpr = x / (x**2 - 1)
I = sp.Integral(fexpr, (x, 2, 3))
f = sp.lambdify(x, fexpr.subs(x, x + 2))

print("b)")
print_equality(I, sp.ln(sp.Rational(8, 3)) / 2)

df["(b)"] = get_est(f, ns)

# c)
fexpr = x / ((1 + x**2) ** 2)
I = sp.Integral(fexpr, (x, 0, sp.oo))
f = sp.lambdify(x, fexpr.subs(x, 1 / x - 1) / (x**2))

print("c)")
print_equality(I, sp.Rational(1, 2))

df["(c)"] = get_est(f, ns)

# d)
fexpr = sp.exp(-(x**2))
I = sp.Integral(fexpr, (x, -sp.oo, sp.oo))
f = sp.lambdify(x, fexpr.subs(x, -sp.ln(1 / x - 1)) / (x * (1 - x))) 

print("d)")
print_equality(I, sp.sqrt(sp.pi))

df["(d)"] = get_est(f, ns)
df

# e)
fexpr = sp.exp((x + y)**2)
I = sp.Integral(fexpr, (x, 0, 1), (y, 0, 1))
f = sp.lambdify((x, y), fexpr) 

print("e)")
print_equality(I, I.doit())

df["(e)"] = get_est(f, ns)

# f)
def lt(y, x):
    return y < x

fexpr = sp.exp(-(x + y))
I = sp.Integral(fexpr, (y, 0, x), (x, 0, sp.oo))

adjusted_fexpr = (fexpr * sp.Piecewise((1, lt(y, x)), (0, True)))
adjusted_fexpr = adjusted_fexpr.subs({x: (1/x)-1, y: (1/y)-1}) / (x**2 * y**2)
f = sp.lambdify((x, y), adjusted_fexpr)

print("f)")
print_equality(I, I.doit())

df["(f)"] = get_est(f, ns)

df

# %%
# Ejercicio 6


# %%
# Ejercicio 7

from numpy.random import uniform
from statistics import mean


def N_sample(size):
    samp = []
    
    for _ in range(size):
        i = 0
        usum = 0
        
        while usum <= 1:
            i += 1
            usum += uniform()
        
        samp.append(i)
        
    return samp

# a)
ns = [100, 1000, 10000, 100000, 1000000]

df = pd.DataFrame(index=ns, columns=["E[N]"])
df["E[N]"] = [mean(N_sample(n)) for n in ns]
df = df.T

print(df)

# %%
# Ejercicio 8

from numpy import exp
from numpy.random import uniform
from statistics import mean
import pandas as pd

def N_sample(size):
    samp = []
    em3 = exp(-3)
    
    for _ in range(size):
        i = 0
        uprod = 1
        
        while uprod >= em3:
            uprod *= uniform()
            if uprod >= em3:
                i += 1
        
        samp.append(i)
        
    return samp

def get_rel_frecuencies(sample):
    frecuencies = {i: 0 for i in range(0, 7)}
    
    for x in sample:
        if x in frecuencies.keys():
            frecuencies[x] += 1
        
    return {i: value/len(sample) for i, value in frecuencies.items()}
#%%
# a)
ns = [100, 1000, 10000, 100000, 1000000]

df = pd.DataFrame(index=ns, columns=["E[N]"])
df["E[N]"] = [mean(N_sample(n)) for n in ns]
df = df.T

print(df)

# %%
# b)
n = 1000000

sample = N_sample(n)
estimations = get_rel_frecuencies(sample)

df = pd.DataFrame.from_dict(estimations, orient='index', columns=["P(N = i)"])

print(df)

# %%
# Ejercicio 9

from numpy.random import uniform
from math import ceil

class DiscreteUniform():
    """
    Clase que representa a una variable aleatoria distribuida de manera uniforme en el intervalo DISCRETO cerrado [a,b].
    """
    def __init__(self, a, b):
        assert type(a) == int
        assert type(b) == int
        
        self.a = a
        self.b = b
    
    def sample(self, size=1):
        samp = [ceil((self.b - (self.a - 1)) * uniform() + self.a - 1) for _ in range(size)]
        return samp[0] if size == 1 else samp

D1 = DiscreteUniform(1,6)
D2 = DiscreteUniform(1,6)
X1 = DiscreteUniform(1,6)
X2 = DiscreteUniform(1,6)

# a)
import itertools

combs = itertools.product(range(1,7), repeat=4)
k = len(list(combs))
combs = itertools.product(range(1,7), repeat=4)
success = 0
for comb in combs:
    d1 = comb[0]
    d2 = comb[1]
    x1 = comb[2]
    x2 = comb[3]

    if d1 == 1 or d1 == 6:
        score = 2 * d2
    else:
        score = x1 + x2

    success += score > 6

print(success/k)

res = 10/18

# %%
# b)
ns = [100000]
estimations = []

for n in ns:
    success = 0
    d1 = D1.sample(n)
    for num in d1:
        if num == 1 or num == 6:
            score = 2 * D2.sample()
        else:
            score = X1.sample() + X2.sample()
        success += score > 6

    estimations.append(success / n)

estimations
