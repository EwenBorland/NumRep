import numpy as np
import matplotlib.pyplot as plt
import inspect

#function for a polynomial line y = ax^0 + bx^1 + cx^2 ... 
#where args = [a,b,c,...]
def polyLine(x,*args):
	value = 0.0
	for n, arg in enumerate(args):
		value += arg*(x**n)
	return value

#test function
def f(x):
	return 3 - 8*x + 12*(x**2)


# function to return d^2, chi squared value for a single data point
def d2(true,obs,err):
	return ((obs-true)/err)**2 


# function to return chi^2 for a dataset
# true, obs and err are lists 
def chi2(true, obs, err):
	c2 = []
	for n,t in enumerate(true):
		c2.append(d2(t,obs[n],err[n]))
	return sum(c2)

#######thing to return the arguments a function accepts
#Nargs = inspect.getargspec(chi2)
#print Nargs
#print len(Nargs.args)

#minimiser, takes a function, initial parameters, a value to vary( eg. vary=2 for params[2])
def minimise(func, params, vary , lim=0.001, jumpL=0.3, maxsteps = 100):
	step = 0
	params_up = list(params)
	params_down = list(params)
	while jumpL > lim and step <= maxsteps:
		step += 1
		##setting up function parameters above and below the current position
		#parameters for having the variable increased/decreased by jumpL
		params_up[vary] = params[vary] + jumpL
		params_down[vary] = params[vary] - jumpL
	
		#getting values for the function above and below the current position
		f_val = func(*params)
		f_up = func(*params_up)
		f_down = func(*params_down)
		print 'n: {n}, jumpLength: {JL}, f_val: {fv}, f_down: {fd}, f_up: {fu}'.format(n=step,JL = jumpL,fv=f_val,fd=f_down,fu=f_up)
		
		if f_up < f_val and f_down < f_val:
			print "nope, bail, at a maximum"
			break
		elif f_up > f_val and f_down > f_val:
			jumpL /= 2.
			print "shrinking"
		elif f_up < f_val:
			params[vary] += jumpL
			print "going right"
		elif f_down < f_val:
			params[vary] -= jumpL
			print "going left"
			
	print "done"
	return params[vary]
	
thing = minimise(polyLine,[0.91,3,-8,12],0)
print thing

data = open("testData.txt",'r')

x = []
y = []
ye = []


for line in data.readlines():
	spl = line.split()
	x.append(spl[0])
	y.append(spl[1])
	ye.append(spl[2])
	
data.close()


#loop over c
#	loop minimise chi2 for m in each c 

#for c in np.arange(-10,10,0.01):
#	m = minimise(chi2)







