matrix_1=$1
matrix_2=$2
out_name=$3
language=$4

task2=testsets/SemEVAL2020/$language/task2.txt
wordsim=testsets/wordsim/$language/all.tsv
freq=testsets/SemEVAL2020/$language/frequencies.tsv
targets=testsets/SemEVAL2020/$language/targets.tsv

mkdir -p "test_out/vi_unstacked_ppa_$out_name"

tmp_file_one=test_out/vi_unstacked_ppa_$out_name/smol_one_$out_name
tmp_file_two=test_out/vi_unstacked_ppa_$out_name/smol_two_$out_name

python3.7 preprocessing/remove_words.py $matrix_1 $targets $tmp_file_one
python3.7 preprocessing/remove_words.py $matrix_2 $targets $tmp_file_two

for ((c=0; c<=25; c++))
do
  outfile_ppa_1=test_out/vi_unstacked_ppa_$out_name/first_vi_ppa_$out_name\_$c
  outfile_ppa_2=test_out/vi_unstacked_ppa_$out_name/sec_vi_ppa_$out_name\_$c

  echo "started with $outfile_ppa_1 and D=$c"
  python3.7 postprocessing/ppa.py $tmp_file_one $outfile_ppa_1 $c

  echo "started with $outfile_ppa_2 and D=$c"
  python3.7 postprocessing/ppa.py $tmp_file_two $outfile_ppa_2 $c
  
  output=$(python3.7 evaluation/test_statistik_diachron.py $outfile_ppa_1 $outfile_ppa_2 $task2 $wordsim $freq)
  echo "$c;$output" >> test_out/vi_unstacked_ppa_$out_name/results_precrust_vi_ppa_$out_name.csv

  rm -f $outfile_ppa_1
  rm -f $outfile_ppa_2
done

rm -f $tmp_file_one
rm -f $tmp_file_two