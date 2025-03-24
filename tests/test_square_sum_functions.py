import numpy as np
import pytest
from src.square_sum_functions import (base_function, jit_function, rust_function,
                                  vector_function)


@pytest.fixture
def example_array():
    # squares of 1 to 5 sum to 55
    return np.arange(6)


@pytest.fixture
def example_result():
    # squares from 1 to 5 sum to 55
    return 55


def test_base_function(example_array, example_result):
    assert base_function(example_array) == example_result


def test_jit_function(example_array, example_result):
    assert jit_function(example_array) == example_result


def test_vector_function(example_array, example_result):
    assert vector_function(example_array) == example_result


def test_rust_function(example_array, example_result):
    assert rust_function(example_array) == example_result
