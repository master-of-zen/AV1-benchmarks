#!/bin/bash
for c in  ultrafast superfast veryfast faster fast medium slow slower veryslow
do
    for i in 41 38 35 32 29 26 23
    do
        start=`date +%s`
        runtime=`time ffmpeg -y  -i ${1} -c:v libx265 -crf ${i} -preset ${c} x265${1}_${c}_${i}.mkv`
        end=`date +%s`
        runtime=$((end-start))
        vmaf=`ffmpeg -i x265${1}_${c}_${i}.mkv -i ${1} -filter_complex libvmaf -f null - 2>&1 | grep "VMAF score" | tr ' ' '\n' | tail -n1`
        bitrate=`ffprobe -i x265${1}_${c}_${i}.mkv 2>&1 | grep bitrate | rev | cut -d' ' -f2 | rev`
        output="('x265', $runtime, '$c', $i, $bitrate, $vmaf), "
        echo $output
        echo -n $output >> x265_${1}data.txt
done
done
