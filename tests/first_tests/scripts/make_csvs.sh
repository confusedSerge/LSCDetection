#!/bin/bash
input=$1
out_file=$2

while IFS= read -r line
do
#   echo "my line: $line"

IFS=$';' read -ra my_array <<< $line

echo "${my_array[0]};${my_array[1]};${my_array[2]}" >> new_ts_results/$out_file\_center.csv
echo "${my_array[0]};${my_array[1]};${my_array[3]}" >> new_ts_results/$out_file\_wordsim.csv
echo "${my_array[0]};${my_array[1]};${my_array[4]}" >> new_ts_results/$out_file\_lowfreq.csv
echo "${my_array[0]};${my_array[1]};${my_array[5]}" >> new_ts_results/$out_file\_highfreq.csv
echo "${my_array[0]};${my_array[1]};${my_array[6]}" >> new_ts_results/$out_file\_freqcor.csv

done < "$input"