from timeit import timeit
from statistics import mean

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

def get_samples(fs, size):
    """
    Gets a list of samples by executing f in fs 'size' times. 
    Assumes f receives exactly one parameter size.
    """
    
    return [f(size) for f in fs]

def get_execution_times(fs, size, internal_size=1):
    """
    Gets a list of the average execution time of running f in fs 'size' times. 
    Assumes f receives exactly one parameter 'internal_size'.
    """
    
    return [timeit(lambda: f(internal_size))/size for f in fs]

def probability_of(sample, predicate):
    return mean(int(predicate(x)) for x in sample)