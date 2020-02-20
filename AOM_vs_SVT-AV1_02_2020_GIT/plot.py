#!/usr/bin/env python3

import matplotlib.pyplot as plt
import statistics
from ast import literal_eval as make_tuple
from pathlib import Path
"""






plt.plot([], [], ' ', label='1280x720 Frames: 360\nEncoder step: 200kbit/s')

with open('data_rav1e.txt', 'r') as f:
    data = make_tuple(f.read())
    print(data)

plt.plot([], [], ' ', label='Rav1e 0.3.0-1 4 tiles (4x1) ')
[plt.plot([x[1] for x in data if x[0] == i], [x[2] for x in data if x[0] == i],
          linestyle='dashdot', linewidth=3.0, label= f'Speed {i} ~ENC TIME = {round(statistics.mean([x[3] for x in data if x[0] == i ]), 1)}')
for i in sorted(set([x[0] for x in data]), reverse=False)]
"""
plt.plot([], [], ' ', label='1280x720 Frames: 360')

# AOM
with open('/home/zen/Git/AV1-benchmarks/bench/aomdata.txt', 'r') as d:
    data = make_tuple(d.read())
    plt.plot([], [], ' ', label='AOM Current Git r29645.gd3e939dbf7-1 --threads=4 ')

    [plt.plot([x[1] for x in data if x[0] == i],
            [x[2] for x in data if x[0] == i],
            linestyle='solid',
            linewidth=3.0,
            label=f'Cpu-used: {i} ~time = {round(statistics.mean([x[3] for x in data if x[0] == i]), 1)}')
    for i in sorted(set([x[0] for x in data]), reverse=False)]

# SVT-AV1

with open('/home/zen/Git/AV1-benchmarks/bench/data_svt.txt', 'r') as f:
    data = make_tuple(f.read())
    print(data)

print(data[0])
plt.plot([], [], ' ', label='SVT-AV1 0.8.1 GIT 0.8.1.r47.g355e277d-1 ')
[plt.plot([x[1] for x in data if x[0] == i],
[x[2] for x in data if x[0] == i],
 linestyle='dashed', linewidth=3.0,
 label= f'enc-mode: {i} ~time: {round(statistics.mean([x[3] for x in data if x[0] == i ]), 1)}')
 for i in sorted(set([x[0] for x in data]), reverse=False)]


plt.tight_layout()
plt.xticks([x for x in range(600, 2100, 100)])
plt.yticks([x for x in range(80, 100, 1)])
[plt.axvline(i, color='grey', linewidth=0.3) for i in range(600, 2100, 100)]
[plt.axhline(i, color='grey', linewidth=0.5) for i in range(73, 100, 2)]
[plt.axhline(i, color='black', linewidth=1) for i in range(74, 100, 2)]
plt.ylabel('Vmaf', size=20)
plt.xlabel('Bitrate', size=20)
plt.title('AOM VS SVT-AV1 Animation encoding test', size=30)
plt.legend(prop={'size': 20}, loc="lower right")
plt.ylim((80, 100))
plt.show()
