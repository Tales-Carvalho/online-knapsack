from __future__ import annotations
import numpy as np

from data import Item

def threshold(y: float, p_min: float, p_max: float, beta_star: float):
    if y < beta_star:
        return p_min
    else:
        return p_min * np.exp(y/beta_star - 1)

def online_knapsack(items: list[Item], p_min: float, p_max: float):
    beta_star = 1/(1 + np.log(p_max/p_min))
    y = 0
    objective_value = 0
    decision_variables = []
    for i, item in enumerate(items):
        p = threshold(y, p_min, p_max, beta_star)
        if item.value / item.weight < p:
            x = 0
        else:
            x = 1
            y += item.weight
            objective_value += item.value
        decision_variables.append(x)
    return objective_value, decision_variables