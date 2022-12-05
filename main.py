from argparse import ArgumentParser
import numpy as np

from utils import verify_result
from data import generate_data
from online_knapsack import online_knapsack
from offline_knapsack import offline_knapsack

def main():
    parser = ArgumentParser()
    parser.add_argument("experiments", help="Number of experiments", type=int, default=1000)
    parser.add_argument("n", help="Number of items", type=int, default=10000)
    parser.add_argument("w_max", help="Maximum weight of items", type=float, default=0.01)
    parser.add_argument("p_min", help="Minimum density of items", type=float, default=10)
    parser.add_argument("p_max", help="Maximum density of items", type=float, default=1000)
    args = parser.parse_args()
    
    empirical_ratios = []
    for e in range(args.experiments):
        items = generate_data(args.n, args.w_max, args.p_min, args.p_max, seed=e)
        offline_obj, offline_vars = offline_knapsack(items)
        verify_result(items, offline_vars, offline_obj)
        online_obj, online_vars = online_knapsack(items, args.p_min, args.p_max)
        verify_result(items, online_vars, online_obj)
        empirical_ratios.append(offline_obj/online_obj)
    
    print(f'Setup: {args.n} items, p_min={args.p_min}, p_max={args.p_max}, w_max={args.w_max}')
    print('Competitive ratio:', 1+np.log(args.p_max/args.p_min))
    print(f'Results after {args.experiments} experiments:')
    print('Average of Empirical Ratio:', np.mean(empirical_ratios))
    print('Std error of Empirical Ratio:', np.std(empirical_ratios) / np.sqrt(args.experiments))

if __name__ == '__main__':
    main()