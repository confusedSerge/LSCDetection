matrix=$1
out_name=$2
threshold_min=$3
threshold_max=$4
dim_red_min=$5
dim_red_max=$6

mkdir -p "test_out/algo_n_$out_name"

# for matrix in $path_to_files/*
# do
for ((i= $threshold_min; i<=$threshold_max; i++))
do
  for ((j= $dim_red_min; j<=$dim_red_max; j++))
  do
    outfile=test_out/algo_n_$out_name/algo_n_$out_name\_thresh$i\_dim$j

    echo "started with $matrix and values thresh: $i, dim_red: $j"
    # echo "outfile will be"

    python3.7 postprocessing/algo_n.py $matrix $outfile $i $j
  done
done
# done