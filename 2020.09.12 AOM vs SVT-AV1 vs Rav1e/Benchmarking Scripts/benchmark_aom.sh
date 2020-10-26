j=0

for cpu in 4 ; do
    for i in 63 55 48 40 32 24 ; do
        temp_folder=folder-$j
cat <<EOF
        runtime=\$(av1an  -p 2 -s 0 -i "${1}" -v " --threads=12 --end-usage=q --cq-level=$i --cpu-used=${cpu} " --temp aom${cpu}_${i} -o "aom${cpu}_${i}" | grep Finished | cut -d' ' -f2 | tr -d '[:alpha:]'); \
        ffmpeg -nostdin -r 60 -i "aom${cpu}_${i}.mkv" -r 60 -i "${1}" -filter_complex "libvmaf=psnr=1:ssim=1:ms_ssim=1:log_path=${i}_${j}.json:log_fmt=json" -f null - 2> /dev/null; \
        printf "('%s', %s, %s, %s, %s, %s, %s, %s, %s)," \
            "default" \
            "\$runtime" \
            "${cpu}" \
            "$i" \
            "\$(ffprobe -i aom${cpu}_${i}.mkv 2>&1 | grep bitrate | rev | cut -d' ' -f2 | rev)" \
            "\$(jq '.["VMAF score"]' ${i}_${j}.json)" \
            "\$(jq '.["PSNR score"]' ${i}_${j}.json)" \
            "\$(jq '.["SSIM score"]' ${i}_${j}.json)" \
            "\$(jq '.["MS-SSIM score"]' ${i}_${j}.json)" | \
            tee -a "aom_data.txt"; \
        echo
EOF
        j=$((j + 1))
    done
done | parallel -u -j 4
