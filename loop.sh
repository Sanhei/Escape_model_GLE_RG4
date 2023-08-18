#!/bin/bash

n=20
base=10
for ((i=0; i<n; i++)); do
        echo $(($i))
        exponent=$(echo "0.2*$i" | bc)
        result=$(awk -v base="$base" -v exponent="$exponent" 'BEGIN {print base ** exponent}')
        result=$(echo "0.001*$result" | bc)
        echo "mass: $result"
        python K_FFPT.py "$result" 0.0001 0.001 "ffpt_m_${result}_g_0.001.txt" 100000
        python plot_ffpt.py   "ffpt_m_${result}_g_0.001.txt" "$result" 0.001
done
