import numpy as np
import matplotlib.pyplot as plt
from time import sleep
import ChargeDistribution as ChDist


#setup charge distribution
rho = ChDist.ChargeDistribution()
xvalues, yvalues = rho._get()

#plt.figure(0)
#rho.show(title='title',disp=False)
#plt.plot()

#define ODE
def dE(x):
	return rho.evaluate(x)
	

#Euler method
def step_Euler(x0, y0, func, stepsize):
	return (y0 + stepsize*(func(x0)))

#4th Order Runge-Kutta
def step_RK4(x0,y0,func,stepsize):
	k1 = func(x0)
	k2 = func(x0 + stepsize/2)
	k3 = func(x0 + stepsize/2)
	k4 = func(x0 + stepsize)
	y1 = y0 + stepsize*(k1/6 + k2/3 + k3/3 + k4/6)
	return y1

#number of E Field values to calculate
ncount = 100
#range to determine the E Field in
xminmax= [-2.0,2.0]
stepsize = (xminmax[1] - xminmax[0])/ncount
#E initial values
init = [-2.0,0.0]

#x values
r = np.linspace(xminmax[0],xminmax[1],ncount)

### Main Loop for Electric Field

#setting up the arrays with the initial conditions
x_Euler = [init[0]]
y_Euler = [init[1]]
x_RK4 = [init[0]]
y_RK4 = [init[1]]

#Loop to integrate using the Euler method
for n in range(len(r)-1):
	y_n = y_Euler[n]
	x_n = r[n]
	y_Euler.append(step_Euler(x_n,y_n,dE,stepsize))
	#x_Euler.append(x_n + stepsize)

#Loop to integrate using the 4th Order Runge Kutta method
for n in range(len(r)-1):
	y_n = y_RK4[n]
	x_n = r[n]
	y_RK4.append(step_RK4(x_n,y_n,dE,stepsize))
	#x_RK4.append(x_n + stepsize)


### Main Loop for Voltage

#list for the Voltage ODE, dv/dx = -E
dVy_list = [i*-1 for i in y_RK4]
def dV(x):
	return dVy_list[x]

#Euler method again
#rewritten to accept the list of E values and use a stepsize twice the size used to make the E values
def step_Euler_V(x0, y0, func,stepsize):
	return (y0 + stepsize*2*(func(x0)))

#RK4 method again
#rewritten to use a list of values instead of a function
def step_RK4_V(x0,y0,func,stepsize):
	k1 = func(x0)
	k2 = func(x0 + 1)
	k3 = func(x0 + 1)
	k4 = func(x0 + 2)
	y1 = y0 + (stepsize*2)*(k1/6 + k2/3 + k3/3 + k4/6)
	return y1

#initial lists
#x value list takes every second value of the E field x list
Vx_vals = r[::2]
Vy_vals_RK4 = [0]
Vy_vals_Euler = [0]

#Euler method
for n in range(len(Vx_vals)-1):
	y_n = Vy_vals_Euler[n]
	Vy_vals_Euler.append(step_Euler_V(n*2,y_n,dV,stepsize))


#RK4 method
for n in range(len(Vx_vals)-1):
	y_n = Vy_vals_RK4[n]
	Vy_vals_RK4.append(step_RK4_V(n*2,y_n,dV,stepsize))


# loops to get the diference between Euler and RK4 at each x value
diffyE = []
diffyV = []
for i in range(len(r)):
	diffyE.append(abs(y_RK4[i]-y_Euler[i]))
for i in range(len(Vx_vals)):
	diffyV.append(abs(Vy_vals_RK4[i] - Vy_vals_Euler[i]))


#plotting

#data sets (x,y)
#for E ,(r,y_RK4),(r,y_Euler), 
#for V ,(Vx_vals,Vy_vals_RK4),(Vx_vals,Vy_vals_Euler)
#(r, diffyE) , (r,diffyV)
plt.figure(1)
#rho.show(disp=False)
plt.plot( xvalues, yvalues , 'm-',label="Charge Distribution")

plt.plot(r,y_RK4,'b-',label='Electric Field(RK4)')
#plt.plot(r,y_Euler,'r-',label='Electric Field(Euler))

plt.plot(Vx_vals,Vy_vals_RK4,'g-',label='Voltage (RK4)')
#plt.plot(Vx_vals,Vy_vals_Euler,'r-',label='Voltage(Euler)')

plt.plot([0,0],[-1.0,1.0],'k--')
plt.plot([-2,2],[0,0],'k--')
plt.legend(loc=3,fontsize=12)

plt.figure(2)
plt.plot(r,y_RK4,'g-',label='Electric Field(RK4)')
plt.plot(r,y_Euler,'r-',label='Electric Field(Euler)')
plt.plot([0,0],[-1.0,1.0],'k--')
plt.legend(loc=3,fontsize=12)

plt.figure(3)
plt.plot(Vx_vals,Vy_vals_RK4,'g-',label='Voltage (RK4)')
plt.plot(Vx_vals,Vy_vals_Euler,'r-',label='Voltage(Euler)')
plt.legend(loc=3,fontsize=12)

plt.figure(4)
plt.plot(r,diffyE,'c-',label='|E(RK4) - E(Euler)|')
plt.plot(r,y_RK4,'g-',label='Electric Field(RK4)')
plt.plot(r,y_Euler,'r-',label='Electric Field(Euler)')
plt.plot([0,0],[-1.0,1.0],'k--')
plt.legend(loc=3,fontsize=12)

plt.figure(5)
plt.plot(Vx_vals,diffyV,'c-',label='|V(RK4) - V(Euler)|')
plt.plot(Vx_vals,Vy_vals_RK4,'g-',label='Voltage (RK4)')
plt.plot(Vx_vals,Vy_vals_Euler,'r-',label='Voltage(Euler)')
plt.legend(loc=3,fontsize=12)

plt.show(block=False)
raw_input("...")
