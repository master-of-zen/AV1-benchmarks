#!/bin/bash
for c in 10 9 8 7 6 5 4 3 2 1 0
do
    for i in 150 125 100 75 50
    do
        runtime=`av1an.py -tr 30 -enc rav1e -s ${1}.csv -i ${1} -v " --threads 12 --quantizer ${i} -s ${c} " -o rav1e${i}_${c} | grep Finished | cut -d' ' -f2 | tr -d '[[:alpha:]]'`
        vmaf=`ffmpeg -i rav1e${i}_${c}.mkv -i ${1} -filter_complex libvmaf -f null - 2>&1 | grep "VMAF score" | tr ' ' '\n' | tail -n1`
        bitrate=`ffprobe -i rav1e${i}_${c}.mkv 2>&1 | grep bitrate | rev | cut -d' ' -f2 | rev`
        echo $runtime, $bitrate, $vmaf
        echo -n "('rav1e', $runtime, $c, $i, $bitrate, $vmaf)," >> rav1e_${1}data.txt
done
done

