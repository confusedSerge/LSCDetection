#!/bin/bash
matrix_one=$1
matrix_two=$2

cp $matrix_two $matrix_two\_backup

sed -i 1d $matrix_one

while IFS= read -r line
do
echo "_$line" >> $matrix_two
done < "$matrix_one"