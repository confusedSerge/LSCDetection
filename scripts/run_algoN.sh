matrix=$1
threshold_min=$2
threshold_max=$3
dim_red_min=$4
dim_red_max=$5

# for matrix in $path_to_files/*
# do
for ((i= $threshold_min; i<=$threshold_max; i++))
do
  for ((j= $dim_red_min; j<=$dim_red_max; j++))
  do
    mkdir -p "test_out/algo_n/algo_n_${matrix##*/}"
    outfile=test_out/algo_n/algo_n_${matrix##*/}/algo_n_${matrix##*/}\_$i\_$j

    echo "started with ${matrix##*/} and values thresh: $i, dim_red: $j"
    # echo "outfile will be"

    python3.7 postprocessing/algo_n.py $matrix $outfile $i $j
  done
done
# done