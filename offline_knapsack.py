from __future__ import annotations
from pulp import LpProblem, LpVariable, GLPK, PULP_CBC_CMD, LpMaximize, LpBinary, lpSum

from data import Item

def offline_knapsack(items: list[Item]):
    problem = LpProblem('Offline_Knapsack', LpMaximize)
    values = []
    # Assuming all items have same dimension
    weights_dimensions = [[] for _ in range(len(items[0].weights))]
    for i, item in enumerate(items):
        x = LpVariable(f'x_{i:09d}', cat=LpBinary)
        values.append(x * item.value)
        for j, w in enumerate(item.weights):
            weights_dimensions[j].append(x * w)
    for weights in weights_dimensions:
        problem += (lpSum(weights) <= 1)
    problem += lpSum(values)
    problem.solve(solver=PULP_CBC_CMD(msg=False, threads=8))
    objective_value = problem.objective.value()
    decision_variables = []
    for variable in problem.variables():
        decision_variables.append(variable.value())
    return objective_value, decision_variables