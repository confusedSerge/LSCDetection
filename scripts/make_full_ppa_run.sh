path_to_files=$1

echo "started"

for file in $path_to_files/*
do
    echo "started with file $file"
    bash -e run_ppa.sh $file 0 25 sdewac_sgns_$file
done