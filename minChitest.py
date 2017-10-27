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
#returns minimum value of function and parameter list where func is minimum 
def minimise(func, params, vary , lim=0.001, jumpL=0.3, maxsteps = 100):
	params_up = list(params)
	params_down = list(params)
	step = 0	
	while jumpL > lim and step <= maxsteps:
		if len(vary) == 1:
			##setting up function parameters above and below the current position
			#parameters for having the variable increased/decreased by jumpL
			params_up[vary[0]] = params[vary[0]] + jumpL
			params_down[vary[0]] = params[vary[0]] - jumpL
		
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
				params[vary[0]] += jumpL
				print "going right"
			elif f_down < f_val:
				params[vary[0]] -= jumpL
				print "going left"
				
				
		if len(vary) >1:
			f_val = func(*params)
			paramsup = params[vary[0]] + jumpL
			paramsdown = params[vary[0]] - jumpL
			newvary = list(vary)
			newvary.pop(0)
			fup,mparams_up = minimise(func,params_up,newvary,lim,jumpL,maxsteps)
			fdown,mparams_down = minimise(func,params_down,newvary,lim,jumpL,maxsteps)
			if fup < f_val and fdown < f_val:
				print "nope, bail, at a maximum"
			elif fup > f_val and fdown > f_val:
				jumpL /= 2.
				print "shrinking"
			elif fup < f_val:
				params = list(mparams_up)
				print "going right"
			elif fdown < f_val:
				params = list(mparams_down)
				print "going left"
		step += 1

	return func(*params),params
thing ,thing2= minimise(polyLine,[0.91,3,-8,12],[0],maxsteps=1000)
print thing
print thing2
