matrix=$1
out_name=$2
language=$3

task2=testsets/SemEVAL2020/$language/task2.txt
wordsim=testsets/wordsim/$language/all.tsv
freq=testsets/SemEVAL2020/$language/frequencies.tsv
targets=testsets/SemEVAL2020/$language/targets.tsv
vac=test_src/matrix/$language/vac

mkdir -p "test_out/wi_ppa_$out_name"

tmp_file=test_out/wi_ppa_$out_name/smol_$out_name

python3.7 preprocessing/remove_words.py $matrix $targets $vac $tmp_file

for ((c=0; c<=25; c++))
do
  outfile_ppa=test_out/wi_ppa_$out_name/wi_ppa_$out_name\_$c
  echo "started with $outfile_ppa and D=$c"
  python3.7 postprocessing/ppa.py $tmp_file $outfile_ppa $c
  
  output=$(python3.7 evaluation/test_statistik_diachron.py $outfile_ppa $outfile_ppa $task2 $wordsim $freq)
  echo "$c;$output" >> test_out/wi_ppa_$out_name/results_wi_ppa_$out_name.csv

  rm -f $outfile_ppa
done

rm -f $tmp_file