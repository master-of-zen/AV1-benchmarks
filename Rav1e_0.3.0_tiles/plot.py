#!/usr/bin/env python3

import matplotlib.pyplot as plt
import statistics
from ast import literal_eval as make_tuple
from scipy.ndimage.filters import gaussian_filter1d

# Read data about encoding
with open('video/data_rav1e.txt', 'r') as f:
    data = make_tuple(f.read())

plt.plot([], [], ' ', label='Rav1e Vmaf Test\n1920*800 Frames: 71\nEncoder step: 200Kb/s ')

[plt.plot([x[1] for x in data if x[0] == i ],
[x[2] for x in data if x[0] == i],
 linewidth=3.0, markevery=1,
 label= f'Enc-mode {i} Tiles: {4} ~ENC TIME = {round(statistics.mean([x[3] for x in data if x[0] == i]), 1)}')
 for i in sorted(set([x[0] for x in data]), reverse=False)]

plt.tight_layout()
plt.xticks([x for x in range(10, 160, 10)])
plt.yticks([x for x in range(80, 101, 1)])
[plt.axvline(i, color='grey', linewidth=0.3) for i in range(10, 160, 10)]
[plt.axhline(i, color='grey', linewidth=0.5) for i in range(81, 101, 2)]
[plt.axhline(i, color='black', linewidth=1) for i in range(80, 101, 2)]
plt.ylabel('Vmaf', size=20)
plt.xlabel('Quantizer', size=20)
plt.title('Rav1e 0.3.0 vmaf tile test', size=30)
plt.legend(prop={'size': 22}, loc="lower right")
plt.show()
