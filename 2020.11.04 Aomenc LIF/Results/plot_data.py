 #!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import matplotlib
import statistics
import sys
from ast import literal_eval
from scipy import interpolate
import numpy as np

def plot_range(data, color, encoder, m_place):
    cpus = list(set([x[2] for x in data]))
    if encoder.lower() == 'vvc':
        cpus = sorted(cpus, key=lambda x: int(x))
    cmap = plt.get_cmap(color)
    colors = list(cmap(np.linspace(0, 1, len(set([x[2] for x in data])))))
    for cpu in cpus:
        dt = [x for x in data if x[2] == cpu]
        x = sorted([round(x[4])for x in dt])
        y = sorted([x[m_place] for x in dt])
        time = sum([x[1] for x in dt])/len(dt)
        f = interpolate.interp1d(x, y, kind='quadratic')
        xnew = np.linspace(min(x), max(x), max(x) - min(x) )
        plt.plot(xnew, f(xnew), label=f'{encoder} {cpu}, Average Time: {round(time)}', linewidth=3, c=colors.pop())

def vvc_sort(x):
    d = ['slow', 'medium', 'fast', 'faster']
    return d.index(x)


if __name__ == "__main__":

    files = sys.argv[1:]
    data = []

    for file in files:
        with open(file) as f:
            dt = literal_eval(f.readline())

            data.extend(dt)

    vvc_data = [x for x in data if x[0] == 'vvc']

    codecs = sorted(list(set([x[0] for x in data])))
    codecs = [x.upper() for x in codecs]
    for metric, place in [('VMAF', 5), ('PSNR', 6), ('SSIM', 7), ('MS-SSIM', 8)]:

        plt.plot([], [], ' ', label='Xiph 1080p 50fps Camera footage "park_joy"\n500 frames')
        plot_range(vvc_data, 'plasma', 'VVC', place)
        # Plot

        plt.xticks([x for x in range(0, 40000, 1000)], [int(x) for x in range(0, 40) ],fontsize=26)

        if metric in ('VMAF', 'PSNR'):
            plt.yticks([x for x in range(0, 101, 1)], fontsize =28)
            [plt.axhline(i, color='grey', linewidth=0.5) for i in range(1, 100, 2)]
            [plt.axhline(i, color='black', linewidth=1) for i in range(0, 100, 2)]
        else:
            [plt.axhline(i/100, color='grey', linewidth=0.5) for i in range(61, 1000, 2)]
            [plt.axhline(i/100, color='black', linewidth=1) for i in range(62, 1000, 2)]
            plt.yticks([x/100 for x in range(0, 1000, 1)], fontsize =28)


        [plt.axvline(i, color='grey', linewidth=0.3) for i in range(0, 40000, 500)]
        plt.ylabel(metric.capitalize(), size=32)
        plt.xlabel('Bit rate, Mbps', size=24)
        plt.title(f"{' vs '.join(codecs)}, 0.1.0 26.09.2020 {metric}", size=28)
        plt.legend(prop={'size': 19}, loc="lower right")

        #if metric in ('VMAF', 'PSNR'):
        low_ylim = [x[place] for x in data]
        low_ylim = np.percentile(low_ylim, 15)

        bitrates = [x[4] for x in data]
        plt.xlim(int(np.percentile(bitrates, 15)), int(np.percentile(bitrates, 75)))

        high_ylim = 100 if metric in ('VMAF') else max([x[place] for x in data])

        plt.ylim((low_ylim, high_ylim))
        plt.margins(0)
        plt.subplots_adjust(left=0.045, right=0.99, top=0.965, bottom=0.065)
        plt.show()

