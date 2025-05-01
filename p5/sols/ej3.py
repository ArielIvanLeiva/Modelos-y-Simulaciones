# %%
# Ejercicio 3
from numpy import log, mean
from numpy.random import rand


class Exponential:
    def __init__(self, lam):
        self.lam = lam

    def sample(self):
        return -log(1 - rand()) / self.lam


# a)
class Mix:
    def __init__(self, ps: list, Xs: list):
        self.ps = ps.copy()
        self.Xs = Xs.copy()
        self.ordered_vas = sorted(zip(ps, Xs), key=lambda x: x[0])[::-1]

    def sample(self):
        cum = 0
        u = rand()

        for p, X in self.ordered_vas:
            cum += p
            if u <= cum:
                return X.sample()


# b)
X1 = Exponential(1 / 3)
X2 = Exponential(1 / 5)
X3 = Exponential(1 / 7)

X = Mix([0.5, 0.3, 0.2], [X1, X2, X3])

k = 10000
samp = [X.sample() for _ in range(k)]

print("Real mean: 4.4")
print(f"Estimation over {k} simulations {mean(samp)}")
