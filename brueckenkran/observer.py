# -*- coding: utf-8 -*-
import numpy as np

def linObs(t, x, u, l, xMeas, A, b, c):
    
    dx = A @ x + b.flatten() * u(t) - l * (c.T.flatten() @ x - c.T.flatten()[0:4] @ xMeas)

    return dx