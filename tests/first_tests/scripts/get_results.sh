#!/bin/bash
input=$1
out_file=$2

while IFS= read -r line
do
IFS=$';' read -ra my_array <<< $line

echo "${my_array[0]};${my_array[1]};${my_array[2]}" >> $out_file\_diachron_all.csv
echo "${my_array[0]};${my_array[1]};${my_array[6]}" >> $out_file\_wordsim_all_c1.csv
echo "${my_array[0]};${my_array[1]};${my_array[7]}" >> $out_file\_wordsim_all_c2.csv
echo "${my_array[0]};${my_array[1]};${my_array[16]}" >> $out_file\_isotropy_c1.csv
echo "${my_array[0]};${my_array[1]};${my_array[17]}" >> $out_file\_isotropy_c2.csv

done < "$input"