matrix=$1
threshold_min=$2
threshold_max=$3

mkdir -p "test_out/ppa"

for ((c=$threshold_min; c<=$threshold_max; c++))
do
  outfile=test_out/ppa/ppa_$c
  py postprocessing/ppa.py $matrix $outfile $c
done