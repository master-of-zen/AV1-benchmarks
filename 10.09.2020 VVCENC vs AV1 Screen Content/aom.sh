#!/bin/bash
for cpu in 6
do
    for i in 50 40 30 20
    do
        runtime=`av1an.py -fmt yuv420p10le -p 1 -s 0 -i ${1} -v " -b 10 --threads=12 --end-usage=q --cq-level=$i --cpu-used=$cpu " -o aom${i}_${c} | grep Finished | cut -d' ' -f2 | tr -d '[[:alpha:]]'`
        vmaf=`ffmpeg -r 60 -i aom${i}_${c}.mkv -r 60 -i ${1} -filter_complex libvmaf=psnr=1:ssim=1:ms_ssim=1:log_path=${i}_${c}.json:log_fmt=json -f null - `

        vmaf=`jq '.["VMAF score"]'  ${i}_${c}.json`
        psnr=`jq '.["PSNR score"]'  ${i}_${c}.json`
        ssim=`jq '.["SSIM score"]'  ${i}_${c}.json`
        ms_ssim=`jq '.["MS-SSIM score"]'  ${i}_${c}.json`

        bitrate=`ffprobe -i aom${i}_${c}.mkv 2>&1 | grep bitrate | rev | cut -d' ' -f2 | rev`
        output="('aom', $runtime, $cpu, $i, $bitrate, $vmaf, $psnr, $ssim, $ms_ssim),"
        eoutput=""
        printf "('aom', %s, %s, %d, %s, %s, %s, %s, %s)," "$runtime" "$cpu" "$i" "$bitrate" "$vmaf" "$psnr" "$ssim" "$ms_ssim" | tee -a "aom_${1}data.txt"
        echo
done
done
