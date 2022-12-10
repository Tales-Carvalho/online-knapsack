#!/bin/sh

source env/bin/activate
mkdir -p logs

for config in 1 2 3 4 5 6
do
    source configs/$config.env
    python main.py exp2_$config $e $n 2 $w_max $p_min $p_max > logs/exp2_$config.out
done