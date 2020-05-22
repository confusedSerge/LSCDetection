matrix=$1
threshold_min=$2
threshold_max=$3
dim_red_min=$4
dim_red_max=$5

mkdir -p "test_out/algo_n"

for ((i= $threshold_min; i<=$threshold_max; i++))
do
  for ((j= $dim_red_min; j<=$dim_red_max; j++))
  do
    outfile=test_out/algo_n/algo_n_$i\_$j
    py postprocessing/algo_n.py $matrix $outfile $i $j
  done
done