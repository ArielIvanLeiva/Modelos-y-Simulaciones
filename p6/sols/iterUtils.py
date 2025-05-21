def update_mean(oldmean, newdata, n):
    return oldmean + (newdata - oldmean) / n


def update_scuad(oldsquad, mean, oldmean, n):
    return oldsquad * (1 - 1 / (n - 1)) + n * (mean - oldmean) ** 2