# %%
import sympy as sp

def fun(x):
    return x/(1 + x**4)

x = sp.Symbol("x")

sp.Integral(fun(x),(x, 0, sp.oo)).evalf()
