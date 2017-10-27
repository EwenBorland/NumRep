import numpy as np
import matplotlib.pyplot as plt
import inspect
import time
import scipy.optimize as opt

#function for a polynomial line y = ax^0 + bx^1 + cx^2 ... 
#where args = [a,b,c,...]
def polyLine(x,*args):
	value = 0.0
	for n, arg in enumerate(args):
		value += arg*(x**n)
	return value


#Chi Squared Function
#args = (x,ob,err,func,params) for func = func(x,*params), eg, chiSq(x,obs,err,polyLine,a,b,c,d)
#or args = (true, obs, err)	
def chiSq(*args):
	c2 = []
	if len(args) >= 4:
		if callable(args[3]):
			true = []
			for i in args[0]:
				true.append(args[3](i,*args[4:]))	
			for n,t in enumerate(true):
				d2 = (((args[1])[n] - t)/(args[2])[n])**2
				c2.append(d2)
		else: print "{f} is not callable".format(f=args[4])
	elif len(args) == 3:
		for n,t in enumerate(args[0]):
			d2 = (((args[1])[n] - t)/(args[2])[n])**2
			c2.append(d2)
	
	return sum(c2)


#minimiser
def minimise(func, params, vary , lim=0.001, jumpL=0.3, maxsteps = 100):
	step = 0
	while jumpL > lim and step <= maxsteps:

		if len(vary) == 1:
			##setting up function parameters where the variable is increased/decreased by jumpL
			params_up = list(params)
			params_down = list(params)
			params_up[vary[0]] = params[vary[0]] + jumpL
			params_down[vary[0]] = params[vary[0]] - jumpL

			#getting values for the function with new parameters
			f_val = func(*params)

			f_up = func(*params_up)
			f_down = func(*params_down)
			
			#print 'n: {n}, jumpLength: {JL}, f_val: {fv}, f_down: {fd}, f_up: {fu}'.format(n=step,JL = jumpL,fv=f_val,fd=f_down,fu=f_up)
			
			#if both values are higher than f_val then decrease jump length
			if f_up > f_val and f_down > f_val:
				jumpL /= 2.
				#print "shrinking"
			#if f_up is less than f_val then new parameters are set to f_up parameters
			elif f_up < f_val:
				params = list(params_up)
				#print "going right"
			#if f_down ... 
			elif f_down < f_val:
				params = list(params_down)
				#print "going left"
			#increase step and loop	
				
		if len(vary) >1:
			#print "heyo"
			f_val = func(*params)
			#getting new parameter lists where the first variable has been increased/decreased
			paramsup = list(params)
			paramsdown = list(params)
			paramsup[vary[0]] = params[vary[0]] + jumpL
			paramsdown[vary[0]] = params[vary[0]] - jumpL
			
			#getting a new variable list where the first variable has been removed
			newvary = list(vary)
			newvary.pop(0)
			#minimising the function with the first variable fixed and varying the remaining variables in the vary list
			fup, mparams_up = minimise(func,paramsup,newvary,lim,jumpL,maxsteps)
			fdown, mparams_down = minimise(func,paramsdown,newvary,lim,jumpL,maxsteps)
			#if statements
			if fup > f_val and fdown > f_val:
				jumpL /= 2.
				#print "shrinking"
			elif fup < f_val:
				params = list(mparams_up)
				#print "going right"
			elif fdown < f_val:
				params = list(mparams_down)
				#print "going left"
		
		step += 1
		#time.sleep(1)
	#returning the minimum value of the function and the parameters at this location
	return func(*params),params







	
#Getting the data set	
data = open("testData.txt",'r')
x = []
y = []
ye = []
for line in data.readlines():
	spl = line.split()
	x.append(float(spl[0]))
	y.append(float(spl[1]))
	ye.append(float(spl[2]))
data.close()	
	
mstart = 0.01
cstart = 0.95


minchi, minchiparams = minimise(chiSq,(x,y,ye,polyLine,cstart,mstart),[4,5],maxsteps=100000000,jumpL=0.0001,lim = 0.000001)
print minchi
print minchiparams




#scipy stuff
def sci_chiSq((c,m)):
	true = []
	c2=[]
	for i in x:
		true.append(polyLine(i,c,m))
	for n,i in enumerate(y):
		c2.append(((true[n]-i)/ye[n])**2)
	return sum(c2)

x0 = np.array([0.95,0.0]) 
scipyres = opt.minimize(sci_chiSq,(0.95,0.0))

print scipyres


#test = chiSq(x,y,ye,polyLine,0.95,0.01)	
#print test

#testx = [0,10]
#testy = [polyLine(testx[0],0.95,0.01),polyLine(testx[1],0.95,0.01)]

#plt.errorbar(x,y,yerr=ye,fmt='.')
#plt.plot(testx,testy,'-')
#plt.show()
	
	
		
