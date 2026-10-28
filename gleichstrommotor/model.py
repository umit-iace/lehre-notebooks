# -*- coding: utf-8 -*-
import numpy as np

def linSys(t, x, u, tauL, params):
    i = x[0]
    w = x[1]

    R, LA, k, J, nu = params

    dx = np.zeros(2)
    dx[0] = (-R * i - k * w + u(t)) / LA
    dx[1] = (k * i - nu * w - tauL(t)) / J

    return dx

def sysMatrices(params):
    R, LA, k, J, nu = params

    A = np.array([[-R / LA, -k / LA],
                  [k / J, -nu / J]])
    b = np.array([1 / LA, 0])
    c = np.array([0, 1])
    P = np.array([[0], [-1 / J]])
    Q = np.array([[0]])

    return A, b, c, P, Q
