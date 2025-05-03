# %%
# Ejercicio 9
from numpy.random import rand
from numpy import exp, log, sqrt, cos, sin, pi, mean, std
from statsUtils import get_samples


# a)
def reject_normal(mu, sigma):
    while True:
        y2 = -log(1 - rand())
        y = -log(1 - rand())

        if y2 >= (y - 1) ** 2 / 2:
            if rand() < 0.5:
                return y * sigma + mu
            else:
                return -y * sigma + mu


# b)
def polar_normal(mu, sigma, size):
    r_squared = -2 * log(1 - rand(size))
    os = 2 * pi * rand(size)

    xs = sqrt(r_squared) * cos(os)
    ys = sqrt(r_squared) * sin(os)

    return (xs * sigma + mu, ys * sigma + mu)


# c)
C = 4 * exp(-0.5) / sqrt(2.0)

def rate_normal(mu, sigma):
    while True:
        u1 = rand()
        u2 = 1 - rand()
        z = C * (u1 - 0.5) / u2
        zz = z * z / 4

        if zz <= -log(u2):
            return mu + z * sigma


# %%
# Setting up parameters
n = 100000
mu = 3
sigma = 5

reject_f = lambda size: [reject_normal(mu, sigma) for _ in range(size)]
rate_f = lambda size: [rate_normal(mu, sigma) for _ in range(size)]
polar_f = lambda size: polar_normal(mu, sigma, size)

fs = [
    reject_f, polar_f, rate_f
]

# Running simulation
reject_samp, polar_samp, rate_samp = get_samples(fs, n)

X_sample, Y_sample = polar_samp

# %%
# Results
print(f"reject mean estimation: {mean(reject_samp)}")
print(f"polar mean estimation: {mean(polar_samp)}")
print(f"rate mean estimation: {mean(rate_samp)}")
print(f"Real mean: {mu}")
print()
print(f"reject stdev estimation: {std(reject_samp)}")
print(f"polar stdev estimation: {std(polar_samp)}")
print(f"rate stdev estimation: {std(rate_samp)}")
print(f"Real stdev: {sigma}")

# %%
# Simple testing cell
import matplotlib.pyplot as plt

plt.hist(reject_samp, bins=100)
plt.hist(rate_samp, bins=100)
plt.hist(X_sample, bins=100)