import math
import numpy as np

def cal_fuction(ZL, Z0, Zs, Vs, L, z, alpha, f):
    lamda = 3*10**8/f
    L = L*lamda
    z = z*lamda
    beta = 2*np.pi/lamda
    gamma = complex(alpha,beta)
    gamma = complex(alpha,beta)
    gamma_L = (ZL-Z0)/(ZL+Z0)
    gamma_In = gamma_L*np.exp(-2*gamma*L)
    gamma_Z = gamma_L*np.exp(-2*gamma*(L-z))
    Z_In = Z0*(1+gamma_In)/(1-gamma_In)
    V_In = Vs*Z_In/(Z_In+Zs)
    V_cong = V_In/(1+gamma_In)
    V_tru = gamma_In*V_cong

    V_temp = V_cong*np.exp(-gamma*z) + V_tru*np.exp(gamma*z)
    V = complex(round(V_temp.real,3), round(V_temp.imag,3))
    
    I_temp = V_cong*np.exp(-gamma*z)/Z0 - V_tru*np.exp(gamma*z)/Z0
    I = complex(round(I_temp.real,3), round(I_temp.imag,3))

    Pinc =  ((np.abs(V_cong))**2)*np.exp(-2*alpha*z)/(2*Z0)


    Pref = Pinc*(np.abs(gamma_Z))**2
    

    Ptrans = Pinc - Pref
    

    return str(V), str(I), str(Pinc), str(Pref), str(Ptrans)
