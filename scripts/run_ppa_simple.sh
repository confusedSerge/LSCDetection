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
            # ppa with mean centering
            outfile_ppa=$out_path/$out_name\_$c

            python3.8 postprocessing/ppa.py $j $outfile_ppa $c
            
            output=$(python3.8 evaluation/test_statistik_wordsim.py $outfile_ppa $wordsim $freq)
            echo "$c;$output" >> $out_path/results_$out_name.csv
            
            rm -f $outfile_ppa

            # ppa without mean centering
            python3.8 postprocessing/ppa_wo_mc.py $j $outfile_ppa $c
            
            output=$(python3.8 evaluation/test_statistik_wordsim.py $outfile_ppa $wordsim $freq)
            echo "$c;$output" >> $out_path/results_wo_mc_$out_name.csv
            
            rm -f $outfile_ppa
        done
    done
done