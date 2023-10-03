def median_index(sorted_array):
    length = len(sorted_array)

    if length % 2 == 0:
        return (length // 2) - 1

    return length // 2


def median(sorted_array):
    index = median_index(sorted_array)
    return sorted_array[index]


def bfprt(X, z, y=None, r=5):
    sublists = [X[j : j + r] for j in range(0, len(X), r)]
    medians = [sorted(sublist)[median_index(sublist)] for sublist in sublists]

    if len(medians) <= r:
        pivot = sorted(medians)[median_index(medians)]
    else:
        pivot = bfprt(medians, median_index(medians), r=r)

    high = [j for j in X if j < pivot]
    low = [j for j in X if j > pivot]

    k = len(low)

    if z < k:
        return bfprt(low, z, r=r)
    elif z > k:
        return bfprt(high, z - k - 1, r=r)
    else:
        return pivot


def select_bfprt(x, y, z, r=5):
    if 1 > z or y < z:
        return False

    z -= 1

    return bfprt(X=x, y=y, z=z, r=r)
