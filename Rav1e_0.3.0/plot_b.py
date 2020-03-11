#!/usr/bin/env python3

import matplotlib.pyplot as plt
import statistics
from ast import literal_eval as make_tuple

with open('rav1e_data.txt','r') as f:
    data = make_tuple(f.read())
    print(data)

plt.plot([], [], ' ', label='Rav1e 0.3.0 nUsing 4 tiles (4x1) ')
[plt.plot([x[1] for x in data if x[0] == i], [x[2] for x in data if x[0] == i], linestyle='dashed', linewidth=3.0, label= f'Speed {i} ~ENC TIME = {round(statistics.mean([x[3] for x in data if x[0] == i ]), 1)}') for i in sorted(set([x[0] for x in data]), reverse=False)]


plt.xticks([x for x in range(800, 2400, 100)])
plt.yticks([x for x in range(74, 100, 1)])
[plt.axvline(i, color='grey', linewidth=0.3) for i in range(400, 2400, 100)]
[plt.axhline(i, color='grey', linewidth=0.5) for i in range(73, 100, 2)]
[plt.axhline(i, color='black', linewidth=1) for i in range(74, 100, 2)]
plt.ylabel('Vmaf', size=20)
plt.xlabel('Bitrate', size=20)
plt.title('Rav1e 0.3.0 Film encoding test', size=30)
plt.legend(prop={'size': 22}, loc="lower right")
plt.show()
