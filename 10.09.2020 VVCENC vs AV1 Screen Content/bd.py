#!/usr/bin/python
# Copyright 2014 Google.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Converts video encoding result data from text files to visualization
data source."""

# __author__ = "jzern@google.com (James Zern),"
# __author__ += "jimbankoski@google.com (Jim Bankoski)"
# __author__ += "hta@gogle.com (Harald Alvestrand)"


import math
import numpy
import sys
from ast import literal_eval

def bdsnr(metric_set1, metric_set2):
  """
  BJONTEGAARD    Bjontegaard metric calculation
  Bjontegaard's metric allows to compute the average gain in psnr between two
  rate-distortion curves [1].
  rate1,psnr1 - RD points for curve 1
  rate2,psnr2 - RD points for curve 2

  returns the calculated Bjontegaard metric 'dsnr'

  code adapted from code written by : (c) 2010 Giuseppe Valenzise
  http://www.mathworks.com/matlabcentral/fileexchange/27798-bjontegaard-metric/content/bjontegaard.m
  """
  # pylint: disable=too-many-locals
  # numpy seems to do tricks with its exports.
  # pylint: disable=no-member
  # map() is recommended against.
  rate1 = [x[0] for x in metric_set1]
  psnr1 = [x[1] for x in metric_set1]
  rate2 = [x[0] for x in metric_set2]
  psnr2 = [x[1] for x in metric_set2]

  log_rate1 = list(map(math.log, rate1))
  log_rate2 = list(map(math.log, rate2))

  # Best cubic poly fit for graph represented by log_ratex, psrn_x.
  poly1 = numpy.polyfit(log_rate1, psnr1, 3)
  poly2 = numpy.polyfit(log_rate2, psnr2, 3)

  # Integration interval.
  min_int = max([min(log_rate1), min(log_rate2)])
  max_int = min([max(log_rate1), max(log_rate2)])

  # Integrate poly1, and poly2.
  p_int1 = numpy.polyint(poly1)
  p_int2 = numpy.polyint(poly2)

  # Calculate the integrated value over the interval we care about.
  int1 = numpy.polyval(p_int1, max_int) - numpy.polyval(p_int1, min_int)
  int2 = numpy.polyval(p_int2, max_int) - numpy.polyval(p_int2, min_int)

  # Calculate the average improvement.
  if max_int != min_int:
    avg_diff = (int2 - int1) / (max_int - min_int)
  else:
    avg_diff = 0.0
  return avg_diff


def bdrate(metric_set1, metric_set2):
  """
  BJONTEGAARD    Bjontegaard metric calculation
  Bjontegaard's metric allows to compute the average % saving in bitrate
  between two rate-distortion curves [1].

  rate1,psnr1 - RD points for curve 1
  rate2,psnr2 - RD points for curve 2

  adapted from code from: (c) 2010 Giuseppe Valenzise

  """
  # numpy plays games with its exported functions.
  # pylint: disable=no-member
  # pylint: disable=too-many-locals
  # pylint: disable=bad-builtin
  rate1 = [x[0] for x in metric_set1]
  psnr1 = [x[1] for x in metric_set1]
  rate2 = [x[0] for x in metric_set2]
  psnr2 = [x[1] for x in metric_set2]

  log_rate1 = list(map(math.log, rate1))
  log_rate2 = list(map(math.log, rate2))

  # Best cubic poly fit for graph represented by log_ratex, psrn_x.
  poly1 = numpy.polyfit(psnr1, log_rate1, 3)
  poly2 = numpy.polyfit(psnr2, log_rate2, 3)

  # Integration interval.
  min_int = max([min(psnr1), min(psnr2)])
  max_int = min([max(psnr1), max(psnr2)])

  # find integral
  p_int1 = numpy.polyint(poly1)
  p_int2 = numpy.polyint(poly2)

  # Calculate the integrated value over the interval we care about.
  int1 = numpy.polyval(p_int1, max_int) - numpy.polyval(p_int1, min_int)
  int2 = numpy.polyval(p_int2, max_int) - numpy.polyval(p_int2, min_int)

  # Calculate the average improvement.
  avg_exp_diff = (int2 - int1) / (max_int - min_int)

  # In really bad formed data the exponent can grow too large.
  # clamp it.
  if avg_exp_diff > 200:
    avg_exp_diff = 200

  # Convert to a percentage.
  avg_diff = (math.exp(avg_exp_diff) - 1) * 100

  return avg_diff


with open(sys.argv[1]) as f:
    data = literal_eval(f.readline())

un = [x[0] for x in data]
un = list(set(un))

ls = []
for r in un:
  ii = ' '
  i = r

  #Vmaf
  vmaf0 = [(x[4],x[5]) for x in data if x[0] == i ]
  vmaf1 = [(x[4],x[5]) for x in data if x[0] == ii ]

  #PSNR
  psnr0 = [(x[4],x[6], 3) for x in data if x[0] == i ]
  psnr1 = [(x[4],x[6], 3) for x in data if x[0] == ii ]

  # SSIM
  ssim0 = [(x[4],x[7]) for x in data if x[0] == i ]
  ssim1 = [(x[4],x[7]) for x in data if x[0] == ii ]

  # MS-SSIM
  mssim0 = [(x[4],x[8]) for x in data if x[0] == i ]
  mssim1 = [(x[4],x[8]) for x in data if x[0] == ii ]

  #print('Vmaf BD rate:   ', round(bdrate(vmaf1, vmaf0), 3),'%')
  #print('PSNR BD rate:   ', round(bdrate(psnr1, psnr0), 3 ),'%')
  #print('SSIM BD rate:   ', round(bdrate(ssim1, ssim0), 3 ),'%')
  #print('MS-SSIM BD rate:', round(bdrate(mssim1, mssim0), 3),'%')
  #print()

  ls.append((r, round(bdrate(vmaf1, vmaf0), 3), round(bdrate(psnr1, psnr0), 3 ), round(bdrate(ssim1, ssim0), 3 ), round(bdrate(mssim1, mssim0), 3)))
  # time0 = [x[1] for x in data if x[0] == i ]
  # time1 = [x[1] for x in data if x[0] == ii ]
  # mean = sum(time0) / sum(time1)
  # mean_time = ( mean -1) * 100
  # print(f'Time Diff: {round( mean_time, 3)}%')

ls.sort(key=lambda x: x[1])
for x in ls:
  print(x[0])
  print('Vmaf:', x[1])
  print('Psnr:', x[2])
  print('Ssim:', x[3])
  print('Msim:', x[4])
  print()
