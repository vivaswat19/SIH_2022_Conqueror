from functools import partial
import numpy as np
from numpy import *
from scipy.integrate import quad
from scipy.integrate import odeint
from scipy.special import *
import sys

class DataSet:
    
    def __init__(self,filepath):
        # pumping test data (time and drawdown arrays)
        self.t = []
        self.tr2 =[]
        self.s = []
        lineInput = []        
        inputFile = open(filepath,'r')
        for line in inputFile: lineInput.append(line.split(','))
        inputFile.close()
        for i in range(1, len(lineInput)):
            self.t.append(float(lineInput[i][0]))
            self.s.append(float(lineInput[i][1]))
        self.t = array(self.t)
        self.s = array(self.s)
        print('Read test data set.')
    def setTr2Array(self,r):
        for i in self.t:
            self.tr2.append(i/r**2)
        self.tr2=array(self.tr2)


class Aquifer:
    
    def __init__(self):
        # aquifer characteristics
        lineInput = []        
        inputFile = open('aquifer.txt','r')
        for line in inputFile: lineInput.append(line.split())
        inputFile.close()
        self.K = float(lineInput[0][1])     # aquifer properties
        self.Ss = float(lineInput[1][1])
        self.Sy = float(lineInput[2][1])
        self.b = float(lineInput[3][1])     # used as saturated thickness for unconfined aquifer
        self.bc = float(lineInput[4][1])        
        self.Kc = float(lineInput[5][1])    # 'c' refers to clay/aquitard
        self.Ssc = float(lineInput[6][1])
        self.S = self.Ss * self.b           # derive storage coefficient from specific storage
        self.T=self.K*self.b       
        
class Well:
    
    def __init__(self, t0, tEnd):
        # well properties
        lineInput = []        
        inputFile = open("well.txt",'r')
        for line in inputFile: lineInput.append(line.split())
        inputFile.close()
        self.r = float(lineInput[0][1])     # well radius; assume radial distance for monitoring drawdown
        self.rArray = np.linspace(0,1,60)
        self.Q = float(lineInput[1][1])     # pumping rate from well (negative value = extraction)
        self.tArray = logspace(log10(t0), log10(tEnd), num=60, endpoint=True)     # evaluation times    
        self.tr2Array = logspace(log10(t0/(self.r)**2), log10(tEnd/(self.r)**2), num=60, endpoint=True)
        self.rootTArray = logspace(log10(t0)/2.0, log10(tEnd)/2.0, num=60, endpoint=True)
        self.fourthRootTArray = logspace(log10(t0)/4.0, log10(tEnd)/4.0, num=60, endpoint=True)

    def WriteValues(self):
        # update parameter file with current values
        output_file = open('well.txt','w')
        output_file.writelines(['r', '\t', str(self.r),'\n'])
        output_file.writelines(['Q', '\t', str(self.Q),'\n'])
        output_file.close()     

        
class Hantush:            # Hantush and Jacob (1955) solution

    def __init__(self, aquifer, well):
        self.B = sqrt(aquifer.bc*aquifer.K*aquifer.b/aquifer.Kc)
        self.aquifer = aquifer
        self.well = well

    def Integrand(self, y):
        # integral term for the Hantush well function
        x = exp(-y - self.well.r**2/(4.*self.B**2*y))/y
        return x

    def W(self, u):
        # Hantush well function
        x = quad(self.Integrand, u, +inf)[0]
        return x
        
    def Drawdown(self,flag):
        if flag==0:
            s = zeros(len(self.well.tArray), float)
        elif flag==1:
            s = zeros(len(self.well.tr2Array), float)
        else:
            s = zeros(len(self.well.rArray), float)

        if flag==0:
            for i, t in enumerate(self.well.tArray):        
                u = self.well.r**2*self.aquifer.Ss/(4*self.aquifer.K*t)
                s[i] = -self.well.Q/(4*pi*self.aquifer.K*self.aquifer.b) * self.W(u)
        elif flag==1:
            for i, tr in enumerate(self.well.tr2Array):        
                u = self.aquifer.Ss/(4*self.aquifer.K*tr)
                s[i] = -self.well.Q/(4*pi*self.aquifer.K*self.aquifer.b) * self.W(u)
        elif flag==2:
            for i, r in enumerate(self.well.rArray):        
                u = r**2*self.aquifer.Ss/(4*self.aquifer.K*self.well.tArray[1])
                s[i] = -self.well.Q/(4*pi*self.aquifer.K*self.aquifer.b) * self.W(u)
        return s

        
