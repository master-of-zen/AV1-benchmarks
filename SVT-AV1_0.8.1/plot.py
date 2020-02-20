#!/usr/bin/env python3

import matplotlib.pyplot as plt
import statistics
from ast import literal_eval as make_tuple

# Read data about encoding
with open('svt_data.txt', 'r') as f:
    data = make_tuple(f.read())
    print(data)

plt.plot([], [], ' ', label='SVT-AV1 0.8.1 Vmaf Test\n1920*800 Frames: 71\nEncoder step: 200kbit/s ')
print(data[0])
[plt.plot([x[1] for x in data if x[0] == i and x[4] == 1],
[x[2] for x in data if x[0] == i and x[4] == 1],
 linestyle='dashed', linewidth=3.0,
 label= f'Enc-mode {i} Pass: {1} ~ENC TIME = {round(statistics.mean([x[3] for x in data if x[0] == i  ]), 1)}')
 for i in sorted(set([x[0] for x in data if x[4] == 1]), reverse=False)]

[plt.plot([x[1] for x in data if x[0] == i and x[4] == 2],
[x[2] for x in data if x[0] == i and x[4] == 2],
 linewidth=3.0,
 label= f'Enc-mode {i} Pass: {2} ~ENC TIME = {round(statistics.mean([x[3] for x in data if x[0] == i ]), 1)}')
 for i in sorted(set([x[0] for x in data  if x[4] == 2 ]), reverse=False)]

plt.tight_layout()
plt.xticks([x for x in range(800, 2600, 100)])
plt.yticks([x for x in range(74, 100, 1)])
[plt.axvline(i, color='grey', linewidth=0.3) for i in range(800, 2600, 100)]
[plt.axhline(i, color='grey', linewidth=0.5) for i in range(73, 100, 2)]
[plt.axhline(i, color='black', linewidth=1) for i in range(74, 100, 2)]
plt.ylabel('Vmaf', size=20)
plt.xlabel('Bitrate', size=20)
plt.title('SVT-AV1 0.8.1 Film encoding test', size=30)
plt.legend(prop={'size': 22}, loc="lower right")
plt.ylim((80, 100))
plt.show()
