language=$1
pretrain=$2

IFS='-'
read -ra arr <<< $pretrain 

path=test_src/$language/${arr[0]}${arr[1]}/corp1

matrixs=($path/*-${arr[0]})
for matrix in "${matrixs[@]}"
do
  matrix1=$matrix
  matrix2=${matrix1/corp1/corp2}
  matrix2VI=${matrix2/-${arr[0]}/-${arr[1]}}

  bash -e scripts/run_quick_stacked.sh "$matrix1" "$matrix2VI" "${arr[0]}${arr[1]}" $language
  bash -e scripts/run_quick_unstacked.sh "$matrix1" "$matrix2VI" "${arr[0]}${arr[1]}" $language
done