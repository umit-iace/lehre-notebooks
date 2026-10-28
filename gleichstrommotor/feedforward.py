# -*- coding: utf-8 -*-
import params as st
import numpy as np

def feedForwardStep(t0, wd):
    """stationäre Spannung für die Enddrehzahl als Sprung"""
    uS = (st.R * st.nu / st.k + st.k) * wd
    uIn = lambda t: uS if t >= t0 else 0
    return uIn

def trajectory(t, wd, t0, T):
    """Polynomiale Überführung phi_2 der Drehgeschwindigkeit und deren Ableitungen"""
    tau = np.clip((t - t0) / T, 0, 1)
    eta = wd * (10 * tau ** 3 - 15 * tau ** 4 + 6 * tau ** 5)
    if 0 < tau < 1:
        deta = wd / T * (30 * tau ** 2 - 60 * tau ** 3 + 30 * tau ** 4)
        ddeta = wd / T ** 2 * (60 * tau - 180 * tau ** 2 + 120 * tau ** 3)
    else:
        deta, ddeta = 0, 0
    return eta, deta, ddeta

def feedForwardFlat(t, wd, t0, T):
    """Flachheitsbasierte Steuerung mit flachem Ausgang omega"""
    w, dw, ddw = trajectory(t, wd, t0, T)
    i = (st.J * dw + st.nu * w) / st.k
    di = (st.J * ddw + st.nu * dw) / st.k
    u = st.LA * di + st.R * i + st.k * w
    return np.array([i, w]), u
