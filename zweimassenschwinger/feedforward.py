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

