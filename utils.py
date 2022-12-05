import numpy as np

from data import Item

def get_values(items: list[Item], variables: list[int]):
    sum_values = np.sum([i.value * x for i, x in zip(items, variables)])
    sum_weights = np.sum([i.weight * x for i, x in zip(items, variables)])
    return sum_values, sum_weights

def verify_result(sum_values: float, sum_weights: float, objective: float, tol: float = 0.00001):
    assert(sum_weights < 1 + tol)
    assert(np.isclose(sum_values, objective, tol))