matrix=$1
outfileCenter=test_out/center/center_out
outfileCenterL=test_out/center/center_out_with_l

mkdir -p "test_out/center"

py postprocessing/center.py $matrix $outfileCenter
py postprocessing/center.py -l $matrix $outfileCenterL