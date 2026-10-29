# -*- coding: utf-8 -*-
import params as st
import numpy as np
from model import outflow

def dOutflow(h, a, g):
    """Ableitung des Ausflusses nach dem Füllstand"""
    return a * g / np.sqrt(2 * g * h)

def trajectory(t, y0, yd, t0, T):
    """Polynomiale Überführung von y0 nach y0 + yd und deren Ableitungen"""
    tau = np.clip((t - t0) / T, 0, 1)
    y = y0 + yd * (10 * tau ** 3 - 15 * tau ** 4 + 6 * tau ** 5)
    if 0 < tau < 1:
        dy = yd / T * (30 * tau ** 2 - 60 * tau ** 3 + 30 * tau ** 4)
        ddy = yd / T ** 2 * (60 * tau - 180 * tau ** 2 + 120 * tau ** 3)
    else:
        dy, ddy = 0, 0
    return y, dy, ddy

def flatTrajectory(t, h10, dh1, t0, T):
    """Überführung von h2 zwischen den zu h1 = h10 und h1 = h10 + dh1 gehörenden Ruhelagen"""
    c = (st.a1 / st.a2) ** 2
    return trajectory(t, c * h10, c * dh1, t0, T)

def feedForwardIO(t, h10, dh1, t0, T):
    """Steuerung mit Ausgang y = h1 (r = 1), h2 folgt aus der internen Dynamik"""
    y, dy, _ = trajectory(t, h10, dh1, t0, T)
    u = st.A1 * dy + outflow(y, st.a1, st.g)
    return y, u

def feedForwardFlat(t, h10, dh1, t0, T):
    """Flachheitsbasierte Steuerung mit flachem Ausgang y = h2 (r = 2 = n)"""
    y, dy, ddy = flatTrajectory(t, h10, dh1, t0, T)
    q1 = st.A2 * dy + outflow(y, st.a2, st.g)
    dq1 = st.A2 * ddy + dOutflow(y, st.a2, st.g) * dy
    h1 = q1 ** 2 / (2 * st.g * st.a1 ** 2)
    dh1dt = q1 * dq1 / (st.g * st.a1 ** 2)
    u = st.A1 * dh1dt + q1
    return np.array([h1, y]), u

def feedBackIO(t, x, sR, ffArgs, integral=False):
    """Eingangs-Ausgangslinearisierung mit Fehlerdynamik de = sR e,
    mit I-Anteil x[2] = int e dt und doppeltem Eigenwert sR"""
    yr, dyr, _ = trajectory(t, *ffArgs)
    e = x[0] - yr
    if integral:
        v = dyr + 2 * sR * e - sR ** 2 * x[2]
    else:
        v = dyr + sR * e
    return st.A1 * v + outflow(x[0], st.a1, st.g)

def feedBackFlat(t, x, sR, ffArgs, integral=False):
    """Exakte Linearisierung mit flachem Ausgang y = h2, doppelter Eigenwert sR der Fehlerdynamik,
    mit I-Anteil x[2] = int e dt und dreifachem Eigenwert sR"""
    yr, dyr, ddyr = flatTrajectory(t, *ffArgs)
    q1 = outflow(x[0], st.a1, st.g)
    dy = (q1 - outflow(x[1], st.a2, st.g)) / st.A2
    e, de = x[1] - yr, dy - dyr
    if integral:
        v = ddyr + 3 * sR * de - 3 * sR ** 2 * e + sR ** 3 * x[2]
    else:
        v = ddyr + 2 * sR * de - sR ** 2 * e
    return q1 + st.A1 * (st.A2 * v + dOutflow(x[1], st.a2, st.g) * dy) / dOutflow(x[0], st.a1, st.g)
