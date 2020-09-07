corp=("sde" "puk")

for i in "${corp[@]}"
do
    echo "$i"
    
    src_path=test_src/ln_exp/$i
    out_path=test_out/ln_exp/$i

    wordsim=testsets/wordsim/$i/all.tsv
    freq=testsets/wordsim/$i/freqs.tsv
    
    mkdir -p $out_path

    for j in $src_path/*
    do
        echo "$j"
        out_name=$(basename $j)

        output=$(python3.8 evaluation/test_statistik_wordsim_lengthseparated.py $j $wordsim $freq)
        
        for ((c=0; c<=25; c++))
        do
            # baseline calculation
            echo "$c;$output" >> $out_path/results_baseline_$out_name.csv
        done
    done
done