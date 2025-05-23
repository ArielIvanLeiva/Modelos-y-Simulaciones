# %%
# Ejercicio 1
from numpy.random import rand
from numpy import log, sqrt, cos, sin, pi
from statutils.execution import update_mean, update_scuad

def polar_normal(mu=0, sigma=1, size=1):
    r_squared = -2 * log(1 - rand(size))
    os = 2 * pi * rand(size)

    xs = sqrt(r_squared) * cos(os)
    ys = sqrt(r_squared) * sin(os)

    return (xs * sigma + mu, ys * sigma + mu)


# %%
def restricted_sample():
    squad = 0
    mean,_ = polar_normal()
    n = 1
    
    while n < 100 or (sqrt(squad/n) >= 0.1):
        n += 1
        
        x, _ = polar_normal()
        
        oldmean = mean
        mean = update_mean(mean, x, n)
        squad = update_scuad(squad, mean, oldmean, n)
    
    return n, mean, squad

sample = restricted_sample()
# %%
n, mean, squad = sample

# a)
print(f"n: {n}")

# b)
print(f"mean: {mean}")

# c)
print(f"squad: {squad}")