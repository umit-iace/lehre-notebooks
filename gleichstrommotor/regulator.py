# -*- coding: utf-8 -*-
import numpy as np

def acker(A, b, poles):
    """Ackermannformel für ein System mit einem Eingang"""
    n = A.shape[0]
    S = np.column_stack([np.linalg.matrix_power(A, i) @ b for i in range(n)])
    coeff = np.real(np.poly(poles))
    pA = sum(ci * np.linalg.matrix_power(A, n - i) for i, ci in enumerate(coeff))
    q = np.linalg.solve(S.T, np.eye(n)[:, -1])
    return q @ pA

def exosystem(wL):
    Aex = np.array([[0, 0, 0],
                    [0, 0, wL],
                    [0, -wL, 0]])
    Cex = np.array([[1, 1, 0]])
    return Aex, Cex

def disturbance(t, d0, d1, wL, td0, td1):
    """Zustand des Exosystems: konstanter Anteil ab td0, harmonischer Anteil ab td1"""
    return np.array([d0 if t >= td0 else 0,
                     d1 * np.sin(wL * (t - td1)) if t >= td1 else 0,
                     d1 * np.cos(wL * (t - td1)) if t >= td1 else 0])

def regulator(A, b, c, P, Q, Aex, Cex):
    """Lösung der Regulatorgleichungen
        A Pi + b gamma^T + P Cex = Pi Aex
        c^T Pi + Q Cex = 0
    durch Vektorisierung mit dem Kronecker-Produkt"""
    n = A.shape[0]
    nz = Aex.shape[0]
    B = b.reshape(-1, 1)
    C = c.reshape(1, -1)
    M = np.block([[np.kron(np.eye(nz), A) - np.kron(Aex.T, np.eye(n)), np.kron(np.eye(nz), B)],
                  [np.kron(np.eye(nz), C), np.zeros((nz, nz))]])
    rhs = -np.concatenate([(P @ Cex).flatten(order='F'), (Q @ Cex).flatten(order='F')])
    sol = np.linalg.solve(M, rhs)
    Pi = sol[:n * nz].reshape((n, nz), order='F')
    gamma = sol[n * nz:]
    return Pi, gamma
