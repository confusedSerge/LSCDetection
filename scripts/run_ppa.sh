matrix=$1
threshold_min=$2
threshold_max=$3

targets=testsets/wordsim/targets.tsv
gold=testsets/wordsim/gold.tsv
outfileCD=outfileCD.tsv

mkdir -p "test_out/ppa"

for ((c=$threshold_min; c<=$threshold_max; c++))
do
  outfile=test_out/ppa/ppa_$c
  py postprocessing/ppa.py $matrix $outfile $c

  py measures/cd.py $targets $outfile $outfile $outfileCD
  output=$(py evaluation/spr.py $outfileCD $gold $matrix gold 1 0 | grep "gold")

  IFS=$'\t' read -ra my_array <<< $output

  echo "$c;${my_array[2]}" >> test_out/ppa/ppa_results.csv
done