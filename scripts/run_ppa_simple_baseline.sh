corp=("sde" "puk")

for i in "${corp[@]}"
do
    echo "$i"

    src_path=test_src/$i
    out_path=test_out/$i

    wordsim=testsets/wordsim/$i/all.tsv
    freq=testsets/wordsim/$i/freqs.tsv
    
    mkdir -p $out_path

    for j in $src_path/*
    do
        echo "$j"
        out_name=$(basename $j)

        for ((c=0; c<=25; c++))
        do
            # baseline calculation
            output=$(python3.8 evaluation/test_statistik_wordsim.py $j $wordsim $freq)
            echo "$c;$output" >> $out_path/results_baseline_$out_name.csv
        done
    done
done