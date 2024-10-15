# -*- coding: utf-8 -*-
import numpy as np

def nonlinSys(t, x, u, params):
    g, m, s0 , k = params

    dx = np.zeros(2)
    dx[0] = x[1]
    dx[1] = k / m * u(t) ** 2 / (x[0] - s0) ** 2 - g

    return dx

def stationarySys(yS, params):
    g, m, s0 , k = params

    return np.sqrt(m / k * g) * (yS - s0)