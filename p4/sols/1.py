# Display utility function
# %%
from IPython.display import display, Math
def dp(text):
    display(Math(text))

# Ejercicio 1
# %%
# a)
# i)
from IPython.display import display, Math
import sympy as sp
import numpy as np
import math
from numpy.random import random

# ESTO ESTÁ MAL PERO LO DEJO COMO EJEMPLO PARA EL USO DE LATEX
# r, i = sp.symbols("r i")
# prod = sp.Product(1/(100-i),(i, 0, r-1))

# dp(r'\text{P(X1=1, X2=2, ... , Xr=r) = }' + sp.latex(prod))
# dp(r'\text{En el caso de r = 10:}')
# prod = prod.subs(r, 10)
# dp(sp.latex(prod) + '=' + f'{prod.evalf()}')

class Experiment():
    def __init__(self, numOfCards=100):
        self.n = numOfCards
    
    def get_avg_variance(self, mean, size=100000):
        res = 0
        
        for i in range(size):
            res += Experiment.get_num_of_successes(self.sample())**2
        
        res = (res - size * mean**2)/(size - 1)
        
        return res
            
        
    def get_avg_successes(self, size=100000):
        sum = 0
        for _ in range(size):
            sum += Experiment.get_num_of_successes(self.sample())
            
        return sum/size
             
    def sample(self, size=1):
        return self.get_random_permutation() if size == 1 else [self.get_random_permutation() for _ in range(size)]

    def get_num_of_successes(nums):
        return sum(1 for i, x in enumerate(nums) if i == x)

    def get_random_permutation(self):
        nums = list(range(self.n))
        n = len(nums)
        
        for i in range(n-1, 0, -1):
            u = int((i+1)*random())
            nums[i], nums[u] = nums[u], nums[i]
        
        return nums

# a)
n, r = sp.symbols("n r")
prob = sp.factorial(n-r)/sp.factorial(n)

dp(r'P(E1 \cap E2 \cap ... \cap Er) = ' + sp.latex(prob) + ' = ' + sp.latex(prob.subs({r: 10, n: 100}).evalf()))
# %%

# c)
n = 100
X = Experiment(n)

avg = X.get_avg_successes()
#[Experiment.get_num_of_successes(x) for x in X.sample(100)]
avg_variance = X.get_avg_variance(avg)

dp( r'\text{'+ f"Estimated Mean: {avg}, Estimated Variance: {avg_variance}" + '}')
# %%
