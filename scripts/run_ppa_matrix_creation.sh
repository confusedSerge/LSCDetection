src_matrix=$1

out_path=test_out/exmpl_mtrx
out_name=$(basename $src_matrix)

mkdir -p $out_path


for i in 0 1 5 10 15 20 25
do
    echo "$i"
    outfile_ppa=$out_path/$out_name\_$i
    outfile_ppa_wo_mc=$out_path/$out_name\_$i\_wo_mc

    python3.8 postprocessing/ppa.py $src_matrix $outfile_ppa $i

    # ppa without mean centering
    python3.8 postprocessing/ppa_wo_mc.py $src_matrix $outfile_ppa_wo_mc $i
done