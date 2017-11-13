from scipy import misc
import matplotlib.pyplot as plt
from scipy.fftpack import fft ,ifft
import numpy as np

#filename
fn = "desync1.pgm"
#Reading file and making it a numpy array
im = misc.imread(fn)
im_org = misc.imread(fn)

def shifter(l,i):
	#print "a"
	c = 0
	if i == 0:
		#print "nope"
		return l
	elif i > 0:
		#print "right"
		while c < i:
			#print"aa"
			l = np.delete(l,len(l)-1)
			#print "ab"
			l = np.insert(l,0,255)
			#print "ac"
			c+=1
	elif i < 0:
		#print "left"	
		while c < abs(i):
			#print "ba" 
			l = np.delete(l,0)
			#print "bb"
			l = np.append(l,0)
			#print "bc"
			c+=1
	return l

transformed = []

for row in im:
	transformed.append(fft(row))

shift_vals = []

for c, row in enumerate(transformed):
	if c == 0:
		row_p = row
		shift_vals.append(0)
	else:
		con = np.conjugate(row)
		eq = con*row_p
		shift_num = np.argmax(ifft(eq))
		shift_vals.append(shift_num)

def shifter(l,i):
	#print "a"
	c = 0
	if i == 0:
		#print "nope"
		return l
	elif i > 0:
		#print "right"
		while c < i:
			#print"aa"
			l = np.delete(l,len(l)-1)
			#print "ab"
			l = np.insert(l,0,255)
			#print "ac"
			c+=1
	elif i < 0:
		#print "left"	
		while c < abs(i):
			#print "ba" 
			l = np.delete(l,0)
			#print "bb"
			l = np.append(l,255)
			#print "bc"
			c+=1
	else:
		print "bork"
	return l





#print shift_vals
rowlen = len(im[0])
i=0
for c, shft in enumerate(shift_vals):
	if shft > rowlen-(rowlen*0.2):
		i += rowlen - shft
	elif shft <= rowlen-(rowlen*0.8):
		i -= -1*shft
	else:
		i = 0
	im[c] = shifter(im[c],i)
	
















plt.imshow(im,cmap=plt.cm.gray)	
plt.show()
