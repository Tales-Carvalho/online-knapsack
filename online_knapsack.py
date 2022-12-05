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
    y = [0 for _ in range(len(items[0].weights))]
    objective_value = 0
    decision_variables = []
    for i, item in enumerate(items):
        x = 1
        for j, w in enumerate(item.weights):
            p = threshold(y[j], p_min, p_max, beta_star)
            if item.value / item.weight < p:
                x = 0
        if x == 1:
            y += item.weights # TODO: does this work?
            objective_value += item.value
        decision_variables.append(x)
    return objective_value, decision_variables