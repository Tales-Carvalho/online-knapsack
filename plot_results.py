from __future__ import annotations
import os
import scipy
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def read_result(exp: int, config: int):
    data = np.loadtxt(f'results/exp{exp}_{config}.csv', skiprows=1, delimiter=',')
    return data[:,2]

if __name__ == '__main__':
    
    # Setup to save pgf files
    # matplotlib.use('pgf')
    # matplotlib.rcParams.update({
    #     'pgf.texsystem': 'pdflatex',
    #     'font.family': 'serif',
    #     'text.usetex': True,
    #     'pgf.rcfonts': False,
    #     'figure.figsize': (5, 3.75),
    #     'font.size': 9,
    # })
    
    exp1 = [read_result(1, i) for i in range(1, 7)]
    exp2 = [read_result(2, i) for i in range(1, 7)]
    
    os.makedirs('plots', exist_ok=True)
    
    plt.figure()
    plt.boxplot(exp1)
    plt.savefig('plots/exp1.png')

    plt.figure()
    plt.boxplot(exp2)
    plt.savefig('plots/exp2.png')
    
    pass
    
    