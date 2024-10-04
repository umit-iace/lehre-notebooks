# -*- coding: utf-8 -*-

def nonlinSys(t, x, u, params):
    cs = np.cos(x[0]);
    sn = np.sin(x[0]);

    g, M, m , l = params

    dx = np.zeros(4)

    h = l * x[1] ** 2 + g * cs;
    dx[0] = x[1];
    dx[2] = x[3];
    dx[3] = (u(t) + m * sn * h) / (M + m * sn ** 2);
    dx[1] = -(dx[3] * cs + g * sn) / l;

    return dx

def linSys(t, x, u, params):
    g, M, m , l = params

    dx = np.zeros(4)
    dx[0] = x[1];
    dx[2] = x[3];
    dx[3] = (u(t) + m * g * x[0]) / M;
    dx[1] = (-dx[3] - g * x[0]) / l;

    return dx


def linRedSys(t, x, u, params):
    g, M, m , l = params

    dx = np.zeros(2)
    dx[0] = x[1]
    dx[1] = g * (u(t) - x[0]) / l

    return dx

