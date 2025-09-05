# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.ticker as mticker
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.lines import Line2D

mpl.use('pgf')

mpl.rcParams["pgf.texsystem"] = "pdflatex"
mpl.rcParams["text.usetex"] = True
mpl.rcParams["font.family"] = "lmodern"
mpl.rcParams["font.serif"] = []
mpl.rcParams["font.monospace"] = []
mpl.rcParams["axes.labelsize"] = 16
mpl.rcParams["axes.unicode_minus"] = False
mpl.rcParams["font.size"] = 14
mpl.rcParams["legend.fontsize"] = 14
mpl.rcParams["xtick.labelsize"] = 16
mpl.rcParams["ytick.labelsize"] = 16
mpl.rcParams["pgf.preamble"] = r"""
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{chemformula}
\usepackage{bm}
\usepackage[per-mode=symbol]{siunitx}
\definecolor{blauC}{HTML}{1f77b4}
\definecolor{orangeC}{HTML}{ff7f0e}
"""


def generateTrapezPlots():
    aMax = 1
    vMax = 1
    y3 = 2

    t1 = vMax / aMax
    y1 = aMax * t1 ** 2 / 2

    t2 = (y3 - 2 * y1) / vMax + t1
    t3 = t1 + t2

    _t1 = np.linspace(0, t1, 101)

    fig = plt.figure(figsize=(14, 7))

    gs = gridspec.GridSpec(3, 1, height_ratios=[1, 1, 1], hspace=0.075)

    ax1 = plt.Subplot(fig, gs[0])
    ax2 = plt.Subplot(fig, gs[1], sharex=ax1)
    ax3 = plt.Subplot(fig, gs[2], sharex=ax1)

    ax1.grid(True)
    ax2.grid(True)
    ax3.grid(True)

    [label.set_visible(False) for label in ax1.get_xticklabels()]
    [label.set_visible(False) for label in ax2.get_xticklabels()]

    ax3.set_xlim(0, t3)
    ax3.set_xticks([0, t1, t2, t3])
    ax3.set_xticklabels([r"$0$", r"$t_1$", r"$t_2$", r"$t_3$"])

    ax1.set_ylim([-aMax - np.abs(aMax) * 0.1, aMax + np.abs(aMax) * 0.1])
    ax1.set_yticks([-aMax, 0, aMax])
    ax1.set_yticklabels([r"$-a_{\text{max}}$", r"$0$", r"$a_{\text{max}}$"])
    ax2.set_ylim([-np.abs(vMax) * 0.1, vMax + np.abs(aMax) * 0.1])
    ax2.set_yticks([0, vMax])
    ax2.set_yticklabels([r"$0$", r"$v_{\text{max}}$"])
    ax3.set_ylim([-np.abs(y3) * 0.1, y3 + np.abs(y3) * 0.1])
    ax3.set_yticks([0, y1, y3 - y1, y3])
    ax3.set_yticklabels([r"$0$", r"$y_1$", r"$y_2$", r"$y_3$"])

    fig.add_subplot(ax1)
    fig.add_subplot(ax2)
    fig.add_subplot(ax3)

    ax1.plot([0, t1], [aMax, aMax], 'C0')

    ax2.plot([0, t1], [0, vMax], 'C0')

    ax3.plot(_t1, _t1 ** 2 / 2 * aMax, 'C0')

    fig.savefig('trapez1.pdf',
                format='pdf', dpi=600, bbox_inches='tight', transparent=True)

    ax1.plot([0, t1], [aMax, aMax], 'C0')
    ax1.plot([t1, t1], [aMax, 0], 'C0')
    ax1.plot([t1, t2], [0, 0], 'C0')

    ax2.plot([0, t1], [0, vMax], 'C0')
    ax2.plot([t1, t2] ,[vMax, vMax], 'C0')

    ax3.plot(_t1, _t1 ** 2 / 2 * aMax, 'C0')
    ax3.plot([t1, t2], [aMax* (t1 ** 2.0) / 2, (t1 **2 ) / 2 * aMax + (t2 - t1) * vMax], 'C0')

    fig.savefig('trapez2.pdf',
                format='pdf', dpi=600, bbox_inches='tight', transparent=True)

    ax1.plot([0, t1], [aMax, aMax], 'C0')
    ax1.plot([t1, t1], [aMax, 0], 'C0')
    ax1.plot([t1, t2], [0, 0], 'C0')
    ax1.plot([t2, t2], [0, -aMax], 'C0')
    ax1.plot([t2, t3], [-aMax, -aMax], 'C0')

    ax2.plot([0, t1], [0, vMax], 'C0')
    ax2.plot([t1, t2] ,[vMax, vMax], 'C0')
    ax2.plot([t2, t3] ,[vMax, 0], 'C0')

    ax3.plot(_t1, _t1 ** 2 / 2 * aMax, 'C0')
    ax3.plot([t1, t2], [aMax* (t1 ** 2.0) / 2, (t1 **2 ) / 2 * aMax + (t2 - t1) * vMax], 'C0')
    ax3.plot(t2 + _t1, aMax*(t1 ** 2.0) / 2 + (t2 - t1 + _t1) * vMax - aMax * _t1 ** 2 / 2, 'C0')

    fig.savefig('trapez3.pdf',
                format='pdf', dpi=600, bbox_inches='tight', transparent=True)

