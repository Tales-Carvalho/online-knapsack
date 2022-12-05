from argparse import ArgumentParser
import numpy as np
from multiprocessing import Pool

from utils import verify_result, get_values
from data import Item, generate_data
from online_knapsack import online_knapsack
from offline_knapsack import offline_knapsack

class Experiment:
    def __init__(self, args):
        self.experiments = args.experiments
        self.n = args.n
        self.w_max = args.w_max
        self.p_min = args.p_min
        self.p_max = args.p_max

    def init_inputs(self):
        sets_items = []
        for e in range(self.experiments):
            sets_items.append(generate_data(self.n, self.w_max, self.p_min, self.p_max, seed=e))
        return sets_items
    
    def run_one(self, items: list[Item]):
        offline_obj, offline_vars = offline_knapsack(items)
        offline_sum_values, offline_sum_weights = get_values(items, offline_vars)
        verify_result(offline_sum_values, offline_sum_weights, offline_obj)
        online_obj, online_vars = online_knapsack(items, self.p_min, self.p_max)
        online_sum_values, online_sum_weights = get_values(items, online_vars)
        verify_result(online_sum_values, online_sum_weights, online_obj)
        return offline_sum_values, offline_sum_weights, online_sum_values, online_sum_weights
    
    def run_experiment(self):
        sets_items = self.init_inputs()
        with Pool() as pool:
            results = pool.map(self.run_one, sets_items)
        return results

def main():
    parser = ArgumentParser()
    parser.add_argument("experiments", help="Number of experiments", type=int, default=1000)
    parser.add_argument("n", help="Number of items", type=int, default=10000)
    parser.add_argument("w_max", help="Maximum weight of items", type=float, default=0.01)
    parser.add_argument("p_min", help="Minimum density of items", type=float, default=10)
    parser.add_argument("p_max", help="Maximum density of items", type=float, default=1000)
    args = parser.parse_args()
    
    results = Experiment(args).run_experiment()
    
    empirical_ratios = []
    for result in results:
        offline_sum_values, offline_sum_weights, online_sum_values, online_sum_weights = result
        empirical_ratios.append(offline_sum_values / online_sum_values)
        print(f'{{Offline_Obj: {offline_sum_values}, Offline_Weight: {offline_sum_weights}, '
                + f'Online_Obj: {online_sum_values}, Online_Weights: {online_sum_weights}}}')
    
    print(f'Setup: {args.n} items, p_min={args.p_min}, p_max={args.p_max}, w_max={args.w_max}')
    print('Competitive ratio:', 1+np.log(args.p_max/args.p_min))
    print(f'Results after {args.experiments} experiments:')
    print('Average of Empirical Ratio:', np.mean(empirical_ratios))
    print('Std error of Empirical Ratio:', np.std(empirical_ratios) / np.sqrt(args.experiments))

if __name__ == '__main__':
    main()