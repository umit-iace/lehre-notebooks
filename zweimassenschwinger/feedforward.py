# -*- coding: utf-8 -*-
import params as st
import sympy as sp
import numpy as np

def feedForwardTrapez(t0, T, yd):
    aMax = 15.0
    vMax = 1.5
    
    t1 = vMax / aMax
    y1 = aMax * t1 ** 2 / 2
    t2 = (yd - 2 * y1) / vMax + t1
    t3 = t1 + t2

    uIn = lambda t: aMax if t0 <= t <= t1 + t0 else -aMax if t2 + t0 <= t <= t3 + t0 else 0
    yR = lambda t: aMax / 2 * (t - t0) ** 2 if t0 <= t <= t1 + t0 else \
                   vMax * (t - t0) + y1 - vMax * t1 if t1 + t0 <= t <= t2 + t0 else \
                   aMax * (t1 ** 2.0) / 2 + (t2 - t1 + (t - t2 - t0)) * vMax - aMax * (t - t2 - t0) ** 2 / 2 if t2 + t0 <= t <= t3 + t0 else \
                   0 if t < t0 else yd
    
    return uIn, yR
