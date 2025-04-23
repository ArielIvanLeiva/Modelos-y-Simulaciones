# %%
# Ejercicio 9
from numpy.random import random

# %%
class Geometric():
    def __init__(self, p):
        assert 0 <= p <= 1, f"p = {p}, wich is not a probability"

        self.p = p

    # a)
    def inv_method(self):
        pass
    
    # b)
    def full_sim_method(self):
        u = random()
        tries = 0
        p = self.p
        
        while u >= p:
            tries += 1
            u = random()
            
        return tries


X = Geometric(0.8)
X.full_sim_method()