import numpy as np


def f(x):
	return 10.2 - 7.4*x - 2.1*(x**2) + x**3
def g(x):
	return np.exp(x) -2
def h(x):
	return np.cos(x)*np.sin(3*x)

def posneg(x):
	if x > 0.0: return 1
	elif x <0.0: return -1
	elif x == 0.0: return 0


#bisection method
def bisect(func, x1, x2, res):
	if abs(x2-x1) > res:
		sfx1=posneg(func(x1))
		sfx2=posneg(func(x2))
		xc = ((x2+x1)/2.0)
		fxc = func((x2+x1)/2.0)
		sxc = posneg(xc)
		
		if sfx1 != sxc:
			print "x1 to " + str(xc)
			return bisect(func,xc,x2,res)
		elif sfx2 != sxc:
			print "x2 to " + str(xc)
			return bisect(func,x1,xc,res)
	
	else: 

		return "Root at x = "+ str((x1 + x2)/2.0)
	 

print bisect(h, 6.0, 7.0, 0.001)	
