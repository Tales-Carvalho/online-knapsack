#!/bin/sh

source env/bin/activate
mkdir -p results

for config in 1 2 3 4 5 6 7
do
    source configs/$config.env
    python main.py $e $n $w_max $p_min $p_max > results/$config.out
done