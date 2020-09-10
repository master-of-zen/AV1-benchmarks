#!/bin/bash
for cpu in faster
do
    for i in 40 35 30 25
    do
        runtime=`vvencapp -i ${1} --size 1920x1080 --format yuv420_10 --output vvc${i}_${cpu}.vvc --preset ${cpu} --qp ${i} --threads 12`
        decode=`vvdecapp -b vvc${i}_${cpu}.vvc -o vvc${i}_${cpu}.yuv`
        vmaf=`ffmpeg -r 60 -s 1920x1080 -pix_fmt yuv420p10le -i vvc${i}_${cpu}.yuv -r 60 -s 1920x1080 -pix_fmt yuv420p10le -i ${1} -filter_complex libvmaf=eof_action=endall:psnr=1:ssim=1:ms_ssim=1:log_path=${i}_${c}.json:log_fmt=json -f null - `

        vmaf=`jq '.["VMAF score"]'  ${i}_${c}.json`
        psnr=`jq '.["PSNR score"]'  ${i}_${c}.json`
        ssim=`jq '.["SSIM score"]'  ${i}_${c}.json`
        ms_ssim=`jq '.["MS-SSIM score"]'  ${i}_${c}.json`

        bittime=$(echo "$runtime" | awk '/Bitrate/{getline; print $3};/Total Time/{print $3}')
        bitrate=$(echo "$bittime" | head -n 1)
        runtime=$(echo "$bittime" | tail -n 1)
        output="('vvc', $runtime, '$cpu', $i, $bitrate, $vmaf, $psnr, $ssim, $ms_ssim),"
        echo $output
        echo -n $output >> vvc_${1}data.txt
done
done
