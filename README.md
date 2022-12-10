# Online Knapsack Solver

This project contains the implementation of a threshold algorithm for solving the 0-1 knapsack problem in online manner. This assumes that every item arrives sequentially and decisions must be made immediatly and irrevocably.

## Setup

All the PyPI requirements are within the project and no external dependency is necessary. Recommended setup through venv:

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Execution

Knapsack instances can be passed as arguments in the main.py file, following the usage instruction:

```
usage: main.py [-h] experiment_name experiments n d w_max p_min p_max

positional arguments:
  experiment_name  Name of experiment
  experiments      Number of experiments
  n                Number of items
  d                Weights dimension of each item
  w_max            Maximum weight of each item
  p_min            Minimum density of each item
  p_max            Maximum density of each item

options:
  -h, --help       show this help message and exit
```

The config files in the folder `configs` provide fixed parameters for experiments, and are accessed through the scripts `solve_exp_1.sh` and `solve_exp_2.sh`, which automatically generate the results and log files.

Plots are obtained by executing the `plot_results.py` script.

## Results

Result files contains the optimal results (offline integer programming solution), the algorithm results and the empirical ratio for every execution of the program, organized in CSV files.

## Acknowledgement

This project has been submitted as part of an assignment for the course "CMPUT676 - Optimization and Decision Making under Uncertainty", instructed by Dr. Xiaoqi Tan, at the Computing Science Centre at University of Alberta.