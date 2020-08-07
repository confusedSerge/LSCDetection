matrix=$1
pre_train=$2
language=$3

task2=testsets/SemEVAL2020/$language/task2.txt
wordsim=testsets/wordsim/$language/all.tsv
freq=testsets/SemEVAL2020/$language/frequencies.tsv

out_name=$(basename $matrix)\_$language\_$pre_train
out_path=test_out/$language/$pre_train

mkdir -p $out_path

for ((c=0; c<=25; c++))
do
  outfile_ppa=$out_path/$out_name\_$c
  echo "started with $outfile_ppa and D=$c"
  python3.7 postprocessing/ppa.py $matrix $outfile_ppa $c
  
  output=$(python3.7 evaluation/test_statistik_diachron.py $outfile_ppa $outfile_ppa $task2 $wordsim $freq)
  echo "$c;$output" >> $out_path/results_$out_name.csv

  rm -f $outfile_ppa
done

rm -f $tmp_file