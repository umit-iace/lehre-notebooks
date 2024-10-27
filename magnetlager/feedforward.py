# -*- coding: utf-8 -*-
import params as st
import sympy as sp
import numpy as np

def feedForwardStep(t0, T, yd, y0):
    uIn = lambda t: y0 + yd if t0 < t < t0 + T else y0
    return uIn

def feedForwardFlat(t0, T, yd, y0):
    yr = np.array([
        lambda t: y0 + yd * (6 * (t - t0) ** 5 / T ** 5 - 15 * (t - t0) ** 4 / T ** 4 + 10 * (t - t0) ** 3 / T ** 3) if t0 <= t <= t0 + T else y0 if t < t0 else y0 + yd,
        lambda t: yd * (30 * (t - t0) ** 4 / T ** 5 - 60 * (t - t0) ** 3 / T ** 4 + 30 * (t - t0) ** 2 / T ** 3) if t0 < t < t0 + T else 0,
        lambda t: yd * (120 * (t - t0) ** 3 / T ** 5 - 180 * (t - t0) ** 2 / T ** 4 + 60 * (t - t0) / T ** 3) if t0 < t < t0 + T else 0,
    ])

    uIn = lambda t: np.sqrt(st.m / st.k * (yr[2](t) + st.g)) * (yr[0](t) - st.s0)

    return yr, uIn
