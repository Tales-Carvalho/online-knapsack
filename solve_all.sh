#!/bin/sh

source env/bin/activate
mkdir -p results

for config in 1 2 3 4 5 6 7
do
    source configs/$config.env
    echo $w_max
    python main.py $e $n $w_max $p_min $p_max > results/wmax_$w_max.out
done