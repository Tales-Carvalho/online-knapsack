from __future__ import annotations
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def read_result(exp: int, config: int):
    data = np.loadtxt(f'results/exp{exp}_{config}.csv', skiprows=1, delimiter=',')
    return data[:,2]

if __name__ == '__main__':
    
    # Setup to save pgf files
    matplotlib.use('pgf')
    matplotlib.rcParams.update({
        'pgf.texsystem': 'pdflatex',
        'font.family': 'serif',
        'text.usetex': True,
        'pgf.rcfonts': False,
        'figure.figsize': (4, 3),
        'font.size': 9,
    })
    
    exp1 = [read_result(1, i) for i in range(1, 7)]
    exp2 = [read_result(2, i) for i in range(1, 7)]
    labels = [
        '$\epsilon=10^{{-5}}$',
        '$\epsilon=10^{{-4}}$',
        '$\epsilon=10^{{-3}}$',
        '$\epsilon=10^{{-2}}$',
        '$\epsilon=10^{{-1}}$',
        '$\epsilon=10^{{0}}$'
    ]
    
    os.makedirs('plots', exist_ok=True)
    
    plt.figure()
    plt.boxplot(exp1, labels=labels)
    plt.xlabel('Configuration')
    plt.ylabel('Experimental ratio')
    plt.tight_layout()
    plt.savefig('plots/exp1.png')
    plt.savefig('plots/exp1.pgf')

    plt.figure()
    plt.boxplot(exp2, labels=labels)
    plt.xlabel('Configuration')
    plt.ylabel('Experimental ratio')
    plt.tight_layout()
    plt.savefig('plots/exp2.png')
    plt.savefig('plots/exp2.pgf')
    
    pass
    
    