import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

cm = 1
v = -75

#Conductances, scale is in mS
gl = .3
gk = 36
gn = 120

#Voltages, scale is in mV
El = -54.387
Ek = -77
En = 50

#Starting n, m, h, 0<x<1, values found from PLOS journal
n = .3177
m = .0529
h = .5960

t = np.arange(0, 500, .001)
#####
#Gate Calculations
def alpha_beta_n(v):
    vn = v+55 #one calculation to skip two calculations
    an = (.01*vn)/(1-np.exp(-.1*vn))
    bn = .125*np.exp(-.0125*(v+65))
    return an, bn

def alpha_beta_m(v):
    vm = v+40 #one calculation to skip two calculations
    am = (.1*vm)/(1-np.exp(-.1*vm))
    bm = 4 * np.exp(-.0556*(v+65))
    return am, bm
    
def alpha_beta_h(v):
    ah = .07*np.exp(-.05*(v+65))
    bh = 1/(1+np.exp(-.1*(v+35)))
    return ah, bh

#General Equation for calculating the probability of each subunit activation
def gen_gate_deriv(ax, bx, x):
    dxdt = ax*(1-x)-bx*x
    return dxdt

def dndtC(v, n):
    an, bn = alpha_beta_n(v)
    dndt = gen_gate_deriv(an, bn, n)
    return dndt

def dmdtC(v, m):
    am, bm = alpha_beta_m(v)
    dmdt = gen_gate_deriv(am, bm, m)
    return dmdt

def dhdtC(v, h):
    ah, bh = alpha_beta_h(v)
    dhdt = gen_gate_deriv(ah, bh, h)
    return dhdt
#####

#Hodgkin-Huxley
def HHdvdt(v, n, m, h, eCurrent):
    dvdt = (eCurrent-gl*(v-El)-gk*(n**4)*(v-Ek)-gn*(m**3)*h*(v-En))/cm
    return dvdt

def equationset(gateset, t):
    v, n, m, h = gateset
    if t >= 250 and t <= 350:
        eCurrent = 2
    elif t >= 20 and t <= 120:
        eCurrent = 10
    elif t >= 140 and t <= 180:
        eCurrent = 4
    elif t >= 450:
        eCurrent = 1.25
    else:
        eCurrent = 0
    dvdt = HHdvdt(v, n, m, h, eCurrent)
    dndt = dndtC(v, n)
    dmdt = dmdtC(v, m)
    dhdt = dhdtC(v, h)
    return dvdt, dndt, dmdt, dhdt

X = odeint(equationset, [v, n, m, h], t)

v = X[:,0]
n = X[:,1]
m = X[:,2]
h = X[:,3]

fig, axs = plt.subplots(2,1, figsize = (10,6))

axs[0].set_title("Action Potential Voltage")
axs[0].plot(t, v, label = 'mV')
axs[0].set_ylabel('mV')

axs[1].set_title("n, m, h")
axs[1].plot(t, n, label = 'n')
axs[1].plot(t, m, label = 'm')
axs[1].plot(t, h, label = 'h')
axs[1].set_xlabel('ms')
axs[1].set_ylabel('Subunit Activation Probability')
axs[1].legend()

plt.show()