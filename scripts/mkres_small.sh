input=$1

path=$(dirname $input)
name=$(basename $input ".csv")
out_path=$path/$name

mkdir -p $out_path

while IFS= read -r line
do
IFS=$';' read -ra my_array <<< $line

echo "${my_array[0]};${my_array[1]};${my_array[2]}" >> $out_path/wordsim.csv
echo "${my_array[0]};${my_array[1]};${my_array[3]}" >> $out_path/frequency.csv
echo "${my_array[0]};${my_array[1]};${my_array[4]}" >> $out_path/isotropy.csv
echo "${my_array[0]};${my_array[1]};${my_array[5]}" >> $out_path/isotropy_norm.csv
echo "${my_array[0]};${my_array[1]};${my_array[6]}" >> $out_path/len_centroid.csv
echo "${my_array[0]};${my_array[1]};${my_array[7]}" >> $out_path/len_centroid_norm.csv

done < "$input"

# wordsim, frequency, isotropy, isotropy_norm, len_centroid, len_centroid_norm