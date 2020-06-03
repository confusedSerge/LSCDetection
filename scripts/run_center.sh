matrix=$1
outfileCenter=test_out/center/center_out
outfileCenterL=test_out/center/center_out_with_l

targets=testsets/wordsim/targets.tsv
gold=testsets/wordsim/gold.tsv
outfileCD=outfileCD.tsv

mkdir -p "test_out/center"

py postprocessing/center.py $matrix $outfileCenter

py measures/cd.py $targets $outfileCenter $outfileCenter $outfileCD
output=$(py evaluation/spr.py $outfileCD $gold $matrix gold 1 0 | grep "gold")

IFS=$'\t' read -ra my_array <<< $output

echo "0;${my_array[2]}" >> test_out/center/center_out_results.csv

py postprocessing/center.py -l $matrix $outfileCenterL

py measures/cd.py $targets outfileCenterL outfileCenterL $outfileCD
output=$(py evaluation/spr.py $outfileCD $gold $matrix gold 1 0 | grep "gold")

IFS=$'\t' read -ra my_array <<< $output

echo "1;${my_array[2]}" >> test_out/center/center_out_results.csv