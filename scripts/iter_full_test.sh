lang=("GER")
comb=("VI-VI" "NO-VI" "OP-OP" "NO-NO" "WI")

for i in "${lang[@]}" 
do
    echo "$i"
    for j in "${comb[@]}"
    do
        if [ "$j" = "WI" ]; then
            bash -e scripts/iterate_matrix_wi.sh $i
        else
            bash -e scripts/iterate_matrix.sh $i $j
        fi
    done
done
