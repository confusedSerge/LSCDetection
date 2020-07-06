matrix=$1
out_name=$2
language=$3

task2=testsets/SemEVAL2020/$language/task2.txt
wordsim=testsets/wordsim/$language/all.tsv
freq=testsets/SemEVAL2020/$language/frequencies.tsv

mkdir -p "test_out/wi_ppa_$out_name"

for ((c=0; c<=25; c++))
do
  outfile_ppa=test_out/wi_ppa_$out_name/wi_ppa_$out_name\_$c
  echo "started with $outfile_ppa and D=$c"

  python3.7 postprocessing/ppa.py $matrix $outfile_ppa $c
  output=$(python3.7 evaluation/test_statistik_diachron.py $outfile_ppa $outfile_ppa $task2 $wordsim $freq)
  echo "$c;$output" >> test_out/wi_ppa_$out_name/results_wi_ppa_$out_name.csv
done