# %%
# Ejercicio 7
from numpy.random import randint
from numpy import mean

xs = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69]
a, b = -5, 5

def estimator(sample):
    return mean(sample) - mean(xs)

# Dejo esto como implementación ineficiente de randint
# def randint(a, b, size):
#     l = []
    
#     for _ in range(size):
#         l.append(int((b-a)*random()) + a)
        
#     return l

def bootstrap_estimation(m=5000):
    estimation = 0

    for _ in range(m):
        indexes = randint(0, len(xs), size=len(xs))
        sample = [xs[i] for i in indexes]
        estimation += a < estimator(sample) < b
    
    return estimation/m

print(f"p estimation: {bootstrap_estimation()}")