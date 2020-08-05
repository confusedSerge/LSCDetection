input=$1

path=$(dirname $input)
name=$(basename $input ".csv")
out_path=$path/$name

mkdir -p $out_path

while IFS= read -r line
do
IFS=$';' read -ra my_array <<< $line

echo "${my_array[0]};${my_array[1]};${my_array[2]}" >> $out_path/diachron_all.csv
echo "${my_array[0]};${my_array[1]};${my_array[3]}" >> $out_path/diachron_low_c1.csv
echo "${my_array[0]};${my_array[1]};${my_array[4]}" >> $out_path/diachron_low_c2.csv
echo "${my_array[0]};${my_array[1]};${my_array[5]}" >> $out_path/diachron_high_c1.csv
echo "${my_array[0]};${my_array[1]};${my_array[6]}" >> $out_path/diachron_high_c2.csv
echo "${my_array[0]};${my_array[1]};${my_array[7]}" >> $out_path/wordsim_all_c1.csv
echo "${my_array[0]};${my_array[1]};${my_array[8]}" >> $out_path/wordsim_all_c2.csv
echo "${my_array[0]};${my_array[1]};${my_array[9]}" >> $out_path/wordsim_low_c1.csv
echo "${my_array[0]};${my_array[1]};${my_array[10]}" >> $out_path/wordsim_low_c2.csv
echo "${my_array[0]};${my_array[1]};${my_array[11]}" >> $out_path/wordsim_high_c1.csv
echo "${my_array[0]};${my_array[1]};${my_array[12]}" >> $out_path/wordsim_high_c2.csv
echo "${my_array[0]};${my_array[1]};${my_array[13]}" >> $out_path/frequency_c1.csv
echo "${my_array[0]};${my_array[1]};${my_array[14]}" >> $out_path/frequency_c2.csv
echo "${my_array[0]};${my_array[1]};${my_array[15]}" >> $out_path/frequency_d.csv
echo "${my_array[0]};${my_array[1]};${my_array[16]}" >> $out_path/isotropy1.csv
echo "${my_array[0]};${my_array[1]};${my_array[17]}" >> $out_path/isotropy2.csv
echo "${my_array[0]};${my_array[1]};${my_array[18]}" >> $out_path/len_centroid_1.csv
echo "${my_array[0]};${my_array[1]};${my_array[19]}" >> $out_path/len_centroid_2.csv

done < "$input"
