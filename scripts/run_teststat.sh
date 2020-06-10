path_to_files=$1
out_name=$2

gold=testsets/wordsim/all.tsv
freq=testsets/wordsim/freqs.tsv

# mkdir -p "test_out/ts_$out_name"

for file in $path_to_files/*
do
    echo "started with file $file"
    output=$(python3.7 evaluation/test_statistik.py $file $gold $freq)

    IFS=$'\t' read -ra my_array <<< $output
    
    echo "${my_array[0]};${my_array[1]};${my_array[3]};${my_array[4]};${my_array[5]}" >> test_out/ts_$out_name.csv
done