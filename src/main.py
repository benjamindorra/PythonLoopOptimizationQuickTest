import argparse
import time

import numpy as np

from square_sum_functions import (base_function, jit_function, rust_function,
                                  vector_function)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_iters", type=int, default=100)
    args = parser.parse_args()
    num_iters = args.num_iters
    arr = np.arange(1000000, dtype=np.int64)

    start = time.time()
    for _ in range(num_iters):
        _ = base_function(arr)
    time_base = time.time() - start

    start = time.time()
    for _ in range(num_iters):
        _ = jit_function(arr)
    time_jit = time.time() - start

    start = time.time()
    for _ in range(num_iters):
        _ = vector_function(arr)
    time_vector = time.time() - start

    start = time.time()
    for _ in range(num_iters):
        _ = rust_function(arr)
    time_rust = time.time() - start

    gain_jit = (time_base - time_jit) * 100 / time_base
    gain_vector = (time_base - time_vector) * 100 / time_base
    gain_rust = (time_base - time_rust) * 100 / time_base

    print(f"Gain de performance avec Numba: {round(gain_jit, 2)}%")
    print(f"Gain de performance avec Numpy: {round(gain_vector, 2)}%")
    print(f"Gain de performance avec Rust: {round(gain_rust, 2)}%")


main()
