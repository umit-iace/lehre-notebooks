# -*- coding: utf-8 -*-
import params as st
import sympy as sp
import numpy as np

def feedForwardTrapez(t0, T, yd, params):
    _, _, m, _, aMax = params

    t3 = T
    
    t1 = ( aMax * t3 - np.sqrt( aMax * (aMax * t3 ** 2 - 4 * yd) ) ) / (2 * aMax)
    t2 = ( aMax * t3 + np.sqrt( aMax * (aMax * t3 ** 2 - 4 * yd) ) ) / (2 * aMax)
    y1 = aMax * t3 ** 2 / 4 - t3 * np.sqrt( aMax * (aMax * t3 ** 2 - 4 * yd) ) / 4 - yd / 2
    vMax = aMax * t3 / 2 - np.sqrt( aMax * (aMax * t3 ** 2 - 4 * yd) ) / 2

    uIn = lambda t: aMax * m if t0 <= t <= t1 + t0 else -aMax * m if t2 + t0 <= t <= t3 + t0 else 0
    yR = []
    yR.append(lambda t: aMax / 2 * (t - t0) ** 2 if t0 <= t <= t1 + t0 else \
                      vMax * (t - t0) + y1 - vMax * t1 if t1 + t0 <= t <= t2 + t0 else \
                      aMax * (t1 ** 2.0) / 2 + (t2 - t1 + (t - t2 - t0)) * vMax - aMax * (t - t2 - t0) ** 2 / 2 if t2 + t0 <= t <= t3 + t0 else \
                      0 if t < t0 else yd)
    yR.append(lambda t: aMax * (t - t0) if t0 <= t <= t1 + t0 else \
                      vMax if t1 + t0 <= t <= t2 + t0 else \
                      vMax - aMax * (t - t2 - t0) if t2 + t0 <= t <= t3 + t0 else \
                      0)
    yR.append(lambda t: aMax if t0 <= t <= t1 + t0 else \
                      - aMax if t2 + t0 <= t <= t3 + t0 else \
                      0)
    
    return uIn, yR

def feedForwardInputShaping(y1R, params):
    d, k, m, M, _ = params

    omega0 = np.sqrt(k / M)
    zeta = d / (2 * M)
    T = np.pi / np.sqrt(omega0 ** 2 - zeta ** 2)

    kappa = np.exp(-zeta * T)
    
    k0 = 1 / (1 + kappa)
    k1 = kappa / (1 + kappa)
    
    v = lambda t: y1R[2](t) * m
    uZvs = lambda t: k0 * v(t) + k1 * v(t - T)

    uIn = lambda t: uZvs(t)

    return uIn

def feedForwardFlach(t0, T, yd, params):
    d, k, m , M, _ = params

    yr = np.array([
        lambda t: yd * (70 * (t - t0) ** 9 / T ** 9 - 315 * (t - t0) ** 8 / T ** 8 + 540 * (t - t0) ** 7 / T ** 7 - 420 * (t - t0) ** 6 / T ** 6 + 126 * (t - t0) ** 5 / T ** 5) if t0 <= t <= t0 + T else 0 if t < t0 else yd,
        lambda t: yd * (630 * (t - t0) ** 8 / T ** 9 - 2520 * (t - t0) ** 7 / T ** 8 + 3780 * (t - t0) ** 6 / T ** 7 - 2520 * (t - t0) ** 5 / T ** 6 + 630 * (t - t0) ** 4 / T ** 5) if t0 < t < t0 + T else 0,
        lambda t: yd * (5040 * (t - t0) ** 7 / T ** 9 - 17640 * (t - t0) ** 6 / T ** 8 + 22680 * (t - t0) ** 5 / T ** 7 - 12600 * (t - t0) ** 4 / T ** 6 + 2520 * (t - t0) ** 3 / T ** 5) if t0 < t < t0 + T else 0,
        lambda t: yd * (35280 * (t - t0) ** 6 / T ** 9 - 105840 * (t - t0) ** 5 / T ** 8 + 113400 * (t - t0) ** 4 / T ** 7 - 50400 * (t - t0) ** 3 / T ** 6 + 7560 * (t - t0) ** 2 / T ** 5) if t0 < t < t0 + T else 0,
        lambda t: yd * (211680 * (t - t0) ** 5 / T ** 9 - 529200 * (t - t0) ** 4 / T ** 8 + 453600 * (t - t0) ** 3 / T ** 7 - 151200 * (t - t0) ** 2 / T ** 6 + 15120 * (t - t0) / T ** 5) if t0 < t < t0 + T else 0,
    ])

    uIn = lambda t: m * (yr[2](t) + d / k * yr[3](t) + M / k * yr[4](t))

    y1R = np.array([
        lambda t: yr[0](t) + d / k * yr[1](t) + (m + M) / k * yr[2](t)
    ])
    y2R = np.array([
        lambda t: - m / k * yr[2](t)
    ])
    
    return uIn, y1R, y2R