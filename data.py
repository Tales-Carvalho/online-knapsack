import numpy as np
from typing import NamedTuple

class Item(NamedTuple):
    value: int
    weight: int

def generate_data(n: int, max_weight: float, p_min: float, p_max: float, seed: int = 1):
    rand_generator = np.random.RandomState(seed)
    items = []
    for _ in range(n):
        # For simplicity, value is drawn from U([0,1))
        value = rand_generator.rand()
        weight_ub = min(max_weight, value/p_min)
        weight_lb = value/p_max
        # Weight is drawn from U([v_t/p_max, min(max_weight, v_t/p_min)))
        weight = rand_generator.rand() * (weight_ub-weight_lb) + weight_lb
        assert weight < max_weight
        assert value/weight >= p_min and value/weight < p_max
        items.append(Item(value, weight))
    return items

if __name__ == '__main__':
    n, w_max, p_min, p_max = 10000, 0.01, 1, 100
    print('Data generation test:')
    items = generate_data(n, w_max, p_min, p_max)
    w = [i.weight for i in items]
    print('W')
    print(np.min(w), np.max(w))
    print(np.mean(w))
    print(np.sum(w))
    p = [i.value/i.weight for i in items]
    print('P')
    print(np.min(p), np.max(p))
    print(np.mean(p))