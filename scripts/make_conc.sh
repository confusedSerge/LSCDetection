#!/bin/bash
matrix_one=$1
matrix_two=$2

cp $matrix_one $matrix_one\_backup
cp $matrix_two $matrix_two\_backup

sed -i 1d $matrix_two

awk '{print $1=$1"_ " substr($0, index($0,$2))}' $matrix_two >> $matrix_one