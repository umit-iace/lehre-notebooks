# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.ticker as mticker
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.lines import Line2D

from feedforward import feedForwardLinFlat
import params as st

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
"""


def generateFeedForwardPlot(t, t0, T, yd, N):
    yr, uIn, Dr, thetar = feedForwardLinFlat(t0, T, yd)
    tRed = np.linspace(t[0], t[-1], N)

    fig = plt.figure(figsize=(16, 5))

    gs = gridspec.GridSpec(1, 3, width_ratios=[1, 2, 1], wspace=0.125, hspace=0.075)

    axes10 = plt.Subplot(fig, gs[0])
    axes20 = plt.Subplot(fig, gs[1])
    axes30 = plt.Subplot(fig, gs[2])

    axes10.plot(t, [yr[0](_t) for _t in t], 'C1-')
    axes30.plot(t, [Dr(_t) for _t in t], 'C1-')

    axes10.set_xlabel(r'$t$ in \si{\second}')
    axes20.set_xlabel(r'$z$ in \si{\meter}')
    axes30.set_xlabel(r'$t$ in \si{\second}')

    axes20.set_xlim(0 - 0.1, 1 + 0.1)
    axes20.set_ylim(-st.l - 2 * st.r, 2 * st.h)

    c = np.linspace(tRed[0], tRed[-1], N)
    norm = mpl.colors.Normalize(vmin=c[0], vmax=c[-1])
    cmap = mpl.cm.ScalarMappable(norm=norm, cmap=mpl.cm.viridis)
    cmap.set_array([])

    for j, _t in enumerate(tRed):
        curCol = cmap.to_rgba(j / (N - 1) * (c[-1] - c[0]) + c[0])

        wagen = mpl.patches.Rectangle(
                xy=(Dr(_t) - st.b/2, 0),
                width=st.b,
                height=st.h,
                color=curCol, zorder=j + 1)
        last = mpl.patches.Circle(
                xy=(yr[0](_t), -np.cos(thetar(_t)) * st.l),
                radius=st.r,
                color=curCol,
                zorder=j + 1)
        seil = Line2D(
                [Dr(_t), yr[0](_t)],
                [0, -np.cos(thetar(_t)) * st.l],
                color=curCol,
                linewidth=2,
                zorder=j + 1)

        axes20.add_patch(wagen)
        axes20.add_line(seil)
        axes20.add_patch(last)

    divider = make_axes_locatable(axes20)
    cbaxes = divider.append_axes("top", size="3%", pad=0.05)
    cbar = fig.colorbar(cmap, cax=cbaxes, ticks= mticker.AutoLocator(), orientation="horizontal")
    cbar.ax.xaxis.set_ticks_position('top')
    cbar.ax.xaxis.set_label_position('top')
    cbar.set_label(r"$t$ in \si{\second}")

    axes10.grid(True)
    axes20.grid(True)
    axes30.grid(True)

    [label.set_visible(False) for label in axes20.get_yticklabels()]

    fig.add_subplot(axes10)
    fig.add_subplot(axes20)
    fig.add_subplot(axes30)
    fig.align_labels()

    fig.savefig('kranSteuerung.pdf',
                format='pdf', dpi=600, bbox_inches='tight', transparent=True)


if __name__ == '__main__':
    t = np.linspace(0, 5, 150)
    yd = 1
    t0 = 0.5
    T = 4
    N = 10
    generateFeedForwardPlot(t, t0, T, yd, N)
