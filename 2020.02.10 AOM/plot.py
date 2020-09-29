#!/usr/bin/env python3

import matplotlib.pyplot as plt
import statistics
from ast import literal_eval as make_tuple

# Read data about encoding
with open('svt_data.txt', 'r') as f:
    data = make_tuple(f.read())
    print(data)

plt.plot([], [], ' ', label='1920*800 Frames: 71\nEncoder step: 200kbit/s\nSVT-AV1 0.8.1 ')
print(data[0])
[plt.plot([x[1] for x in data if x[0] == i and x[4] == 1],
[x[2] for x in data if x[0] == i and x[4] == 1],
 linestyle='dashed', linewidth=3.0,
 label= f'Enc-mode {i} Pass: {1} ~ENC TIME = {round(statistics.mean([x[3] for x in data if x[0] == i  ]), 1)}')
 for i in sorted(set([x[0] for x in data if x[4] == 1]), reverse=False)]

with open('data.txt', 'r') as f:
    data = make_tuple(f.read())
plt.plot([], [], ' ', label='AOM --threads=4 ')

[plt.plot([x[1] for x in data if x[0] == i],
          [x[2] for x in data if x[0] == i],
          linestyle='solid',
          linewidth=3.0,
          label=f'Cpu-used: {i} ~ENC TIME = {round(statistics.mean([x[3] for x in data if x[0] == i]), 1)}')
 for i in sorted(set([x[0] for x in data]), reverse=False)]


with open('rav1e_data.txt', 'r') as f:
    data = make_tuple(f.read())
    print(data)

plt.plot([], [], ' ', label='Rav1e 0.3.0 4 tiles (4x1) ')
[plt.plot([x[1] for x in data if x[0] == i], [x[2] for x in data if x[0] == i],
          linestyle='dashdot', linewidth=3.0, label= f'Speed {i} ~ENC TIME = {round(statistics.mean([x[3] for x in data if x[0] == i ]), 1)}')
for i in sorted(set([x[0] for x in data]), reverse=False)]


plt.tight_layout()
plt.xticks([x for x in range(800, 2600, 100)])
plt.yticks([x for x in range(74, 100, 1)])
[plt.axvline(i, color='grey', linewidth=0.3) for i in range(800, 2600, 100)]
[plt.axhline(i, color='grey', linewidth=0.5) for i in range(73, 100, 2)]
[plt.axhline(i, color='black', linewidth=1) for i in range(74, 100, 2)]
plt.ylabel('Vmaf', size=20)
plt.xlabel('Bitrate', size=20)
plt.title('AOM 15.02.2020 VS Rav1e 0.3.0 VS SVT-AV1 0.8.1 Film encoding test', size=30)
plt.legend(prop={'size': 20}, loc="lower right")
plt.ylim((80, 100))
plt.show()
