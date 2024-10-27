# -*- coding: utf-8 -*-
import numpy as np

def nonlinObs(t, x, u, l, yMeas, params):
    g, m, s0 , k = params

    dx = np.zeros(3)
    dx[0] = x[1] - l[0] * (x[0] - yMeas)
    dx[1] = k / m * u(t) ** 2 / (x[0] - s0) ** 2 - g - l[1] * (x[0] - yMeas)
    dx[2] = - l[2] * (x[0] - yMeas)
    
    return dx