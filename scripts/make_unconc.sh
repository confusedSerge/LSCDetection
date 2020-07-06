#!/bin/bash
matrix=$1
outfile_one=$2
outfile_two=$3

IFS=$' ' read -ra head <<< $(head -n 1 $matrix)

echo "${head[0]} ${head[2]} " >> $outfile_one
echo "${head[1]} ${head[2]} " >> $outfile_two

((maxline =${head[0]}+1))

sed -n 2,${maxline}p $matrix  >> $outfile_one\_tmp
awk '{print $1=substr($1, 1, length($1)-1)" " substr($0, index($0,$2))}' $outfile_one\_tmp >> $outfile_one
rm -f $outfile_one\_tmp

sed -n 1,${maxline}!p $matrix >> $outfile_two

