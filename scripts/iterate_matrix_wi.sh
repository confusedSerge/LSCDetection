language=$1

path=test_src/$language/WI

matrixs=($path/*-WI)
for matrix in "${matrixs[@]}"
do
  bash -e scripts/run_quick_wi.sh $matrix WI $language
done