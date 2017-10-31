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

low_chi = 1000
#print "start loop"
##Need a method to estimate good initial parameters(i.e. grid search)
for c in np.arange(-5,5,0.1):
	for m in np.arange(-5,10,0.1):
		chi = chiSq(x,y,ye,polyLine,c,m)
		if chi < low_chi:
			#print "lower"
			cstart = c
			mstart = m
#mstart = 0.01
#cstart = 0.95

print "Starting parameters: m = {0} , c = {1}".format(mstart,cstart)
print "~~~~~Own ChiSq Method~~~~~"


minchi, minchiparams = minimise(chiSq,(x,y,ye,polyLine,cstart,mstart),[4,5],maxsteps=100000000,jumpL=0.0001,lim = 0.000001)
print "Minimum Chi Squared = {0}".format(minchi)
#print minchiparams
print "Found at c = {0} and m = {1}\n\n".format(minchiparams[4],minchiparams[5])

bestc = minchiparams[4]
bestm = minchiparams[5]
print "~~~~~Scipy ChiSq Method~~~~~"

#scipy stuff
def sci_chiSq((c,m)):
	true = []
	c2=[]
	for i in x:
		true.append(polyLine(i,c,m))
	for n,i in enumerate(y):
		c2.append(((true[n]-i)/ye[n])**2)
	return sum(c2)

x0 = np.array([cstart,mstart]) 
scipyres = opt.minimize(sci_chiSq,(cstart,mstart))

#print scipyres.x
print "Minimum Chi Squared = {0}".format(scipyres.fun)
#print minchiparams
print "Found at c = {0} and m = {1}\n\n".format(scipyres.x[0],scipyres.x[1])


#varying around the best c and m values
clist = np.arange(bestc-0.05,bestc+0.05,0.0001)
chi_clist=[]
mlist = np.arange(bestm-0.05,bestm+0.05,0.0001)
chi_mlist=[]
for i in clist:
	chi_clist.append(chiSq(x,y,ye,polyLine,i,bestm))

for i in mlist:
	chi_mlist.append(chiSq(x,y,ye,polyLine,bestc,i))
	
c_chiplusoneindex = min(chi_clist, key=lambda x:abs(x-(minchi+1)))
m_chiplusoneindex = min(chi_mlist, key=lambda x:abs(x-(minchi+1)))
c_plusone = clist[chi_clist.index(c_chiplusoneindex)]
m_plusone = mlist[chi_mlist.index(m_chiplusoneindex)]
cerr = abs(bestc-c_plusone)
merr = abs(bestm-m_plusone)

print "~~~Results with errors~~~\n"
print "c = {0} +/- {1} , m = {2} +/- {3} \n\n\n".format(bestc,cerr,bestm,merr)






plt.figure(0)
bestx = [-1,11]
besty = [polyLine(bestx[0],bestc,bestm),polyLine(bestx[1],bestc,bestm)]
plt.errorbar(x,y,yerr=ye,fmt='.')
plt.plot(bestx,besty,'-')
plt.xlim(bestx)

plt.figure(1)
plt.plot(mlist,chi_mlist,'-')
plt.plot([bestm,bestm],[0,max(chi_mlist)],'--')
plt.xlabel("m")
plt.ylabel("Chi Squared")
plt.figure(2)
plt.plot(clist,chi_clist,'-')
plt.plot([bestc,bestc],[0,max(chi_clist)],'--')
plt.xlabel("c")
plt.ylabel("Chi Squared")

plt.show(block=False)
input()
	
	
		
