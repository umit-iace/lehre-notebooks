# -*- coding: utf-8 -*-
import params as st
import sympy as sp
import numpy as np

def feedForwardRamp(t0, T, yd):
    uIn = lambda t: yd if t0 < t < t0 + T else 0
    return uIn

def feedForwardLinFlat(t0, T, yd):
    yr = np.array([
        lambda t: yd * (70 * (t - t0) ** 9 / T ** 9 - 315 * (t - t0) ** 8 / T ** 8 + 540 * (t - t0) ** 7 / T ** 7 - 420 * (t - t0) ** 6 / T ** 6 + 126 * (t - t0) ** 5 / T ** 5) if t0 <= t <= t0 + T else 0 if t < t0 else yd,
        lambda t: yd * (630 * (t - t0) ** 8 / T ** 9 - 2520 * (t - t0) ** 7 / T ** 8 + 3780 * (t - t0) ** 6 / T ** 7 - 2520 * (t - t0) ** 5 / T ** 6 + 630 * (t - t0) ** 4 / T ** 5) if t0 < t < t0 + T else 0,
        lambda t: yd * (5040 * (t - t0) ** 7 / T ** 9 - 17640 * (t - t0) ** 6 / T ** 8 + 22680 * (t - t0) ** 5 / T ** 7 - 12600 * (t - t0) ** 4 / T ** 6 + 2520 * (t - t0) ** 3 / T ** 5) if t0 < t < t0 + T else 0,
        lambda t: yd * (35280 * (t - t0) ** 6 / T ** 9 - 105840 * (t - t0) ** 5 / T ** 8 + 113400 * (t - t0) ** 4 / T ** 7 - 50400 * (t - t0) ** 3 / T ** 6 + 7560 * (t - t0) ** 2 / T ** 5) if t0 < t < t0 + T else 0,
        lambda t: yd * (211680 * (t - t0) ** 5 / T ** 9 - 529200 * (t - t0) ** 4 / T ** 8 + 453600 * (t - t0) ** 3 / T ** 7 - 151200 * (t - t0) ** 2 / T ** 6 + 15120 * (t - t0) / T ** 5) if t0 < t < t0 + T else 0,
    ])

    uIn = lambda t: st.M * st.l / st.g * yr[4](t) + (st.M + st.m) * yr[2](t)

    thetar = lambda t: - yr[2](t) / st.g
    Dr = lambda t: yr[0](t) + st.l / st.g * yr[2](t)
    
    return yr, uIn, Dr, thetar