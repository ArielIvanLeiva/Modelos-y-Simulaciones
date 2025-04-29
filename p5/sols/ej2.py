# %%
# Ejercicio 2
from numpy import vectorize, log, prod, array, mean
from math import gamma
from numpy.random import rand

# %%
# a)
# i)
class Pareto:
    def __init__(self, a):
        assert a > 0, f"a received value is less or equal than zero: a = {a}"
        self.a = a
        self.inverse_cdf = vectorize(self.inverse_cdf)

    def sample(self, size):
        return self.inverse_cdf(rand(size))

    def inverse_cdf(self, y):
        assert 0 <= y <= 1
        return (1 - y) ** (-1 / self.a)

    def mean(self):
        assert a > 1, "Pareto dist mean with a <= 1 diverges."
        return self.a/(self.a - 1)

    def __str__(self):
        return f"Pareto(a={self.a})"


# ii)
class Erlang:
    def __init__(self, mu, k):
        assert mu > 0, f"mu received value is less or equal than zero: mu = {mu}"
        assert k > 0 and isinstance(
            k, int
        ), f"k must be a positive integer, but k = {k}"

        self.mu = mu
        self.k = k

        self.sample = vectorize(self.sample)

    def sample(self, size):
        mu = self.mu
        k = self.k
        samp = []

        for _ in range(size):
            u_prod = prod(1 - rand(k))
            samp.append(-mu * log(u_prod))

        return array(samp)

    def mean(self):
        return self.k*self.mu
    
    def __str__(self):
        return f"Erlang(mu={self.mu}, k={self.k})"
    


# iii)
class Weibull:
    def __init__(self, lam, beta):
        assert lam > 0, f"lam received value is less or equal than zero: lam = {lam}"
        assert (
            beta > 0
        ), f"beta received value is less or equal than zero: beta = {beta}"

        self.lam = lam
        self.beta = beta

        self.inverse_cdf = vectorize(self.inverse_cdf)

    def sample(self, size):
        return self.inverse_cdf(rand(size))

    def inverse_cdf(self, y):
        return (-log(1 - y) * self.lam) ** (1 / self.beta)

    def mean(self):
        return self.lam * gamma(1 + 1/self.beta)
    
    def __str__(self):
        return f"Weibull(lam={self.lam}, beta={self.beta})"


# %%
# b)

a = 2
mu = 2
k = 2
lam = 1
beta = 2
P = Pareto(a)
E = Erlang(mu, k)
W = Weibull(lam, beta)

vas = [P, E, W]
n = 10000

for X in vas:
    print(f"Estimated mean of {X}: {mean(X.sample(n))}")
    print(f"Real value: {X.mean()}\n")
