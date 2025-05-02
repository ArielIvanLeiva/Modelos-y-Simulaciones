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
