from pulp import LpProblem, LpVariable, GLPK, PULP_CBC_CMD, LpMaximize, LpBinary, lpSum

from data import Item

def offline_knapsack(items: list[Item]):
    problem = LpProblem('Offline_Knapsack', LpMaximize)
    values = []
    weights = []
    for i, item in enumerate(items):
        x = LpVariable(f'x_{i:09d}', cat=LpBinary)
        values.append(x * item.value)
        weights.append(x * item.weight)
    problem += (lpSum(weights) <= 1)
    problem += lpSum(values)
    problem.solve(solver=PULP_CBC_CMD(msg=False))
    objective_value = problem.objective.value()
    decision_variables = []
    for variable in problem.variables():
        decision_variables.append(variable.value())
    return objective_value, decision_variables