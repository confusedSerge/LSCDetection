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

for ((c=0; c<=25; c++))
do
  outfile_ppa_1=$out_path/first_$out_name\_unstacked_$c
  outfile_ppa_2=$out_path/sec_$out_name\_unstacked_$c

  echo "started with $outfile_ppa_1 and D=$c"
  python3.8 postprocessing/ppa.py $matrix_1 $outfile_ppa_1 $c

  echo "started with $outfile_ppa_2 and D=$c"
  python3.8 postprocessing/ppa.py $matrix_2 $outfile_ppa_2 $c

  outfile_stacked=$out_path/tmp_stacked_$out_name
  bash -e scripts/make_conc.sh $outfile_ppa_1 $outfile_ppa_2 $outfile_stacked
  header=$(sed -n 1p $outfile_stacked)
  IFS=$' ' read -ra arr <<< $header
  i=$((${arr[0]} + ${arr[1]}))
  sed -i 1d $outfile_stacked
  sed -i "1s/^/$i ${arr[2]}\n/" $outfile_stacked
  
  output=$(python3.8 evaluation/test_statistik_diachron.py $outfile_stacked $outfile_stacked $task2 $wordsim $freq)
  echo "$c;$output" >> $out_path/results_unstacked_$out_name.csv

  rm -f $outfile_ppa_1
  rm -f $outfile_ppa_2
  rm -f $outfile_stacked
done