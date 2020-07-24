#!/bin/bash
matrix=$1
corp=$2

dir=$(dirname $matrix)

awk '{if(NR>1)print $1=$1}' $matrix >> $dir/tmp
python3.7 measures/freq.py $dir/tmp $corp $dir/tmp_trg_freq
# awk '{if($2>=700)print $1=$1}' $dir/tmp_trg_freq >> $dir/new_targets.tsv

rm -f $dir/tmp
rm -f $dir/tmp_trg_freq

