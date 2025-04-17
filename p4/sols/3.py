# Display utility function
# %%
from IPython.display import display, Math


def dp(text):
    display(Math(text))


# %%
# Ejercicio 3
from numpy.random import random
from statistics import mean, stdev
import pandas as pd


# %%
# a)
def simulation():
    tries = 0
    checklist = set(range(2, 12 + 1))

    while len(checklist) != 0:
        tries += 1

        u1 = int(6 * random() + 1)
        u2 = int(6 * random() + 1)

        checklist.discard(u1 + u2)

    return tries


# %%
# b)
ns = [100, 1000, 10000, 100000]

# i)

means = [mean(simulation() for _ in range(n)) for n in ns]
stdevs = [stdev(simulation() for _ in range(n)) for n in ns]

# %%
print(f"Means: {list(zip(ns, means))}")
print(f"Stdevs: {list(zip(ns, stdevs))}")

# %%
# ii)


def probability_of(sample, check):
    assertions = 0
    for x in sample:
        assertions += check(x)

    return assertions / len(sample)


samples = [[simulation() for _ in range(n)] for n in ns]

p_ge_15 = [probability_of(sample, lambda x: x >= 15) for sample in samples]
p_le_9 = [probability_of(sample, lambda x: x <= 9) for sample in samples]

# %%
df_p_ge_15 = pd.DataFrame({"n": ns, "P(N >= 15)": p_ge_15})
df_p_le_9 = pd.DataFrame({"n": ns, "P(N <= 9)": p_le_9})

print(df_p_ge_15)
print()
print(df_p_le_9)
