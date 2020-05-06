#!/bin/bash
for c in 5 4 3 2
do
    for i in 60 55 50 45 40 35 30 25 20
    do
        runtime=`av1an.py -tr 30 -s ${1}.csv -i ${1} -v " --threads=12 --end-usage=q --cq-level=$i --cpu-used=$c " -o aom${i}_${c} | grep Finished | cut -d' ' -f2 | tr -d '[[:alpha:]]'`
        vmaf=`ffmpeg -i aom${i}_${c}.mkv -i ${1} -filter_complex libvmaf -f null - 2>&1 | grep "VMAF score" | tr ' ' '\n' | tail -n1`
        bitrate=`ffprobe -i aom${i}_${c}.mkv 2>&1 | grep bitrate | rev | cut -d' ' -f2 | rev`
        output="('aom', $runtime, $c, $i, $bitrate, $vmaf), "
        echo $output
        echo -n $output >> aom_${1}data.txt
done
done
