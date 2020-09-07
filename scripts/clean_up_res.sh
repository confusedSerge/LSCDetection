matrix=$1
dim=$2

sed -i 's/\s/;/g' $matrix

path=$(dirname $matrix)
name=$(basename $matrix ".csv")
outfile=$path/$name\_cleaned.csv
c=0

while IFS=";" read -ra line
do
    len=${#line[@]}
	echo "$dim;$c;${line[@]:2:len}" >> $outfile
    ((c=c+1))
done <"$matrix"

sed -i 's/\s/;/g' $outfile
sed -i 's/[-+]0.000000j//g' $outfile 

bash -e scripts/mkres_small.sh $outfile
mv $matrix $path/$name\_cleaned/
mv $outfile $path/$name\_cleaned/