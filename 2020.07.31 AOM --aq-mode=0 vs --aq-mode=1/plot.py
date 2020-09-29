#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import matplotlib
import statistics
from ast import literal_eval as make_tuple
from scipy import interpolate
import numpy as np
import sys


# AOMS

plt.plot([], [], ' ', label='Aq modes comparison')
with open(sys.argv[1], 'r') as f:
        data = make_tuple(f.read())

dt = []

x_limit = []
y_limit = []

for q in sorted(set([x[2] for x in data])):

    dt = [x for x in data if x[2] == q]
    x = sorted([x[4] for x in dt])
    y = sorted([x[5] for x in dt])
    x_limit.append((min(x), max(x)))
    y_limit.append((min(y), max(y)))
    time = sum([x[1] for x in dt])/len(dt)
    f = interpolate.interp1d(x, y, kind='quadratic')
    xnew = np.linspace(min(x), max(x), max(x) - min(x) )
    plt.plot(xnew, f(xnew), label=f'--aq-mode={q}', linewidth=3)

# Plot


xlim = min([x[0] for x in x_limit])
x_max = max(([x[1] for x in x_limit]))

ylim = min([x[0] for x in y_limit])
y_max = max(([x[1] for x in y_limit]))

plt.tight_layout()
plt.xticks([x for x in range(0, x_max, 1000)])
plt.yticks([x for x in range(30, 100, 1)])
[plt.axvline(i, color='grey', linewidth=0.3) for i in range(0, x_max, 500)]
[plt.axhline(i, color='grey', linewidth=0.5) for i in range(21, 100, 2)]
[plt.axhline(i, color='black', linewidth=1) for i in range(22, 100, 2)]
plt.ylabel('Vmaf', size=20)
plt.xlabel('Bitrate', size=20)
plt.title('AOM --aq-mode=0 vs --aq-mode=1  31.07.2020 ', size=30)
plt.legend(prop={'size': 20}, loc="lower right")



plt.xlim(xlim, x_max)
plt.ylim((ylim, 100))
plt.show()
