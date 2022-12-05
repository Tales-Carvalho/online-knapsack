import numpy as np

from data import Item

def verify_result(items: list[Item], variables: list[int], objective: float, tol: float = 0.00001):
    sum_weights = np.sum([i.weight * x for i, x in zip(items, variables)])
    assert(sum_weights < 1 + tol)
    sum_values = np.sum([i.value * x for i, x in zip(items, variables)])
    assert(np.isclose(sum_values, objective, tol))