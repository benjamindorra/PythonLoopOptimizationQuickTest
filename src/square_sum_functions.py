import numpy as np
from numba import jit
from square_sum_module import square_sum


def base_function(x):
    result = 0
    for i in x:
        result += i**2
    return result


@jit(nopython=True)
def jit_function(x):
    result = 0
    for i in x:
        result += i**2
    return result


def vector_function(x):
    x2 = np.square(x)
    result = np.sum(x2)
    return result


def rust_function(x):
    result = square_sum(x)
    return result
