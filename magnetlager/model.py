# -*- coding: utf-8 -*-
import numpy as np

def nonlinSys(t, x, u, params):
    k, m, s0, g = params

    dx = np.zeros(2)
    dx[0] = x[1]
    dx[1] = k / m * u(t) ** 2 / (x[0] - s0) ** 2 - g

    return dx
