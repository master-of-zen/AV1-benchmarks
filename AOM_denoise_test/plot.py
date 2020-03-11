#!/usr/bin/env python3

import matplotlib.pyplot as plt
import statistics
from ast import literal_eval as make_tuple
from scipy.ndimage.filters import gaussian_filter1d

# Read data about encoding
with open('video/data.txt', 'r') as f:
    data = make_tuple(f.read())

plt.plot([], [], ' ', label='Rav1e Tiles Vmaf Test\n1920*800 Frames: 71\nEncoder step: 200Kb/s ')

[[plt.plot([x[1] for x in data if x[0] == i and x[4] == tl],
[x[2] for x in data if x[0] == i and x[4] == tl],
 linewidth=3.0, markevery=1,
 label= f'Enc-mode {i} Tiles: {tl} ~ENC TIME = {round(statistics.mean([x[3] for x in data if x[0] == i and x[4] == tl ]), 1)}') 
 for i in sorted(set([x[0] for x in data if x[4] == 1]), reverse=False)] for tl in set(x[4] for x in data)]

plt.tight_layout()
plt.xticks([x for x in range(1000, 2100, 100)])
plt.yticks([x for x in range(88, 95, 1)])
[plt.axvline(i, color='grey', linewidth=0.3) for i in range(1000, 2100, 100)]
[plt.axhline(i, color='grey', linewidth=0.5) for i in range(89, 95, 2)]
[plt.axhline(i, color='black', linewidth=1) for i in range(88, 95, 2)]
plt.ylabel('Vmaf', size=20)
plt.xlabel('Bitrate', size=20)
plt.title('Rav1e 0.3.0 vmaf tile test', size=30)
plt.legend(prop={'size': 22}, loc="lower right")
plt.show()
