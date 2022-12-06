from __future__ import annotations
import numpy as np

from data import Item

def get_values(items: list[Item], variables: list[int]):
    sum_values = np.sum([i.value * x for i, x in zip(items, variables)])
    sum_weights = np.sum([np.multiply(i.weights, x) for i, x in zip(items, variables)], axis=0)
    return sum_values, sum_weights

def verify_result(sum_values: float, sum_weights: float, objective: float, tol: float = 0.0001):
    for s in sum_weights:
        assert(s < 1 + tol)
    assert(np.isclose(sum_values, objective, tol))