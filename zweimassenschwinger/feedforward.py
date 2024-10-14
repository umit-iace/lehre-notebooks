# -*- coding: utf-8 -*-
import params as st
import sympy as sp
import numpy as np

def feedForwardRamp(t0, T, yd):
    uIn = lambda t: yd if t0 < t < t0 + T else 0
    return uIn