class ShortStorage:            # Hantush (1960) solution for leaky aquifer with aquitard storage (short-term)

    def __init__(self, aquifer, well):
        self.beta = sqrt(aquifer.Kc*aquifer.Ssc/(aquifer.K*aquifer.Ss)) * 4.0*well.r/aquifer.b
        self.aquifer = aquifer
        self.well = well

    def Integrand(self, y, u):
        # integral term for the Hantush well function
        x = erfc(self.beta*sqrt(u)/sqrt(y*(y-u))) * exp(-y)/y
        return x

    def H(self, u):
        # Hantush modified well function
        x = quad(self.Integrand, u, +inf, args=(u))[0]
        return x
        
    def Drawdown(self,flag):

        if flag==0:
            s = zeros(len(self.well.tArray), float)
        elif flag==1:
            s = zeros(len(self.well.tr2Array), float)
        else:
            s = zeros(len(self.well.rArray), float)

        if flag==0:
            for i, t in enumerate(self.well.tArray):        
                u = self.well.r**2*self.aquifer.Ss/(4*self.aquifer.K*t)
                s[i] = -self.well.Q/(4*pi*self.aquifer.K*self.aquifer.b) * self.H(u)
        elif flag==1:
             for i, tr in enumerate(self.well.tr2Array):        
                u = self.aquifer.Ss/(4*self.aquifer.K*tr)
                s[i] = -self.well.Q/(4*pi*self.aquifer.K*self.aquifer.b) * self.H(u)
        elif flag==2:
             for i, r in enumerate(self.well.rArray):        
                u = r**2*self.aquifer.Ss/(4*self.aquifer.K*self.well.tArray[1])
                s[i] = -self.well.Q/(4*pi*self.aquifer.K*self.aquifer.b) * self.H(u)
        return s        

        
class Theis:    # Theis (1935) solution

    def __init__(self, aquifer, well):
        self.aquifer = aquifer
        self.well = well
        
    def W(self, u):
        # Theis well function
        return expn(1, u)        

    def Drawdown(self, mode,flag):
        if flag == 0:
            s = zeros(len(self.well.tArray), float)
        elif flag == 1:
            s = zeros(len(self.well.rArray), float)
        else:
            s = zeros(len(self.well.tr2Array), float)
        if flag==0:
            if mode == 0:       # confined aquifer
                for i, t in enumerate(self.well.tArray):    
                    u = self.well.r**2 * self.aquifer.Ss/(4*self.aquifer.K*t)
                    s[i] = -self.well.Q/(4*pi*self.aquifer.K*self.aquifer.b) * self.W(u)
            else:               # unconfined aquifer (assuming ~ constant saturated thickness)
                for i, t in enumerate(self.well.tArray):    
                    u = self.well.r**2 * self.aquifer.Sy/(4*self.aquifer.K*self.aquifer.b*t)
                    s[i] = -self.well.Q/(4*pi*self.aquifer.K*self.aquifer.b) * self.W(u)      
        elif flag == 1:
            if mode == 0:
                for i,r in enumerate(self.well.rArray):
                    u = r**2 * self.aquifer.Ss/(4*self.aquifer.K*self.well.tArray[1])
                    s[i] = -self.well.Q/(4*pi*self.aquifer.K*self.aquifer.b) * self.W(u)
            else:
                for i, r in enumerate(self.well.rArray):    
                    u = r**2 * self.aquifer.Sy/(4*self.aquifer.K*self.aquifer.b*self.well.tArray[1])
                    s[i] = -self.well.Q/(4*pi*self.aquifer.K*self.aquifer.b) * self.W(u)
        elif flag==2:
            if mode == 0:
                for i,tr2 in enumerate(self.well.tr2Array):
                    u = self.aquifer.Ss/(4*self.aquifer.K*tr2)
                    s[i] = -self.well.Q/(4*pi*self.aquifer.K*self.aquifer.b) * self.W(u)
            else:
                for i,tr2 in enumerate(self.well.tr2Array):
                    u = self.aquifer.Sy/(4*self.aquifer.K*self.aquifer.b*tr2)
                    s[i] = -self.well.Q/(4*pi*self.aquifer.K*self.aquifer.b) * self.W(u)

        return s
       

