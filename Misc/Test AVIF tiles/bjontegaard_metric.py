import numpy as np
import scipy.interpolate
import sys
import csv
import pprint
from itertools import combinations

def BD_PSNR(R1, PSNR1, R2, PSNR2, piecewise=0):
    lR1 = np.log(R1)
    lR2 = np.log(R2)

    p1 = np.polyfit(lR1, PSNR1, 3)
    p2 = np.polyfit(lR2, PSNR2, 3)

    # integration interval
    min_int = max(min(lR1), min(lR2))
    max_int = min(max(lR1), max(lR2))

    # find integral
    if piecewise == 0:
        p_int1 = np.polyint(p1)
        p_int2 = np.polyint(p2)

        int1 = np.polyval(p_int1, max_int) - np.polyval(p_int1, min_int)
        int2 = np.polyval(p_int2, max_int) - np.polyval(p_int2, min_int)
    else:
        # See https://chromium.googlesource.com/webm/contributor-guide/+/master/scripts/visual_metrics.py
        lin = np.linspace(min_int, max_int, num=100, retstep=True)
        interval = lin[1]
        samples = lin[0]
        v1 = scipy.interpolate.pchip_interpolate(np.sort(lR1), np.sort(PSNR1), samples)
        v2 = scipy.interpolate.pchip_interpolate(np.sort(lR2), np.sort(PSNR2), samples)
        # Calculate the integral using the trapezoid method on the samples.
        int1 = np.trapz(v1, dx=interval)
        int2 = np.trapz(v2, dx=interval)

    # find avg diff
    avg_diff = (int2-int1)/(max_int-min_int)

    return avg_diff


def BD_RATE(R1, PSNR1, R2, PSNR2, piecewise=0):
    lR1 = np.log(R1)
    lR2 = np.log(R2)

    # rate method
    p1 = np.polyfit(PSNR1, lR1, 3)
    p2 = np.polyfit(PSNR2, lR2, 3)

    # integration interval
    min_int = max(min(PSNR1), min(PSNR2))
    max_int = min(max(PSNR1), max(PSNR2))

    # find integral
    if piecewise == 0:
        p_int1 = np.polyint(p1)
        p_int2 = np.polyint(p2)

        int1 = np.polyval(p_int1, max_int) - np.polyval(p_int1, min_int)
        int2 = np.polyval(p_int2, max_int) - np.polyval(p_int2, min_int)
    else:
        lin = np.linspace(min_int, max_int, num=100, retstep=True)
        interval = lin[1]
        samples = lin[0]
        v1 = scipy.interpolate.pchip_interpolate(np.sort(PSNR1), np.sort(lR1), samples)
        v2 = scipy.interpolate.pchip_interpolate(np.sort(PSNR2), np.sort(lR2), samples)
        # Calculate the integral using the trapezoid method on the samples.
        int1 = np.trapz(v1, dx=interval)
        int2 = np.trapz(v2, dx=interval)

    # find avg diff
    avg_exp_diff = (int2-int1)/(max_int-min_int)
    avg_diff = (np.exp(avg_exp_diff)-1)*100
    return round(avg_diff, 3)



if __name__ == "__main__":

    data = []
    pp = pprint.PrettyPrinter(indent=4)
    pp = pp.pprint

    fields = ("ID","SRC","FMT","SIZE","PSNR","SSIM","DSSIM","SSIMULACRA","BUTTERAUGLI","BUTTERAUGLI_3NORM","VMAF","ENCTIME","DECTIME","S_MINQ","S_MAXQ","S_SPEED","S_COLRANGE","S_TILEC","S_TILER","S_YUV","S_DEPTH","S_TUNE","S_AQMODE")

    files = sys.argv[1:]
    for f in files:
        with open(f) as fl:
            csv_reader = csv.reader(fl, delimiter='|')
            for x in csv_reader:
                data.append(dict([n for n in zip(fields, x)]))

    grouped = [[x for x in data
            if int(x.get("S_TILEC")) == tc
            and int(x.get("S_TILER")) == tr]
            for tc,tr in [(x,y)
                for x in range(6)
                for y in range(6)]]

    for fl in set([x.get("SRC") for x in data]):

        print('File: ', fl)

        for tile in grouped[1:]:
            print('Tile Column:      ', tile[0].get('S_TILEC'))
            print('Tile Row:         ',tile[0].get("S_TILER"))
            for metric in "PSNR", "SSIM", "DSSIM", "SSIMULACRA", "BUTTERAUGLI", "BUTTERAUGLI_3NORM", "VMAF":

                reference = [ x for x in grouped[0]
                            if x.get("SRC") == fl]

                reference_data = [(x.get(metric), x.get("SIZE"))
                            for x in reference]

                tiles = [x for x in tile
                        if x.get("SRC") == fl]

                tiles_data = [(x.get(metric), x.get("SIZE"))
                    for x in tiles]

                print(metric, f": {' ' * (17 - len(metric)) }" ,BD_RATE(
                    [float(x[1]) for x in reference_data],
                    [float(x[0]) for x in reference_data],
                    [float(x[1]) for x in tiles_data],
                    [float(x[0]) for x in tiles_data],
                    ),'%', sep='')
            time_dif_enc = sum([float(x.get("ENCTIME")) for x in tiles])/ \
                       sum([float(x.get("ENCTIME")) for x in reference])

            time_dif_dec = sum([float(x.get("DECTIME")) for x in tiles])/ \
                       sum([float(x.get("DECTIME")) for x in reference])
            print('Enc time:          ', round(time_dif_enc * 100, 1), "%", sep='')
            print('Dec time:          ', round(time_dif_dec * 100, 1), "%", sep='')
            print()

