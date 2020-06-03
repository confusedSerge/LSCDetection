matrix=$1
threshold_min=$2
threshold_max=$3
dim_red_min=$4
dim_red_max=$5

targets=testsets/wordsim/targets.tsv
gold=testsets/wordsim/gold.tsv
outfileCD=outfileCD.tsv

mkdir -p "test_out/algo_n"

for ((i= $threshold_min; i<=$threshold_max; i++))
do
  for ((j= $dim_red_min; j<=$dim_red_max; j++))
  do
    outfile=test_out/algo_n/algo_n_$i\_$j
    python3.7 postprocessing/algo_n.py $matrix $outfile $i $j

    python3.7 measures/cd.py $targets $outfile $outfile $outfileCD
    output=$(python3.7 evaluation/spr.py $outfileCD $gold $matrix gold 1 0 | grep "gold")

    IFS=$'\t' read -ra my_array <<< $output

  echo "$i;$j;${my_array[2]}" >> test_out/algo_n/algo_n_results.csv
  done
done