#!/bin/sh

source env/bin/activate
mkdir -p results

e=1000
n=10000
p_min=0.1
p_max=1000

for w_min in 0.01 0.05 0.1 0.5 1 5 10
do
    python main.py $e $n $w_min $p_min $p_max > results/wmin_$w_min.out
done