import numpy as np
from numpy import *
import pandas as pd
from scipy.integrate import quad
from scipy.integrate import odeint
from scipy.special import *
import sys
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from scipy.optimize import curve_fit
import math as m
import matplotlib.pyplot as plt
from scipy.stats import linregress

class CooperJacob:
    def __init__(self, filepath,q,r):
        df = pd.read_csv(filepath)
        self.s=df['S'].to_numpy()
        self.t=df['T'].to_numpy()
        self.Q=q
        self.r=r
    
    def Values(self):
        reg = linregress(self.t, self.s)
        delta_s = reg.slope
        # score=reg.score(self.t.reshape(-1, 1), self.s)
        # print(score)
        # delta_s=reg.predict([[100]])-reg.predict([[10]])
        T=2.303*self.Q/4*np.pi*delta_s
        S=2.25*T*reg.predict([[0]])/self.r**2

        intercept = 2.3*self.Q*np.log(S)/(4*3.14*T)
        slope = 2.3*self.Q/(4*3.14*T)

        y = intercept+slope*np.log(self.t)
        
        return self.t,y,self.s,T,S

obj = CooperJacob('./transducer.csv',27.255,0.076)

obj.Values()

# plt.plot(a,b)
# plt.show()

# print(d,e)