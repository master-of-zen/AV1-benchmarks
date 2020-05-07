#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import matplotlib
import statistics
from ast import literal_eval as make_tuple
from scipy import interpolate
import numpy as np



# AOMS

plt.plot([], [], ' ', label='Nature footage downscaled from 4k, 1920*1080 Frames: 180, \n\nAOM git 06.05.2020 CQ range: cq 20-55, step 5')
with open('aom_git_nature.mkvdata.txt', 'r') as f:
        data = make_tuple(f.read())

dt = []

cmap = plt.get_cmap('Purples')
colors = list(cmap(np.linspace(0.4,0.8, len(set([x[2] for x in data])))))
for cpu in sorted(set([x[2] for x in data])):

    dt = [x for x in data if x[2] == cpu]
    x = sorted([x[4] for x in dt])
    y = sorted([x[5] for x in dt])
    time = sum([x[1] for x in dt])/len(dt)
    f = interpolate.interp1d(x, y, kind='cubic')
    xnew = np.linspace(min(x), max(x), max(x) - min(x) )
    plt.plot(xnew, f(xnew), label=f'Aom {cpu}, Average Time: {round(time)}', linewidth=3, c=colors.pop())

# Rav1e
plt.plot([], [], ' ', label='Rav1e git 06.05.2020 Quantizer range: 50-150, step 5')
with open('rav1e_nature.mkvdata.txt') as f:
    rav1e = make_tuple(f.read())

cmap = plt.get_cmap('Oranges')
colors1 = list(cmap(np.linspace(0.3,0.7, len(set([x[2] for x in rav1e])))))
for speed in sorted(set([x[2] for x in rav1e])):
    ks = [x for x in rav1e if x[2] == speed]
    x = sorted([x[4] for x in ks])
    y = sorted(x[5] for x in ks)
    time = sum(x[1] for x in ks)/len(x)
    f = interpolate.interp1d(x, y, kind='cubic')
    xnew = np.linspace(min(x), max(x), max(x) - min(x) )
    plt.plot(xnew, f(xnew), label=f'Rav1e {speed}, Average Time: {round(time)}',linestyle='dashed',linewidth=3, c=colors1.pop())

# x265
plt.plot([], [], ' ', label='FFmpeg 06.05.2020 x265: CRF range: 41 - 20, step 3')
with open('x265_nature.mkvdata.txt') as f:
    x265 = make_tuple(f.read())

speeds = (('ultrafast', 0), ('superfast', 1), ('veryfast', 2), ('faster', 3), ('fast', 4), ('medium', 5), ('slow', 6), ('slower', 7), ('veryslow', 8))


in_file = set([x[2] for x in x265])
speeds = reversed([x for x in speeds if x[0] in in_file])

cmap = plt.get_cmap('Greens')
colors2 = list(cmap(np.linspace(0.4,0.9, len(in_file))))


for speed, _ in speeds:
    ks = [x for x in x265 if x[2] == speed]
    x = sorted([x[4] for x in ks])
    y = sorted(x[5] for x in ks)
    time = sum(x[1] for x in ks)/len(x)
    f = interpolate.interp1d(x, y, kind='cubic')
    xnew = np.linspace(min(x), max(x), max(x) - min(x) )
    plt.plot(xnew, f(xnew), label=f'X265 {speed}, Average Time: {round(time)}',linestyle='-.', linewidth=3, c=colors2.pop())

# Plot
plt.tight_layout()
plt.xticks([x for x in range(0, 10000, 100)])
plt.yticks([x for x in range(30, 100, 1)])
[plt.axvline(i, color='grey', linewidth=0.3) for i in range(0, 4000, 100)]
[plt.axhline(i, color='grey', linewidth=0.5) for i in range(21, 100, 2)]
[plt.axhline(i, color='black', linewidth=1) for i in range(22, 100, 2)]
plt.ylabel('Vmaf', size=20)
plt.xlabel('Bitrate', size=20)
plt.title('AOM vs Rav1e vs x265 ', size=30)
plt.legend(prop={'size': 20}, loc="lower right")
plt.xlim(100, 3000)
plt.ylim((80, 100))
plt.show()
