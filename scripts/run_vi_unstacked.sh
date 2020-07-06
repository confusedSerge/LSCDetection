matrix_1=$1
matrix_2=$2
out_name=$3
language=$4

task2=testsets/SemEVAL2020/$language/task2.txt
wordsim=testsets/wordsim/$language/all.tsv
freq=testsets/SemEVAL2020/$language/frequencies.tsv

mkdir -p "test_out/vi_unstacked_ppa_$out_name/precrust/first"
mkdir -p "test_out/vi_unstacked_ppa_$out_name/precrust/sec"
mkdir -p "test_out/vi_unstacked_ppa_$out_name/postcrust/first"
mkdir -p "test_out/vi_unstacked_ppa_$out_name/postcrust/sec"

for ((c=0; c<=25; c++))
do
  outfile_ppa_1=test_out/vi_unstacked_ppa_$out_name/precrust/first/vi_ppa_$out_name\_$c
  outfile_ppa_2=test_out/vi_unstacked_ppa_$out_name/precrust/sec/vi_ppa_$out_name\_$c

  echo "started with $outfile_ppa_1 and D=$c"
  python3.7 postprocessing/ppa.py $matrix_1 $outfile_ppa_1 $c

  echo "started with $outfile_ppa_2 and D=$c"
  python3.7 postprocessing/ppa.py $matrix_2 $outfile_ppa_2 $c
  
  output=$(python3.7 evaluation/test_statistik_diachron.py $outfile_ppa_1 $outfile_ppa_2 $task2 $wordsim $freq)
  echo "$c;$output" >> test_out/vi_unstacked_ppa_$out_name/results_precrust_wi_ppa_$out_name.csv

  outfile_ppa_postcrust_1=test_out/vi_unstacked_ppa_$out_name/postcrust/first/vi_ppa_$out_name\_$c
  outfile_ppa_postcrust_2=test_out/vi_unstacked_ppa_$out_name/postcrust/sec/vi_ppa_$out_name\_$c

  python3.7 alignment/map_embeddings.py --normalize unit center --init_identical --orthogonal $outfile_ppa_1 $outfile_ppa_2 $outfile_ppa_postcrust_1 $outfile_ppa_postcrust_2

  output=$(python3.7 evaluation/test_statistik_diachron.py $outfile_ppa_postcrust_1 $outfile_ppa_postcrust_2 $task2 $wordsim $freq)
  echo "$c;$output" >> test_out/vi_unstacked_ppa_$out_name/results_postcrust_wi_ppa_$out_name.csv
done