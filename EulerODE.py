import numpy as np
import matplotlib.pyplot as plt
from time import sleep

#test functions
def dy_dx(x):
	#return (1 - 6*x + 3*(x**2))
	return np.cos(x)
	#return np.exp(x)


#euler method for getting next y value	
def next_y(yn_0, xn_0, func, step):
	return (yn_0 + step*(func(xn_0)))

# total steps, x range, stepsize
ncount = 100
xminmax= [0.0,20.0]
stepsize = (xminmax[1] - xminmax[0])/ncount

#initial conditions
y_vals = [1]
x_vals = [0]

#the loop
n=0
while n <= ncount:
	y_n = y_vals[n]
	x_n = x_vals[n]
	y_vals.append(next_y(y_n,x_n,dy_dx,stepsize))
	x_vals.append(x_n+stepsize)
	n+=1


plt.plot(x_vals,y_vals,'r.')
plt.show()

