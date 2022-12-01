import numpy
from scipy.optimize import linprog
from typing import NamedTuple

class Item(NamedTuple):
    value: int
    weight: int

def generate_data(n, max_weight, p_min, p_max, seed=1):
    rand_generator = numpy.random.RandomState(seed)
    items = []
    for i in range(n):
        # For simplicity, value is drawn from U([0,1))
        value = rand_generator.rand()
        weight_ub = max(max_weight, value/p_max)
        weight_lb = value/p_min
        weight = rand_generator.rand() * (weight_ub-weight_lb) + weight_lb
        items.append(Item(value, weight))
    return items

def threshold(y, p_min, p_max, beta_star):
    if y < beta_star:
        return p_min
    else:
        return p_min * numpy.exp(y/beta_star - 1)

def online_knapsack(items, p_min, p_max):
    beta_star = 1/(1+numpy.log(p_max/p_min))
    # TODO    

def offline_knapsack(items):
    # Sample IP
    obj = [-1, -2]
    lhs_ineq = [[2, 1],
                [-4, 5],
                [1, -2]]
    
    rhs_ineq = [20, 10, 2]
    
    lhs_eq = [[-1, 5]]
    rhs_eq = [15]
    
    bnd = [(0, numpy.inf), (0, numpy.inf)]
    
    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd)
    print(opt)

def main():
    pass

if __name__ == '__main__':
    main()