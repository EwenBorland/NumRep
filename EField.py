import numpy as np
import matplotlib.pyplot as plt
from time import sleep
import ChargeDistribution as ChDist


#setup charge distribution
rho = ChDist.ChargeDistribution()
#rho.show(title='title',disp=True)

#define ODE
def dE(x):
	return rho.evaluate(x)
	#return np.cos(x)


#Euler method for next y value
def Euler_next_y(yn_0, xn_0, func, step):
	return (yn_0 + step*(func(xn_0)))

def step_RK4(x0,y0,func,stepsize):
	k1 = func(x0)
	k2 = func(x0 + stepsize/2)
	k3 = func(x0 + stepsize/2)
	k4 = func(x0 + stepsize)
	y1 = y0 + stepsize*(k1/6 + k2/3 + k3/3 + k4/6)
	return y1

ncount = 40
xminmax= [-2.0,2.0]
stepsize = (xminmax[1] - xminmax[0])/ncount
init = [-2.0,0.0]
##bit to split the whole range (xmin,xmax) into two list, one left of the initialx and the other to the right
r = np.linspace(min(xminmax),max(xminmax),ncount)
for i in range(len(r)):
	if r[i] >= init[0]:
		print i
		leftlist = r[0:i]
		rightlist = r[i:]
		break
#the loop
y_vals = [init[1]]
x_vals = [init[0]]
x_vals2 = [init[0]]
y_vals2 = [init[1]]
n=0
for n in range(len(rightlist)):
	y_n = y_vals[n]
	x_n = x_vals[n]
	#y_vals.append(Euler_next_y(y_n,x_n,dE,stepsize))
	y_vals.append(step_RK4(x_n,y_n,dE,stepsize))
	x_vals.append(x_n + stepsize)
	n+=1
	
for n in range(len(rightlist)):
	y_n = y_vals2[n]
	x_n = x_vals2[n]
	y_vals2.append(Euler_next_y(y_n,x_n,dE,stepsize))
	#y_vals2.append(step_RK4(x_n,y_n,dE,stepsize))
	x_vals2.append(x_n + stepsize)
	n+=1	
	
	
'''
for n in range(len(leftlist)):
	y_n = y_vals[0]
	x_n = x_vals[0]
	#y_vals.insert(0,Euler_next_y(y_n,x_n,dE,-stepsize))
	y_vals.insert(0,step_RK4(y_n,x_n,dE,-stepsize))
	x_vals.insert(0,x_n-stepsize)
	n+=1
'''
diffx = []
diffy = []
for i in range(len(x_vals)):
	diffx.append(abs(x_vals[i]-x_vals2[i]))
	diffy.append(abs(y_vals[i]-y_vals2[i]))

####plotting garbage
plt.plot(x_vals,y_vals,'r-')
plt.plot(x_vals,diffy,'y-')
plt.plot(x_vals2,y_vals2,'g-')
plt.plot([0,0],[0,0.6],'b-')
#print max(diffx)
#print max(diffy)

plt.show()
