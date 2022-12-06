from __future__ import annotations
from argparse import ArgumentParser
import os
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
        self.d = args.d
        self.w_max = args.w_max
        self.p_min = args.p_min
        self.p_max = args.p_max
    
    def run_one(self, seed: int):
        items = generate_data(self.n, self.d, self.w_max, self.p_min, self.p_max, seed)
        offline_obj, offline_vars = offline_knapsack(items)
        offline_sum_values, offline_sum_weights = get_values(items, offline_vars)
        verify_result(offline_sum_values, offline_sum_weights, offline_obj)
        online_obj, online_vars = online_knapsack(items, self.p_min, self.p_max)
        online_sum_values, online_sum_weights = get_values(items, online_vars)
        verify_result(online_sum_values, online_sum_weights, online_obj)
        return offline_sum_values, offline_sum_weights, online_sum_values, online_sum_weights
    
    def run_experiment(self):
        with Pool(processes=4) as pool:
            results = pool.map(self.run_one, range(self.experiments))
        return results

def main():
    parser = ArgumentParser()
    parser.add_argument("experiment_name", help="Name of experiment", type=str)
    parser.add_argument("experiments", help="Number of experiments", type=int, default=1000)
    parser.add_argument("n", help="Number of items", type=int, default=10000)
    parser.add_argument("d", help="Weights dimension of each item", type=int, default=1)
    parser.add_argument("w_max", help="Maximum weight of each item", type=float, default=0.01)
    parser.add_argument("p_min", help="Minimum density of each item", type=float, default=10)
    parser.add_argument("p_max", help="Maximum density of each item", type=float, default=1000)
    args = parser.parse_args()
    
    results = Experiment(args).run_experiment()
    
    empirical_ratios = []
    for result in results:
        offline_sum_values, offline_sum_weights, online_sum_values, online_sum_weights = result
        empirical_ratios.append(offline_sum_values / online_sum_values)
        print(f'{{Offline_Obj: {offline_sum_values}, Offline_Weight: {offline_sum_weights}, '
                + f'Online_Obj: {online_sum_values}, Online_Weights: {online_sum_weights}}}')
    
    print(f'Setup: {args.n} items, weight_dimension={args.d}, p_min={args.p_min}, p_max={args.p_max}, w_max={args.w_max}')
    print('Competitive ratio:', 1+np.log(args.p_max/args.p_min))
    print(f'Results after {args.experiments} experiments:')
    print('Average of Empirical Ratio:', np.mean(empirical_ratios))
    print('Std error of Empirical Ratio:', np.std(empirical_ratios) / np.sqrt(args.experiments))
    
    os.makedirs('results', exist_ok=True)
    with open(f'results/{args.experiment_name}.csv', 'w') as f:
        f.write('offline_result,online_result,empirical_ratio\n')
        for result, empirical_ratio in zip(results, empirical_ratios):
            offline_result, _, online_result, _ = result
            f.write(f'{offline_result},{online_result},{empirical_ratio}\n')

if __name__ == '__main__':
    main()