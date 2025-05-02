# %%
# Ejercicio 9
from numpy.random import rand
from numpy import log, sqrt, cos, sin, pi


# a)
def reject_normal(mu, sigma, size):
    
    for _ in range(size):
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
    r_squared = -2 * log(1-rand(size))
    os = 2 * pi * rand(size)
    
    xs = sqrt(r_squared) * cos(os)
    ys = sqrt(r_squared) * sin(os)
    
    return (xs * sigma + mu, ys * sigma + mu)

# c)