Comparison of AV1 encoders and their presets.

Target of this research is to benchmark different AV1 encoders and compare their performance, compare different presets of encoders.

Current test cover: Aomenc, SVT-AV1, Rav1e

All test material and scripts that were used for benchmark and processing data available on GITHUB repository. Feel free to use different sample, different settings, etc

For testing dota2 footage from xiph.org was used. (As It contain a lot of movement and small details, big contrast ranges within scenes and require a lot of bitrate to be encoded at decent quality)

All encoders were working in 8 bit mode.
# Aomenc presets comparison:
## Vmaf:
![](https://github.com/master-of-zen/AV1-benchmarks/blob/master/5.08.2020%20Aomenc%20SVT-AV1%20Rav1e/Plots/aom_vmaf.png)
## PSNR:
![](https://github.com/master-of-zen/AV1-benchmarks/blob/master/5.08.2020%20Aomenc%20SVT-AV1%20Rav1e/Plots/aom_psnr.png)
## SSIM:
![](https://github.com/master-of-zen/AV1-benchmarks/blob/master/5.08.2020%20Aomenc%20SVT-AV1%20Rav1e/Plots/aom_ssim.png)
## MS-SSIM
![](https://github.com/master-of-zen/AV1-benchmarks/blob/master/5.08.2020%20Aomenc%20SVT-AV1%20Rav1e/Plots/aom_mssim.png)
## BD-rates for presets:

### What are BD rates?

> BD-Rate. The Bjontegaard rate difference, also known as BD-rate, allows the measurement of the bitrate reduction offered by a codec or codec feature, while maintaining the same quality as measured by objective metrics.

So next comparison reads like:

> By switching from aomenc preset from cpu-used 6 to cpu-used 5 we need -N % bit rate (negative means we save bit rate - efficiency improves) to get same quality in objective metric Y.

```
Bd rate for speeds:  6 -> 5 

Vmaf BD rate:    -4.579 %
PSNR BD rate:    -4.28 %
SSIM BD rate:    -3.757 %
MS-SSIM BD rate: -3.955 %

Time Diff: +12.939

Bd rate for speeds:  5 -> 4 

Vmaf BD rate:    -7.46 %
PSNR BD rate:    -6.815 %
SSIM BD rate:    -6.737 %
MS-SSIM BD rate: -7.108 %

Time Diff: +69.205

Bd rate for speeds:  4 -> 3 

Vmaf BD rate:    -1.69 %
PSNR BD rate:    -3.957 %
SSIM BD rate:    -2.915 %
MS-SSIM BD rate: -3.902 %

Time Diff: +48.141

Bd rate for speeds:  3 -> 2 

Vmaf BD rate:    -3.416 %
PSNR BD rate:    -4.38 %
SSIM BD rate:    -5.022 %
MS-SSIM BD rate: -4.788 %

Time Diff: +147.199%

Bd rate for speeds:  2 -> 1 

Vmaf BD rate:    -1.567 %
PSNR BD rate:    -1.758 %
SSIM BD rate:    -2.028 %
MS-SSIM BD rate: -1.713 %

Time Diff: +51.777%

Bd rate for speeds:  1 -> 0 

Vmaf BD rate:    -2.007 %
PSNR BD rate:    -0.696 %
SSIM BD rate:    -1.794 %
MS-SSIM BD rate: -1.177 %


Time Diff: +173.963
```


## Fastest/Optimal/Slowest preset comparison:

```
Bd rate for speeds:  6 -> 4 

Vmaf BD rate:    -11.607 %
PSNR BD rate:    -10.787 %
SSIM BD rate:    -10.231 %
MS-SSIM BD rate: -10.758 %

Time Diff: +91.099

Bd rate for speeds:  4 -> 0 

Vmaf BD rate:    -7.816 %
PSNR BD rate:    -10.463 %
SSIM BD rate:    -10.45 %
MS-SSIM BD rate: -11.013 %

Time Diff: +1422.72
```

# SVT-AV1 presets comparison:
## VMAF:
![](https://github.com/master-of-zen/AV1-benchmarks/blob/master/5.08.2020%20Aomenc%20SVT-AV1%20Rav1e/Plots/svt_vmaf.png)
## PSNR:
![](https://github.com/master-of-zen/AV1-benchmarks/blob/master/5.08.2020%20Aomenc%20SVT-AV1%20Rav1e/Plots/svt_psrn.png)
## SSIM
![](https://github.com/master-of-zen/AV1-benchmarks/blob/master/5.08.2020%20Aomenc%20SVT-AV1%20Rav1e/Plots/svt_ssim.png)
## MS-SSIM
![](https://github.com/master-of-zen/AV1-benchmarks/blob/master/5.08.2020%20Aomenc%20SVT-AV1%20Rav1e/Plots/svt_mssim.png)

## BD-rates for presets:

```
Bd rate for speeds:  8 -> 7 

Vmaf BD rate:    -8.59 %
PSNR BD rate:    -5.133 %
SSIM BD rate:    -5.357 %
MS-SSIM BD rate: -5.115 %

Time Diff: +20.462%

Bd rate for speeds:  7 -> 6 

Vmaf BD rate:    -2.033 %
PSNR BD rate:    -1.786 %
SSIM BD rate:    -0.867 %
MS-SSIM BD rate: -0.881 %

Time Diff: +1.986%

Bd rate for speeds:  6 -> 5 

Vmaf BD rate:    -8.428 %
PSNR BD rate:    -8.534 %
SSIM BD rate:    -12.302 %
MS-SSIM BD rate: -11.786 %

Time Diff: +33.58%

Bd rate for speeds:  5 -> 4 

Vmaf BD rate:    -3.671 %
PSNR BD rate:    -5.699 %
SSIM BD rate:    -3.097 %
MS-SSIM BD rate: -3.546 %

Time Diff: +7.139%

Bd rate for speeds:  4 -> 3 

Vmaf BD rate:    -0.285 %
PSNR BD rate:    -0.423 %
SSIM BD rate:    -0.938 %
MS-SSIM BD rate: -0.83 %

Time Diff: +32.051%

Bd rate for speeds:  3 -> 2 

Vmaf BD rate:    -13.658 %
PSNR BD rate:    -9.872 %
SSIM BD rate:    -8.639 %
MS-SSIM BD rate: -8.556 %

Time Diff: +396.304%

Bd rate for speeds:  2 -> 1 

Vmaf BD rate:    -4.79 %
PSNR BD rate:    -6.213 %
SSIM BD rate:    -5.792 %
MS-SSIM BD rate: -5.855 %

Time Diff: +179.056%

Bd rate for speeds:  1 -> 0 

Vmaf BD rate:    0.09 %
PSNR BD rate:    -0.754 %
SSIM BD rate:    -0.288 %
MS-SSIM BD rate: -0.419 %

Time Diff: +29.831%.
```

## Fastest/Optimal/Slowest preset comparison:

```
Bd rate for speeds:  8 -> 4 

Vmaf BD rate:    -20.568 %
PSNR BD rate:    -19.537 %
SSIM BD rate:    -18.624 %
MS-SSIM BD rate: -19.266 %

Time Diff: +75.825

Bd rate for speeds:  4 -> 0 

Vmaf BD rate:    -17.801 %
PSNR BD rate:    -16.43 %
SSIM BD rate:    -14.683 %
MS-SSIM BD rate: -14.861 %

Time Diff: +2274.425%
```

# Rav1e presets comparison:
## VMAF:
![](https://github.com/master-of-zen/AV1-benchmarks/blob/master/5.08.2020%20Aomenc%20SVT-AV1%20Rav1e/Plots/rav1e_vmaf.png)
## PSNR:
![](https://github.com/master-of-zen/AV1-benchmarks/blob/master/5.08.2020%20Aomenc%20SVT-AV1%20Rav1e/Plots/rav1e_psnr.png)
## SSIM:
![](https://github.com/master-of-zen/AV1-benchmarks/blob/master/5.08.2020%20Aomenc%20SVT-AV1%20Rav1e/Plots/rav1e_ssim.png)
## MS-SSIM:
![](https://github.com/master-of-zen/AV1-benchmarks/blob/master/5.08.2020%20Aomenc%20SVT-AV1%20Rav1e/Plots/rav1e_mssim.png)
#### BD-rates for presets:
```
Bd rate for speeds:  10 -> 9 

Vmaf BD rate:    -1.025 %
PSNR BD rate:    -12.423 %
SSIM BD rate:    -4.655 %
MS-SSIM BD rate: -8.422 %

Time Diff: +34.292

Bd rate for speeds:  9 -> 8 

Vmaf BD rate:    -27.324 %
PSNR BD rate:    -26.921 %
SSIM BD rate:    -24.747 %
MS-SSIM BD rate: -25.977 %

Time Diff: +24.3%

Bd rate for speeds:  8 -> 7 

Vmaf BD rate:    -1.052 %
PSNR BD rate:    -0.116 %
SSIM BD rate:    -0.158 %
MS-SSIM BD rate: 0.085 %

Time Diff: +2.253%

Bd rate for speeds:  7 -> 6 

Vmaf BD rate:    -0.477 %
PSNR BD rate:    -0.51 %
SSIM BD rate:    -0.606 %
MS-SSIM BD rate: -0.584 %

Time Diff: +0.907

Bd rate for speeds:  6 -> 5 

Vmaf BD rate:    -4.008 %
PSNR BD rate:    -7.383 %
SSIM BD rate:    -4.821 %
MS-SSIM BD rate: -5.877 %

Time Diff: +36.288

Bd rate for speeds:  5 -> 4 

Vmaf BD rate:    0.223 %
PSNR BD rate:    -0.048 %
SSIM BD rate:    0.009 %
MS-SSIM BD rate: -0.006 %

Time Diff: +4.194

Bd rate for speeds:  4 -> 3 

Vmaf BD rate:    -0.609 %
PSNR BD rate:    -0.635 %
SSIM BD rate:    -0.838 %
MS-SSIM BD rate: -0.727 %

Time Diff: +0.181%

Bd rate for speeds:  3 -> 2 

Vmaf BD rate:    -0.524 %
PSNR BD rate:    -1.87 %
SSIM BD rate:    -0.562 %
MS-SSIM BD rate: -1.003 %

Time Diff: +34.176

Bd rate for speeds:  2 -> 1 

Vmaf BD rate:    -2.993 %
PSNR BD rate:    -3.319 %
SSIM BD rate:    -2.647 %
MS-SSIM BD rate: -2.933 %

Time Diff: +40.646

Bd rate for speeds:  1 -> 0 

Vmaf BD rate:    -6.826 %
PSNR BD rate:    -8.231 %
SSIM BD rate:    -10.606 %
MS-SSIM BD rate: -10.783 %

Time Diff: +404.139
```

## Fastest/Optimal/Slowest preset comparison:

```
Bd rate for speeds:  10 -> 6 

Vmaf BD rate:    -29.108 %
PSNR BD rate:    -36.452 %
SSIM BD rate:    -28.774 %
MS-SSIM BD rate: -32.57 %

Time Diff: +72.235

Bd rate for speeds:  6 -> 0 

Vmaf BD rate:    -14.018 %
PSNR BD rate:    -20.021 %
SSIM BD rate:    -18.206 %
MS-SSIM BD rate: -19.945 %

Time Diff: +1253.436
```

# Encoders comparison:
## VMAF:
![](https://github.com/master-of-zen/AV1-benchmarks/blob/master/5.08.2020%20Aomenc%20SVT-AV1%20Rav1e/Plots/all_vmaf.png)
## PSNR:
![](https://github.com/master-of-zen/AV1-benchmarks/blob/master/5.08.2020%20Aomenc%20SVT-AV1%20Rav1e/Plots/all_psnr.png)
## SSIM:
![](https://github.com/master-of-zen/AV1-benchmarks/blob/master/5.08.2020%20Aomenc%20SVT-AV1%20Rav1e/Plots/all_ssim.png)
## MS-SSIM:
![](https://github.com/master-of-zen/AV1-benchmarks/blob/master/5.08.2020%20Aomenc%20SVT-AV1%20Rav1e/Plots/all_mssim.png)
## Encoders presets comparison:

### For preset comparsion I selected aom presets (0,4,6), for SVT-AV1 (0,4,8), Rav1e(0,6,10).

### Presets compared from most unefficient to most efficient.

Next comparison reads like:

> By switching from Rav1e preset 10 to SVT-AV1 preset 8 need -N % bit rate (negative means we save bit rate - efficiency improves) to get same quality in objective metric Y.

```
Bd rate for :  Rav1e, 10 -> SVT-AV1, 8 

Vmaf BD rate:    -18.973 %
PSNR BD rate:    -43.094 %
SSIM BD rate:    -16.071 %
MS-SSIM BD rate: -28.58 %

Time Diff: 34.071%

Bd rate for :  SVT-AV1, 8 -> Rav1e, 6 

Vmaf BD rate:    -12.637 %
PSNR BD rate:    11.078 %
SSIM BD rate:    -13.954 %
MS-SSIM BD rate: -4.973 %

Time Diff: 28.465%

Bd rate for :  Rav1e, 6 -> SVT-AV1, 4 

Vmaf BD rate:    -8.906 %
PSNR BD rate:    -27.346 %
SSIM BD rate:    -7.091 %
MS-SSIM BD rate: -15.619 %

Time Diff: 36.866%

Bd rate for :  SVT-AV1, 4 -> Rav1e, 0 

Vmaf BD rate:    -5.766 %
PSNR BD rate:    9.974 %
SSIM BD rate:    -11.214 %
MS-SSIM BD rate: -4.743 %

Time Diff: 888.878%

Bd rate for :  Rav1e, 0 -> Aomenc, 6 

Vmaf BD rate:    -1.571 %
PSNR BD rate:    -8.311 %
SSIM BD rate:    4.342 %
MS-SSIM BD rate: 2.205 %

Time Diff: -87.311%

Bd rate for :  Aomenc, 6 -> Aomenc, 4 

Vmaf BD rate:    -11.607 %
PSNR BD rate:    -10.787 %
SSIM BD rate:    -10.231 %
MS-SSIM BD rate: -10.758 %

Time Diff: 91.099%

Bd rate for :  Aomenc, 4 -> SVT-AV1, 0 

Vmaf BD rate:    1.13 %
PSNR BD rate:    -7.291 %
SSIM BD rate:    2.367 %
MS-SSIM BD rate: -2.73 %

Time Diff: 890.196%

Bd rate for :  SVT-AV1, 0 -> Aomenc, 0 

Vmaf BD rate:    -8.188 %
PSNR BD rate:    -3.389 %
SSIM BD rate:    -11.311 %
MS-SSIM BD rate: -7.985 %

Time Diff: 53.78%
```
Thanks for attention :)
