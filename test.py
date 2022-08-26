import numpy as np
import math as m
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def wufunc(r,S,T,t):
    u = (r**2)*S/(4*T*t)
    Wu=-0.5772-np.log(u)+u
    ntrm = 30
    for i in range (2, ntrm+1):
        sign = (-1)**(i-1)
    factval = float(m.factorial(i))
    Wu = Wu + sign*(u**i)/(i*factval)
    #End loop i
    return (Wu)
def myfunc(tt, T, S):
    pi = 3.14
    Q = 27.255 #m3/d
    r = 0.076 #m
    nrow = len(tt)
    n = nrow
    drawdown=np.zeros((n),float)
    for i in range (0,n):
        Wu_val=wufunc(r,S,T,tt[i])
    drawdown[i] = Q*Wu_val/(4*pi*T)
    #End loop i
    return (drawdown)
def main():
    indata = np.loadtxt("transducer.csv", delimiter=",")
    Times = np.copy(indata[:,0]) # Time from first column
    sobs = np.copy(indata[:,1]) # Drawdown from second column
    init_vals = [1, 0.00001] # for [T & S values]
    best_vals, covar = curve_fit(myfunc, Times, sobs, p0=init_vals, bounds=([0.01, 0.000001], [100000, 0.1]), method = 'trf')
    stdevs = np.sqrt(np.diag(covar))
    plt.xscale('log')
    plt.yscale('log')
    print ('Best valus (T, S)')
    print (best_vals)
    print ('Covariance')
    print (covar)
    print ('standard deviation')
    print (stdevs)
    plt.xscale('log')
    plt.yscale('log')
    T = best_vals [0]
    S = best_vals [1]
    smodel=myfunc(Times,T,S)
    plt.plot(Times,smodel)
    plt.plot(Times, sobs, 'bo')
    plt.xlabel("Time (day)")
    plt.ylabel("Drawdown (m)")
    plt.show()
main()