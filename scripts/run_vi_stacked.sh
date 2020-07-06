matrix_1=$1
matrix_2=$2
out_name=$3
language=$4

task2=testsets/SemEVAL2020/$language/task2.txt
wordsim=testsets/wordsim/$language/all.tsv
freq=testsets/SemEVAL2020/$language/frequencies.tsv

mkdir -p "test_out/vi_stacked_ppa_$out_name/precrust"
mkdir -p "test_out/vi_stacked_ppa_$out_name/postcrust"

outfile_stacked=test_out/vi_stacked_ppa_$out_name/precrust/stacked_$out_name

bash -e scripts/make_conc.sh $matrix_1 $matrix_2 $outfile_stacked

for ((c=0; c<=25; c++))
do
  outfile_ppa=test_out/vi_stacked_ppa_$out_name/precrust/vi_ppa_$out_name\_$c

  echo "started with $outfile_ppa and D=$c"
  python3.7 postprocessing/ppa.py $outfile_stacked $outfile_ppa $c

  output=$(python3.7 evaluation/test_statistik_diachron.py $outfile_ppa $outfile_ppa $task2 $wordsim $freq)
  echo "$c;$output" >> test_out/vi_stacked_ppa_$out_name/results_precrust_vi_ppa_$out_name.csv

  postcrust_first=test_out/vi_stacked_ppa_$out_name/postcrust/vi_ppa_$out_name\_$c\_first
  postcrust_sec=test_out/vi_stacked_ppa_$out_name/postcrust/vi_ppa_$out_name\_$c\_sec

  bash -e scripts/make_unconc.sh $outfile_ppa $postcrust_first $postcrust_sec

  outfile_ppa_postcrust_one=test_out/vi_stacked_ppa_$out_name/postcrust/vi_ppa_$out_name\_$c\_alg_first
  outfile_ppa_postcrust_two=test_out/vi_stacked_ppa_$out_name/postcrust/vi_ppa_$out_name\_$c\_alg_sec
  
  python3.7 alignment/map_embeddings.py --normalize unit center --init_identical --orthogonal $postcrust_first $postcrust_sec $outfile_ppa_postcrust_one $outfile_ppa_postcrust_two 

  output=$(python3.7 evaluation/test_statistik_diachron.py $outfile_ppa_postcrust_one $outfile_ppa_postcrust_two $task2 $wordsim $freq)
  echo "$c;$output" >> test_out/vi_stacked_ppa_$out_name/results_postcrust_vi_ppa_$out_name.csv

  rm -f $outfile_ppa
  rm -f $postcrust_first
  rm -f $postcrust_sec
  rm -f $outfile_ppa_postcrust_one
  rm -f $outfile_ppa_postcrust_two
done

rm -f $outfile_stacked