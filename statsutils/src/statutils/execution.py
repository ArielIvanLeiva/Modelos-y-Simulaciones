from timeit import timeit


def update_mean(oldmean, newdata, n):
    return oldmean + (newdata - oldmean) / n


def update_scuad(oldsquad, mean, oldmean, n):
    return oldsquad * (1 - 1 / (n - 1)) + n * (mean - oldmean) ** 2


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

    return [timeit(lambda: f(internal_size)) / size for f in fs]
