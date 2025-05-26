from statistics import mean
import matplotlib.pyplot as plt
import numpy as np

def get_rel_frecuencies(sample, keys=range(1, 10 + 1)):
    frecuencies = {i: 0 for i in keys}

    for x in sample:
        if x in frecuencies.keys():
            frecuencies[x] += 1

    return {i: value / len(sample) for i, value in frecuencies.items()}


def get_density_frecuencies(sample):
    frecuencies = {}

    for x in sample:
        if x in frecuencies.keys():
            frecuencies[x] += 1
        else:
            frecuencies[x] = 1

    return {i: value / len(sample) for i, value in frecuencies.items()}


def probability_of(sample, predicate):
    return mean(int(predicate(x)) for x in sample)


def get_ic_confidence(ics, real_value):
    return probability_of(ics, lambda x: x[0] <= real_value <= x[1])

def plot_fun(fun, start, end, num=10000, limits=None, figsize=(6,4), ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize, constrained_layout=True)

    xs = np.linspace(start, end, num)
    ys = [fun(x) for x in xs]
    ax.plot(xs, ys)
    
    if limits:
        ax.set_xlim(*limits[0])
        ax.set_ylim(*limits[1])

    ax.set_aspect('equal')
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

    return ax