class MOL:  # numerical (method-of-lines) solution for an unconfined aquifer
    
    def __init__(self, aquifer, well):
        self.aquifer = aquifer
        self.well = well
        self.N = 70                                                 # default number of radial grid cells       
        self.rFace = self.Gridder()                                 # array of grid cell interface radii
        self.r = 0.5*self.rFace[1:] + 0.5*self.rFace[:-1]           # radius of node point associated with each cell
        self.r = insert(self.r, 0, self.well.r)                     # cell representing well
        self.A = pi*(self.rFace[1:]**2 - self.rFace[:-1]**2)      # base areas associated with individual grid cells
        self.A = insert(self.A, 0, pi*self.rFace[0]**2)
        self.Sy = zeros(self.N, float) + aquifer.Sy                 # assign storage coefficient of 1.0 to wellbore cell
        self.Sy = insert(self.Sy, 0, 1.0)
        self.S = zeros(self.N, float) + aquifer.S
        self.S = insert(self.S, 0, 1.0)       
    
    def Gridder(self):
        # generate radial grid
        rb = self.aquifer.b * 100.                   # set fixed boundary condition = 10X the available drawdown        
        index = arange(0, self.N+1, 1)
        f = 10.**(log10((rb/self.well.r))/self.N)   # sequential scaling factor
        r = self.well.r * f**index
        return r

    def Dupuit(self, h, t):
        # ordinary differential equations (volumetric balance for water) for grid cells; variable saturated thickness
        J = 2. * pi * self.aquifer.K * self.rFace[:-1] * (0.5*h[1:] + 0.5*h[:-1]) * (h[1:] - h[:-1]) / (self.r[1:] - self.r[:-1])
        J = insert(J, 0, -self.well.Q)  
        J = append(J, 2.*pi*self.aquifer.K*self.rFace[-1]*(0.5*h[-1]+0.5*self.aquifer.b)    
            *(self.aquifer.b-h[-1])/(self.rFace[-1]-self.r[-1]))            # append flux from across exterior boundary
        dhdt = (J[1:] - J[:-1]) / (self.A * self.Sy)
        return dhdt       
    
    def Theis(self, h, t):
        # ordinary differential equations (volumetric balance for water) for grid cells; fixed saturated thickness
        J = 2. * pi * self.aquifer.K * self.rFace[:-1] * self.aquifer.b * (h[1:] - h[:-1]) / (self.r[1:] - self.r[:-1])
        J = insert(J, 0, -self.well.Q)                                      # express pumping as extraction from well
        J = append(J, 2.*pi*self.aquifer.K*self.rFace[-1]*self.aquifer.b
            *(self.aquifer.b-h[-1])/(self.rFace[-1]-self.r[-1]))            # append flux from across exterior boundary
        dhdt = (J[1:] - J[:-1]) / (self.A * self.S)
        return dhdt 
    
    def Drawdown(self, mode):
        # solve the transient unconfined aquifer test problem using the numerical method-of-lines
        h = zeros(self.N+1,float) + self.aquifer.b
        if mode == 0: h_t = odeint(self.Dupuit, h, self.well.tArray)
        else: h_t = odeint(self.Theis, h, self.well.tArray)
        h_t = transpose(h_t)
        s = self.aquifer.b - h_t[0]         # drawdown vector for cell representing well bore
        return s         