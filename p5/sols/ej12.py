# %%
# Ejercicio 12
from numpy.random import rand
from numpy import log


class Poisson:
    def __init__(self, lam):
        self.lam = lam

    def sample(self, t):
        arrivals = []
        
        time_past = 0
        events = 0
        while time_past <= t:
            x = self.exp_sample()
            time_past += x

            if time_past > t:
                break

            events += 1
            arrivals.append((events, time_past))

        return (events, arrivals)

    def exp_sample(self):
        return -log(1 - rand()) / self.lam

P = Poisson(3)
P.sample(3)

# %%
# For testing purposes
from statutils.analysis import probability_of

t = 0.3
n = 100000
samp = [P.sample(t)[0] for _ in range(n)]

probability_of(samp, lambda x: x > 1)