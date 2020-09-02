out=$1
path1=$2
path2=$3
path3=$4
title=$5

mkdir -p $out/$title

label=(diachron_all diachron_low_c1 diachron_low_c2 diachron_high_c1 diachron_high_c2 wordsim_all_c1 wordsim_all_c2 wordsim_low_c1 wordsim_low_c2 wordsim_high_c1 wordsim_high_c2 frequency_c1 frequency_c2 frequency_d isotropy1 isotropy2 len_centroid_1 len_centroid_2)

for i in "${label[@]}"
do
    echo "$i"
    if [ "$path3" = "0" ]; then
        python3.8 postprocessing/plot.py -z $out/$title/$i.png $path1/$i.csv $path2/$i.csv $title name1 name2 "pca components" "$i"
    else
        python3.8 postprocessing/plot.py -z -t $out/$title/$i.png $path1/$i.csv $path2/$i.csv $path3/$i.csv $title "stacked" "unstacked" "pca components" "$i"
    fi
done