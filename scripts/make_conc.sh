#!/bin/bash
matrix_one=$1
matrix_two=$2
outfile=$3

IFS=$' ' read -ra head_one <<< $(head -n 1 $matrix_one)
IFS=$' ' read -ra head_two <<< $(head -n 1 $matrix_two)

echo "${head_one[0]} ${head_two[0]} ${head_two[1]} " >> $outfile

awk '{if(NR>1)print $1=$1"_ " substr($0, index($0,$2))}' $matrix_one >> $outfile
sed -n '1!p' $matrix_two >> $outfile

