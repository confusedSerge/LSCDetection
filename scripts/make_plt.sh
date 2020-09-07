out=$1
path1=$2
path2=$3
path3=$4
title=$5

mkdir -p $out/$title

label=(wordsim frequency isotropy isotropy_norm len_centroid len_centroid_norm)

for i in "${label[@]}"
do
    echo "$i"
    if [ "$path3" = "0" ]; then
        python3.8 postprocessing/plot.py -z $out/$title/$i.png $path1/$i.csv $path2/$i.csv $title name1 name2 "pca components" "$i"
    else
        python3.8 postprocessing/plot.py -z -t $out/$title/$i.png $path1/$i.csv $path2/$i.csv $path3/$i.csv $title "with mean centering" "without" "pca components" "$i"
    fi
done