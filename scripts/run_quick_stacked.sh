matrix_1=$1
matrix_2=$2
pre_train=$3
language=$4

task2=testsets/SemEVAL2020/$language/task2.txt
wordsim=testsets/wordsim/$language/all.tsv
freq=testsets/SemEVAL2020/$language/frequencies.tsv

out_name=$(basename $matrix_2)\_$language\_$pre_train
out_path=test_out/$language/$pre_train

mkdir -p $out_path

outfile_stacked=$out_path/tmp_stacked_$out_name
bash -e scripts/make_conc.sh $matrix_1 $matrix_2 $outfile_stacked

for ((c=0; c<=25; c++))
do
  outfile_ppa=$out_path/$out_name\_stacked_$c

  echo "started with $outfile_ppa and D=$c"
  # header=$(sed -n 1p $outfile_stacked)
  python3.8 postprocessing/ppa.py $outfile_stacked $outfile_ppa $c
  # sed -i 1d $outfile_ppa
  # sed -i "1s/^/$header\n/" $outfile_ppa

  output=$(python3.8 evaluation/test_statistik_diachron.py $outfile_ppa $outfile_ppa $task2 $wordsim $freq)
  echo "$c;$output" >> $out_path/results_stacked_$out_name.csv

  rm -f $outfile_ppa
done

rm -f $outfile_stacked