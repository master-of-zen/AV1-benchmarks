#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib
import statistics
from ast import literal_eval as make_tuple

# Read data about encoding


plt.plot([], [], ' ', label='1920*1080 Frames: ~250 each Encoder step 5, Range: cq 35-10 \nAOM  r29830.g236ac54278-1 ')

# JOJO
with open('crow.txt', 'r') as f:
    data = make_tuple(f.read())
    print(data)
x = [plt.plot([x[2] for x in data], [x[1] for x in data],
    linewidth=1.5, marker="x",label=f'Crow movie segment, dark movie, noise\n'
                                    f'Encoding time = Min time: {min([x[3] for x in data])} '
                                    f'Average time: {round(statistics.mean([x[3] for x in data]), 1)} '
                                    f'Max time {max([x[3] for x in data])}')]
# Crow
with open('jojo.txt', 'r') as f:
    data = make_tuple(f.read())
    print(data)
x = [plt.plot([x[2] for x in data], [x[1] for x in data],
    linewidth=1.5, marker="x",label=f'Jojo anime segment, dim, mostly steady shots\n'
                                    f'Encoding time = Min time: {min([x[3] for x in data])} '
                                    f'Average time: {round(statistics.mean([x[3] for x in data]), 1)} '
                                    f'Max time {max([x[3] for x in data])}')]

# Blue
with open('blue.txt', 'r') as f:
    data = make_tuple(f.read())
    print(data)
x = [plt.plot([x[2] for x in data], [x[1] for x in data],
    linewidth=1.5, marker="x",label=f'Nature footage, lots of details, mostly moving content, moving camera\n'
                                    f'Encoding time = Min time: {min([x[3] for x in data])} '
                                    f'Average time: {round(statistics.mean([x[3] for x in data]), 1)} '
                                    f'Max time {max([x[3] for x in data])}')]



plt.tight_layout()
plt.xticks([x for x in range(300, 50000, 100)])
plt.yticks([x for x in range(74, 100, 1)])
[plt.axvline(i, color='grey', linewidth=0.3) for i in range(300, 26000, 100)]
[plt.axhline(i, color='grey', linewidth=0.5) for i in range(73, 100, 2)]
[plt.axhline(i, color='black', linewidth=1) for i in range(74, 100, 2)]
plt.ylabel('Vmaf', size=20)
plt.xlabel('Bitrate', size=20)
plt.title('AOM Vmaf of Q mode with different video types', size=30)
plt.legend(prop={'size': 20}, loc="lower right")
plt.xlim(500, 4000)
plt.ylim((90, 100))
plt.show()
