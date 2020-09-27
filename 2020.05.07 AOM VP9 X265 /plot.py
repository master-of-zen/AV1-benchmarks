#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import matplotlib
import statistics
from ast import literal_eval as make_tuple
from scipy import interpolate
import numpy as np

plt.plot([], [], ' ', label='Dota 2 xiph.org footage\n 1920*1080 Frames: 180, 6 different scenes')

# AV1
plt.plot([], [], ' ', label='AOM 06.05.2020 CQ range: cq 30-60, step 5')
with open('aom_dotatest.mkvdata.txt', 'r') as f:
        raw = f.read().split('),(')
        raw = [x for x in raw]
        d = raw[1:-1] + [raw[0][1:], raw[-1][:-2]]

data = []

for x in d:
    try:
        data.append(make_tuple('(' + x + ')'))
    except:
        print(x)


cmap = plt.get_cmap('Purples')
colors = list(cmap(np.linspace(0.4,0.8, len(set([x[2] for x in data])))))

cpus = sorted(set([x[2] for x in data]))

for cpu in cpus:
    dt = [x for x in data if x[2] == cpu]
    x = sorted([x[4] for x in dt])
    y = sorted([x[5] for x in dt])
    time = sum([x[1] for x in dt])/len(dt)
    f = interpolate.interp1d(x, y, kind='cubic')
    xnew = np.linspace(min(x), max(x), max(x) - min(x) )
    plt.plot(xnew, f(xnew), label=f'AOM {cpu}, Average Time: {round(time)}', linewidth=3, c=colors.pop())


# VP9
plt.plot([], [], ' ', label='FFmpeg 06.05.2020 CQ range: cq 30-60, step 5')
with open('vp9_dotatest.mkvdata.txt', 'r') as f:
        raw = f.read().split('),(')
        raw = [x for x in raw]
        d = raw[1:-1] + [raw[0][1:], raw[-1][:-2]]
        # for i in d:
        #     print(i)

data = []

for x in d:
    try:
        data.append(make_tuple('(' + x + ')'))
    except:
        print(x)


cmap = plt.get_cmap('Greens')
colors = list(cmap(np.linspace(0.4,0.8, len(set([x[2] for x in data])))))

cpus = sorted(set([x[2] for x in data]))

for cpu in cpus:
    dt = [x for x in data if x[2] == cpu]
    if cpu == -1:
        cpu = '0 --best'
    x = sorted([x[4] for x in dt])

    y = sorted([x[5] for x in dt])
    time = sum([x[1] for x in dt])/len(dt)
    f = interpolate.interp1d(x, y, kind='cubic')
    xnew = np.linspace(min(x), max(x), max(x) - min(x) )
    plt.plot(xnew, f(xnew), label=f'VPX VP9 {cpu}, Average Time: {round(time)}', linewidth=3, c=colors.pop())



# x265
plt.plot([], [], ' ', label='FFmpeg 06.05.2020 x265: CRF range: 35 - 17, step 3')
with open('x265_dotatest.mkvdata.txt') as f:
    raw = f.read().split('),(')
    raw = [x for x in raw]
    d = raw[1:-1] + [raw[0][1:], raw[-1][:-2]]

x265 = []

for x in d:
    try:
        x265.append(make_tuple('(' + x + ')'))
    except:
        print(x)

speeds = (('ultrafast', 0), ('superfast', 1), ('veryfast', 2), ('faster', 3), ('fast', 4), ('medium', 5), ('slow', 6), ('slower', 7), ('veryslow', 8), ('placebo',9))


in_file = set([x[2] for x in x265])
speeds = reversed([x for x in speeds if x[0] in in_file])

cmap = plt.get_cmap('Reds')
colors2 = list(cmap(np.linspace(0.4,0.9, len(in_file))))

for speed, _ in speeds:
    ks = [x for x in x265 if x[2] == speed]
    x = sorted([x[4] for x in ks])
    y = sorted(x[5] for x in ks)
    time = sum(x[1] for x in ks)/len(x)
    f = interpolate.interp1d(x, y, kind='cubic')
    xnew = np.linspace(min(x), max(x), max(x) - min(x) )
    plt.plot(xnew, f(xnew), label=f'X265 {speed}, Average Time: {round(time)}',linestyle='-.', linewidth=3, c=colors2.pop())

"""
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
"""


# Plot

plt.xticks([x for x in range(0, 10000, 100)])
plt.yticks([x for x in range(30, 100, 1)])
[plt.axvline(i, color='grey', linewidth=0.3) for i in range(0, 10000, 100)]
[plt.axhline(i, color='grey', linewidth=0.5) for i in range(21, 100, 2)]
[plt.axhline(i, color='black', linewidth=1) for i in range(22, 100, 2)]
plt.ylabel('Vmaf', size=20)
plt.xlabel('Bitrate', size=20)
plt.title('AOM vs VP9 vs x265 ', size=30)
plt.legend(prop={'size': 20}, loc="lower right")
plt.xlim(1000,6000)
plt.ylim((80, 100))
plt.tight_layout()
plt.show()
