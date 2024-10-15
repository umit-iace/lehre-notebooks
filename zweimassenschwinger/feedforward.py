# -*- coding: utf-8 -*-
import params as st
import sympy as sp
import numpy as np

def feedForwardTrapez(t0, T, yd):
    aMax = 10.0
    vMax = 2.5
    t1 = vMax / aMax
    y1 = aMax * t1 ** 2 / 2
    t2 = (2 * yd - 0.5 * y1) / vMax + t1
    t3 = t2 + t1
    uIn = lambda t: aMax if t0 <= t <= t1 + t0 else -aMax if t2 + t0 <= t <= t3 + t0 else 0
    return uIn
