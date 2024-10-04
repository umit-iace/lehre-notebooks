# -*- coding: utf-8 -*-

def fkt_phi(tau,n=0):
    tau = np.atleast_1d(tau)
    res = np.zeros_like(tau)
    ind_m = np.logical_and(tau >= 0, tau <= 1)
    #n=n+2
    if(n == 0):
        ind_e = tau > 1
        res[ind_m] = (35-84*tau[ind_m]+70*tau[ind_m]**2-20*tau[ind_m]**3) * tau[ind_m]**4
        res[ind_e] = 1.
    elif(n == 1):
        res[ind_m] = 140*(1-3*tau[ind_m]+3*tau[ind_m]**2-tau[ind_m]**3) * tau[ind_m]**3
    elif(n == 2):
        res[ind_m] = 420*(1-4*tau[ind_m]+5*tau[ind_m]**2-2*tau[ind_m]**3) * tau[ind_m]**2
    elif(n == 3):
        res[ind_m] = 840*(1-6*tau[ind_m]+10*tau[ind_m]**2-5*tau[ind_m]**3) * tau[ind_m]
    elif(n == 4):
        res[ind_m] = 840*(1-12*tau[ind_m]+30*tau[ind_m]**2-20*tau[ind_m]**3)
    return res
