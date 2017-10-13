import numpy as np

funcdict = {}
for i in np.linspace(-2.0,2.0,4001):
		funcdict[i] = 1/3



#given an x value, returns (x,y) of function elist
def retXY(elist,x):
	return elist[x]



print retXY(funcdict, 0.5)
print retXY(funcdict, -0.03)

'''
init = [1.0,1.0]


ncount = 101
xminmax= [-2.0,2.0]
stepsize = (xminmax[1] - xminmax[0])/ncount
r = np.linspace(min(xminmax),max(xminmax),ncount)
print len(r)
#print r[0:7]
for i in range(len(r)):
	if r[i] >= init[0]:
		print i
		leftlist = r[0:i]
		rightlist = r[i:]
		break

print leftlist
print rightlist

##runge kutte shenanigans


def step_RK4(func,x0,y0,stepsize):
	k1 = func(x0)
	k2 = func(x0 + stepsize/2)
	k3 = func(x0 + stepsize/2)
	k4 = func(x0 + stepsize)
	y1 = y0 + stepsize*(k1/6 + k2/3 + k3/3 + k4/6)
	return y1
	
	
'''
