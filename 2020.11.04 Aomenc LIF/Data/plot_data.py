 #!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import matplotlib
import statistics
import sys
from ast import literal_eval
from scipy import interpolate
import os
import json
import re
import numpy
import pprint
import math


def bdsnr(metric_set1, metric_set2):
  rate1 = [x[0] for x in metric_set1]
  psnr1 = [x[1] for x in metric_set1]
  rate2 = [x[0] for x in metric_set2]
  psnr2 = [x[1] for x in metric_set2]

  log_rate1 = list(map(math.log, rate1))
  log_rate2 = list(map(math.log, rate2))

  # Best cubic poly fit for graph represented by log_ratex, psrn_x.
  poly1 = numpy.polyfit(log_rate1, psnr1, 3)
  poly2 = numpy.polyfit(log_rate2, psnr2, 3)

  # Integration interval.
  min_int = max([min(log_rate1), min(log_rate2)])
  max_int = min([max(log_rate1), max(log_rate2)])

  # Integrate poly1, and poly2.
  p_int1 = numpy.polyint(poly1)
  p_int2 = numpy.polyint(poly2)

  # Calculate the integrated value over the interval we care about.
  int1 = numpy.polyval(p_int1, max_int) - numpy.polyval(p_int1, min_int)
  int2 = numpy.polyval(p_int2, max_int) - numpy.polyval(p_int2, min_int)

  # Calculate the average improvement.
  if max_int != min_int:
    avg_diff = (int2 - int1) / (max_int - min_int)
  else:
    avg_diff = 0.0
  return avg_diff


def bdrate(metric_set1, metric_set2):
  rate1 = [x[0] for x in metric_set1]
  psnr1 = [x[1] for x in metric_set1]
  rate2 = [x[0] for x in metric_set2]
  psnr2 = [x[1] for x in metric_set2]

  log_rate1 = list(map(math.log, rate1))
  log_rate2 = list(map(math.log, rate2))

  # Best cubic poly fit for graph represented by log_ratex, psrn_x.
  poly1 = numpy.polyfit(psnr1, log_rate1, 3)
  poly2 = numpy.polyfit(psnr2, log_rate2, 3)

  # Integration interval.
  min_int = max([min(psnr1), min(psnr2)])
  max_int = min([max(psnr1), max(psnr2)])

  # find integral
  p_int1 = numpy.polyint(poly1)
  p_int2 = numpy.polyint(poly2)

  # Calculate the integrated value over the interval we care about.
  int1 = numpy.polyval(p_int1, max_int) - numpy.polyval(p_int1, min_int)
  int2 = numpy.polyval(p_int2, max_int) - numpy.polyval(p_int2, min_int)

  # Calculate the average improvement.
  avg_exp_diff = (int2 - int1) / (max_int - min_int)

  # In really bad formed data the exponent can grow too large.
  # clamp it.
  if avg_exp_diff > 200:
    avg_exp_diff = 200

  # Convert to a percentage.
  avg_diff = (math.exp(avg_exp_diff) - 1) * 100

  return avg_diff

def bd_sort(data, c1, p1, c2, p2):

    #Vmaf
    vmaf0 = [(x[4],x[5]) for x in data if x[2] == p1 and x[0] == c1  ]
    vmaf1 = [(x[4],x[5]) for x in data if x[2] == p2 and x[0] == c2  ]

    #PSNR
    psnr0 = [(x[4],x[6], 3) for x in data if x[2] == p1 and x[0] == c1 ]
    psnr1 = [(x[4],x[6], 3) for x in data if x[2] == p2 and x[0] == c2 ]

    # SSIM
    ssim0 = [(x[4],x[7]) for x in data if x[2] == p1 and x[0] == c1 ]
    ssim1 = [(x[4],x[7]) for x in data if x[2] == p2 and x[0] == c2 ]

    # MS-SSIM
    mssim0 = [(x[4],x[8]) for x in data if x[2] == p1 and x[0] == c1 ]
    mssim1 = [(x[4],x[8]) for x in data if x[2] == p2 and x[0] == c2 ]

    time0 = [x[1] for x in data if x[2] == p1 and x[0] == c1 ]
    time1 = [x[1] for x in data if x[2] == p2 and x[0] == c2 ]
    mean = sum(time0) / sum(time1)
    mean_time = ( mean -1) * 100
    bd1 = round(bdrate(vmaf1, vmaf0), 3)
    bd2 = round(bdrate(psnr1, psnr0), 3 )
    bd3 = round(bdrate(ssim1, ssim0), 3 )
    bd4 = round(bdrate(mssim1, mssim0), 3)

    # ssim aand ms-ssim weight changed to avoid locking
    summary = bd1  + bd2 + bd3 * 1.1 + bd4 * 1.1
    print(c1, p1, c2, p2, summary)

    return 0 <= summary * 100


