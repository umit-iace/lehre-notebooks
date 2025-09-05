# -*- coding: utf-8 -*-
import params as st
import sympy as sp
import numpy as np

def feedForwardTrapez(t0, yd, params):
    _, _, m, _, vMax, aMax = params
    
    t1 = vMax / aMax
    y1 = aMax * t1 ** 2 / 2
    t2 = (yd - 2 * y1) / vMax + t1
    t3 = t1 + t2

    uIn = lambda t: aMax * m if t0 <= t <= t1 + t0 else -aMax * m if t2 + t0 <= t <= t3 + t0 else 0
    yR = lambda t: aMax / 2 * (t - t0) ** 2 if t0 <= t <= t1 + t0 else \
                   vMax * (t - t0) + y1 - vMax * t1 if t1 + t0 <= t <= t2 + t0 else \
                   aMax * (t1 ** 2.0) / 2 + (t2 - t1 + (t - t2 - t0)) * vMax - aMax * (t - t2 - t0) ** 2 / 2 if t2 + t0 <= t <= t3 + t0 else \
                   0 if t < t0 else yd
    
    return uIn, yR

def feedForwardSCurve(t0, yd, params):
    _, _, m, M, vMax, aMax = params

    Ts = 0.05
    T = 50e-6

    sMax = yd
    jMax = aMax / Ts

    tC = vMax / aMax
    tB = np.sqrt(sMax / aMax)
    tQ = np.minimum(tB, tC)
    tU = sMax / vMax - tC;
    tW = np.maximum(tU,0);
    tJ = np.minimum(Ts,tQ)
    kJ = np.ceil(tJ / T)
    tR = tQ + tW
    kR = np.ceil(tR / T)
    tF = tQ + Ts - tJ
    kF = np.ceil(tF / T)
    kMax = kJ + kR + kF
    j0 = sMax / kJ / kR / kF / T ** 3
    tA = tJ + vMax / aMax
    tV = sMax / vMax - tA

    x1 = x2 = x3 = 0
    c1 = T
    c2 = T ** 2 / 2
    c3 = T ** 3 / 6

    j = np.zeros(int(kMax))
    a = np.zeros(int(kMax))
    v = np.zeros(int(kMax))
    s = np.zeros(int(kMax))

    for k in range(int(kMax)):
        uk = 0;
        if 0 <= k and k < kJ:
            uk = uk + 1
        if kR <= k and k < (kR + kJ):
            uk = uk - 1
        if kF <= k and k < (kF + kJ):
            uk = uk - 1
        if kF + kR <= k and k < kMax:
            uk = uk + 1

        jk = uk * j0
        ak = c1 * x1 * j0
        vk = c2 * x2 * j0
        sk = c3 * x3 * j0

        x3 = 3 * x1 + 3 * x2 + x3 + uk
        x2 = 2 * x1 + x2 + uk
        x1 = x1 + uk
        j[k] = jk
        a[k] = ak
        v[k] = vk
        s[k] = sk

    tTraj = np.linspace(t0, t0 + kMax * T, int(kMax))

    uIn = lambda t: np.interp(t, tTraj, a * m)
    yR = lambda t: np.interp(t, tTraj, s)
    
    return uIn, yR