j=0

for cpu in 0 1 2 3 4 5 6 7 8; do
    for i in 63 58 53 48 43 38 ; do
        temp_folder=folder-$j
cat <<EOF
        runtime=\$(av1an -fmt yuv420p10le -enc svt_av1 -p 1 -s 0 -i "${1}" -v " --qp $i --preset $cpu " --temp svt${cpu}_${i} -o "svt${cpu}_${i}" | grep Finished | cut -d' ' -f2 | tr -d '[:alpha:]'); \
        ffmpeg -nostdin -r 60 -i "svt${cpu}_${i}.mkv" -r 60 -i "${1}" -filter_complex "libvmaf=psnr=1:ssim=1:ms_ssim=1:log_path=${i}_${j}.json:log_fmt=json" -f null - 2> /dev/null; \
        printf "('%s', %s, %s, %s, %s, %s, %s, %s, %s)," \
            "svt" \
            "\$runtime" \
            "${cpu}" \
            "$i" \
            "\$(ffprobe -i aom${cpu}_${i}.mkv 2>&1 | grep bitrate | rev | cut -d' ' -f2 | rev)" \
            "\$(jq '.["VMAF score"]' ${i}_${j}.json)" \
            "\$(jq '.["PSNR score"]' ${i}_${j}.json)" \
            "\$(jq '.["SSIM score"]' ${i}_${j}.json)" \
            "\$(jq '.["MS-SSIM score"]' ${i}_${j}.json)" | \
            tee -a "svt_data.txt"; \
        echo
EOF
        j=$((j + 1))
    done
done | parallel -u -j 4