def generateSCurvePlot():
    Ts = 0.05
    T = 50e-6

    aMax = 20.0
    vMax = 2.0
    sMax = 0.4
    jMax = aMax / Ts

    if sMax == 0:
        s = [0, 0]
        v = a = j = s
        t = np.linspace(0, T, 101)
    else:
        tC = vMax / aMax
        tB = np.sqrt(sMax / aMax)
        tQ = np.minimum(tB, tC)
        tU = sMax / vMax - tC;
        tW = np.maximum(tU,0);
        tJ = np.minimum(Ts,tQ)
        kJ = np.ceil(tJ / T)
        tR = tQ + tW
        kR = np.ceil(tR / T)
        tF = tQ + Ts - tJ
        kF = np.ceil(tF / T)
        kMax = kJ + kR + kF
        j0 = sMax / kJ / kR / kF / T ** 3
        tA = tJ + vMax / aMax
        tV = sMax / vMax - tA

        j = []
        a = []
        v = []
        s = []
        x1 = x2 = x3 = 0
        c1 = T
        c2 = T ** 2 / 2
        c3 = T ** 3 / 6

        for k in range(int(kMax)):
            uk = 0;
            if 0 <= k and k < kJ:
                uk = uk + 1
            if kR <= k and k < (kR + kJ):
                uk = uk - 1
            if kF <= k and k < (kF + kJ):
                uk = uk - 1
            if kF + kR <= k and k < kMax:
                uk = uk + 1

            jk = uk * j0
            ak = c1 * x1 * j0
            vk = c2 * x2 * j0
            sk = c3 * x3 * j0

            x3 = 3 * x1 + 3 * x2 + x3 + uk
            x2 = 2 * x1 + x2 + uk
            x1 = x1 + uk
            j.append(jk)
            a.append(ak)
            v.append(vk)
            s.append(sk)

        t = np.linspace(0, kMax * T, int(kMax))

    fig = plt.figure(figsize=(14, 7))

    gs = gridspec.GridSpec(4, 1, height_ratios=[1, 1, 1, 1], hspace=0.075)

    ax1 = plt.Subplot(fig, gs[0])
    ax2 = plt.Subplot(fig, gs[1], sharex=ax1)
    ax3 = plt.Subplot(fig, gs[2], sharex=ax1)
    ax4 = plt.Subplot(fig, gs[3], sharex=ax1)

    ax1.plot(t, j)
    ax2.plot(t, a)
    ax3.plot(t, v)
    ax4.plot(t, s)

    ax1.grid(True)
    ax2.grid(True)
    ax3.grid(True)
    ax4.grid(True)

    [label.set_visible(False) for label in ax1.get_xticklabels()]
    [label.set_visible(False) for label in ax2.get_xticklabels()]
    [label.set_visible(False) for label in ax3.get_xticklabels()]

    ax3.set_xlim(0, t[-1])
    ax3.set_xticks([0, tJ, tA, tA + tV, kMax * T])
    ax3.set_xticklabels([r"$0$", r"$T_{\text{j}}$", r"$T_{\text{a}}$", r"$T_{\text{a}} + T_{\text{v}}$", r"$T$"])

    ax1.set_yticks([-jMax, 0, jMax])
    ax1.set_yticklabels([r"$-j_{\text{max}}$", r"$0$", r"$j_{\text{max}}$"])
    ax2.set_yticks([-aMax, 0, aMax])
    ax2.set_yticklabels([r"$-a_{\text{max}}$", r"$0$", r"$a_{\text{max}}$"])
    ax3.set_yticks([0, vMax])
    ax3.set_yticklabels([r"$0$", r"$v_{\text{max}}$"])
    ax4.set_yticks([0, sMax])
    ax4.set_yticklabels([r"$0$", r"$y_T$"])

    fig.add_subplot(ax1)
    fig.add_subplot(ax2)
    fig.add_subplot(ax3)
    fig.add_subplot(ax4)

    fig.savefig('scurve.pdf',
                format='pdf', dpi=600, bbox_inches='tight', transparent=True)


if __name__ == '__main__':
    generateTrapezPlots()
    # generateSCurvePlot()
