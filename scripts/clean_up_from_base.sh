matrix=$1
dim=$2

sed -i 's/\s/;/g' $matrix

IFS=";" read -ra line <<< $(head -n 1 $matrix)

path=$(dirname $matrix)
name=$(basename $matrix ".csv")
outfile=$path/$name\_cleaned.csv

for ((c=0; c<=25; c++))
do
    len=${#line[@]}
	echo "$dim;$c;${line[@]:1:len}" >> $outfile
done 

sed -i 's/\s/;/g' $outfile
sed -i 's/[-+]0.000000j//g' $outfile 

bash -e scripts/mkres.sh $outfile
mv $matrix $path/$name\_cleaned/
mv $outfile $path/$name\_cleaned/