# -*- coding: utf-8 -*-
import params as st
import numpy as np
from model import outflow

def trajectory(t, y0, yd, t0, T):
    """Polynomiale Überführung des Füllstands von y0 nach y0 + yd und deren Ableitung"""
    tau = np.clip((t - t0) / T, 0, 1)
    y = y0 + yd * (10 * tau ** 3 - 15 * tau ** 4 + 6 * tau ** 5)
    if 0 < tau < 1:
        dy = yd / T * (30 * tau ** 2 - 60 * tau ** 3 + 30 * tau ** 4)
    else:
        dy = 0
    return y, dy

def feedForward(t, y0, yd, t0, T):
    """Steuerung aus der nach u umgestellten ersten Ausgangsableitung (r = 1)"""
    y, dy = trajectory(t, y0, yd, t0, T)
    u = st.A1 * dy + outflow(y, st.a1, st.g)
    return y, u

def feedBack(t, h1, k, y0, yd, t0, T):
    """Eingangs-Ausgangslinearisierung mit Fehlerdynamik de = -k e"""
    yr, dyr = trajectory(t, y0, yd, t0, T)
    v = dyr - k * (h1 - yr)
    return st.A1 * v + outflow(h1, st.a1, st.g)
