matrix=$1
threshold_min=$2
threshold_max=$3
out_name=$4

targets=testsets/wordsim/targets.tsv
gold=testsets/wordsim/gold.tsv
outfileCD=outfileCD.tsv

mkdir -p "test_out/ppa_$out_name"

for ((c=$threshold_min; c<=$threshold_max; c++))
do
  outfile=test_out/ppa_$out_name/ppa_$out_name\_$c
  echo "started with $outfile"

  python3.7 postprocessing/ppa.py $matrix $outfile $c

  python3.7 measures/cd.py $targets $outfile $outfile $outfileCD
  output=$(python3.7 evaluation/spr.py $outfileCD $gold $matrix gold 1 0 | grep "gold")

  IFS=$'\t' read -ra my_array <<< $output

  echo "$c;${my_array[2]}" >> test_out/ppa_$out_name/ppa_results.csv
done