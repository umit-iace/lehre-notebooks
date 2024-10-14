# -*- coding: utf-8 -*-
import numpy as np

def linSys(t, x, u, params):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    d, k, m, M = params

    dx = np.zeros(4)
    dx[0] = x2
    dx[1] = u(t) / m
    dx[2] = x4
    dx[3] = (-u(t) - k * x3 - d * x4) / M

    return dx
