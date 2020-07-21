matrix_1=$1
matrix_2=$2
out_name=$3
language=$4

task2=testsets/SemEVAL2020/$language/task2.txt
wordsim=testsets/wordsim/$language/all.tsv
freq=testsets/SemEVAL2020/$language/frequencies.tsv

mkdir -p "test_out/vi_stacked_ppa_$out_name"

outfile_stacked=test_out/vi_stacked_ppa_$out_name/stacked_$out_name
tmp_file_one=test_out/vi_stacked_ppa_$out_name/smol_one_$out_name
tmp_file_two=test_out/vi_stacked_ppa_$out_name/smol_two_$out_name

python3.7 preprocessing/remove_words.py $matrix_1 $wordsim $tmp_file_one
python3.7 preprocessing/remove_words.py $matrix_2 $wordsim $tmp_file_two

bash -e scripts/make_conc.sh $tmp_file_one $tmp_file_two $outfile_stacked

rm -f $tmp_file_one
rm -f $tmp_file_two

for ((c=0; c<=25; c++))
do
  outfile_ppa=test_out/vi_stacked_ppa_$out_name/vi_ppa_$out_name\_$c

  echo "started with $outfile_ppa and D=$c"
  header=$(sed -n 1p $outfile_stacked)
  python3.7 postprocessing/ppa.py $outfile_stacked $outfile_ppa $c
  sed -i 1d $outfile_ppa
  sed -i "1s/^/$header\n/" $outfile_ppa

  output=$(python3.7 evaluation/test_statistik_diachron.py $outfile_ppa $outfile_ppa $task2 $wordsim $freq)
  echo "$c;$output" >> test_out/vi_stacked_ppa_$out_name/results_precrust_vi_ppa_$out_name.csv

  rm -f $outfile_ppa
done

rm -f $outfile_stacked