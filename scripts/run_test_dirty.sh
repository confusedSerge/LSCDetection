#!/bin/bash
matrix_path_one=$1
matrix_path_two=$2
gold_path=$3

mkdir -p test_out/ppa
echo " $matrix_path_one" >> test_out/ppa/ppa_results.csv
for i in {0..25} 
do
    output=$(python3.7 evaluation/subtask2.py $matrix_path_one$i $matrix_path_two$i $gold_path | grep "$matrix_path_one$i")

    IFS=$'\t' read -ra my_array <<< $output

    echo "Stats: 300;$i;${my_array[1]}"
    echo "300;$i;${my_array[1]}" >> test_out/ppa/ppa_results.csv
done