def compare_bd(d1, d2):

    print(f'ff', '\n')

    #Vmaf
    vmaf0 = [(x.get('vmaf'), x.get('bitrate')) for x in d1 if d1[0].get('vmaf')]
    vmaf1 = [(x.get('vmaf'), x.get('bitrate')) for x in d2 if d2[0].get('vmaf')]

    print(vmaf0, vmaf1)
    #PSNR
    psnr0 = [(x[4],x[6], 3) for x in data if x[2] == p1 and x[0] == c1 ]
    psnr1 = [(x[4],x[6], 3) for x in data if x[2] == p2 and x[0] == c2 ]

    # SSIM
    ssim0 = [(x[4],x[7]) for x in data if x[2] == p1 and x[0] == c1 ]
    ssim1 = [(x[4],x[7]) for x in data if x[2] == p2 and x[0] == c2 ]

    # MS-SSIM
    mssim0 = [(x[4],x[8]) for x in data if x[2] == p1 and x[0] == c1 ]
    mssim1 = [(x[4],x[8]) for x in data if x[2] == p2 and x[0] == c2 ]

    print('Vmaf    BD rate:', round(bdrate(vmaf1, vmaf0), 3),'%')
    print('PSNR    BD rate:', round(bdrate(psnr1, psnr0), 3 ),'%')
    print('SSIM    BD rate:', round(bdrate(ssim1, ssim0), 3 ),'%')
    print('MS-SSIM BD rate:', round(bdrate(mssim1, mssim0), 3),'%')

    time0 = [x[1] for x in data if x[2] == p1 and x[0] == c1 ]
    time1 = [x[1] for x in data if x[2] == p2 and x[0] == c2 ]
    mean = sum(time0) / sum(time1)
    mean_time = round(( mean -1) * 100, 1)
    mean_time = f'+{mean_time} %' if mean_time > 0 \
            else f'{mean_time} %'
    print('\n')


def plot_range(data, metric, color='Blues' ):
    x = sorted([x.get('bitrate') for x in data])
    y = sorted([x.get(metric) for x in data])

    f = interpolate.interp1d(x, y, kind='quadratic')
    xnew = numpy.linspace(min(x), max(x), max(x) - min(x) )
    plt.plot(xnew, f(xnew), label=f'{data[0].get("lif")}', linewidth=3)

if __name__ == "__main__":

    data = []


    # Read Data
    for subdir, dirs, files in os.walk(os.getcwd()):
        for filename in files:
            filepath = subdir + os.sep + filename

            if filepath.endswith(".json"):
                dt = filepath.split('_')
                cq = int(re.findall(r'\d+', dt[-2])[0])
                lif = int(re.findall(r'\d+', dt[-1])[0])

                with open(filepath, 'r') as js:
                    test = json.load(js)
                    mean_vmaf = numpy.mean([x.get('vmaf') for x in test['vmaf']])
                    mean_psnr = numpy.mean([x.get('psnr_avg') for x in test['psnr']])
                    mean_ssim = numpy.mean([x.get('ssim_avg') for x in test['ssim']])
                    mean_ms_ssim = numpy.mean([x.get('ms_ssim') for x in test['vmaf']])

                txt = os.path.splitext(filepath)[0]+'.txt'
                with open(txt) as iwanttodie:
                    bitrate = int(iwanttodie.read())

                point = {
                        'cq' : cq,
                        'lif': lif,
                        'bitrate': bitrate,
                        'vmaf': mean_vmaf,
                        'psnr': mean_psnr,
                        'ssim': mean_ssim,
                        'ms_ssim': mean_ms_ssim,
                        }

                data.append(point)

    # Sort Data
    sorted_data = []

    for i in range(15, 36):
        pack = []
        for x in data:
            if x.get('lif') == i:
                pack.append(x)
        sorted_data.append(pack)

    sorted_lif = sorted(sorted_data, key=lambda x: x[0].get('lif'))
    to_compare = zip(sorted_lif, sorted_lif.pop(0))

 #   for x,y in to_compare:
  #      bdrate(x, y)


    for metric in [ 'vmaf','psnr', 'ssim', 'ms_ssim']:

        plt.plot([], [], ' ', label='Xiph SVT 1080p 50fps Camera footage "Ducks Get Off"\n500 frames')
        for x  in sorted_data:
            plot_range(x, metric)

        # Plot

        plt.xticks([x for x in range(0, 50000, 1000)], [int(x) for x in range(0, 50) ],fontsize=26)

        if metric in ('vmaf', 'psnr'):
            plt.yticks([x for x in range(0, 101, 1)], fontsize =28)
            [plt.axhline(i, color='grey', linewidth=0.5) for i in range(1, 100, 2)]
            [plt.axhline(i, color='black', linewidth=1) for i in range(0, 100, 2)]
        else:
            [plt.axhline(i/100, color='grey', linewidth=0.5) for i in range(61, 1000, 2)]
            [plt.axhline(i/100, color='black', linewidth=1) for i in range(62, 1000, 2)]
            plt.yticks([x/100 for x in range(0, 1000, 1)], fontsize =28)


        [plt.axvline(i, color='grey', linewidth=0.3) for i in range(0, 60000, 500)]
        plt.ylabel(metric.capitalize(), size=32)
        plt.xlabel('Bit rate, Mbps', size=24)
        plt.title(f"Aomenc lag-in-frames, latest git 04.11.2020 {metric}", size=28)
        plt.legend(prop={'size': 19}, loc="lower right")

        if metric in 'vmaf':
            low_ylim = 90
        if metric in 'psnr':
            low_ylim = 30
        if metric in ('ssim', 'ms_ssim'):
            low_ylim = 0.99
        plt.xlim(20000, 50000)

        high_ylim = 100 if metric in ('vmaf') else 50 if metric in ('psnr') else 1

        plt.ylim((low_ylim, high_ylim))
        plt.margins(0)
        plt.subplots_adjust(left=0.045, right=0.99, top=0.965, bottom=0.065)
        plt.show()

