#import scipy
from scipy import integrate
import ChargeDistribution as ChDist
import matplotlib.pyplot as plt
import numpy as np

rho = ChDist.ChargeDistribution()
#plt.figure(3)
#rho.show(title='title',disp=False)

#define ODE
def dE(x,y):
	return rho.evaluate(x)
	#return np.cos(x)
	
X = np.arange(-2.0,2.0,0.01)

#plot(X,f(X))
print enumerate(X)

def F(x):
    res = np.zeros_like(x)
    for i,val in enumerate(x):
        y,err = integrate.dblquad(dE,0,val,lambda x:0,lambda x:val)
        res[i]=y
    return res
    
plt.plot(X,F(X))
plt.show()
