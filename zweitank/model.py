# -*- coding: utf-8 -*-
import numpy as np

def outflow(h, a, g):
    """Ausfluss nach Torricelli, leerer Tank liefert keinen Ausfluss"""
    return a * np.sqrt(2 * g * np.maximum(h, 0))

def nonlinSys(t, x, u, params):
    h1 = x[0]
    h2 = x[1]

    g, A1, A2, a1, a2 = params

    # Pumpe kann nur fördern
    q = np.maximum(u(t), 0)

    dx = np.zeros(2)
    dx[0] = (q - outflow(h1, a1, g)) / A1
    dx[1] = (outflow(h1, a1, g) - outflow(h2, a2, g)) / A2

    return dx

def stationarySys(yS, params):
    """Ruhelage (u, h2) zum Füllstand h1 = yS"""
    g, A1, A2, a1, a2 = params

    uS = outflow(yS, a1, g)
    h2S = (a1 / a2) ** 2 * yS

    return uS, h2S
