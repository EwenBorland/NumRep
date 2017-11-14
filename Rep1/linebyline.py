from scipy import misc
import matplotlib.pyplot as plt
from scipy.fftpack import fft ,ifft
import numpy as np
# 184,216
#filename
fn = "desync3.pgm"
#Reading file and making it a numpy array
im = misc.imread(fn)
im_org = misc.imread(fn)
filey = open("rep1testout.txt",'w')
def shifter(l,i):
	#print "a"
	p = 0
	if i == 0:
		#print "nope"
		return l
	elif i > 0:
		#print "right"
		while p <= i:
			#print"aa"
			l = np.insert(l,0,l[len(l)-1])
			l = np.delete(l,len(l)-1)
			#print "ab"
			
			#print "ac"
			p+=1
	elif i < 0:
		#print "left"	
		while p <= abs(i):
			#print "ba" 
			l = np.append(l,l[0])
			l = np.delete(l,0)
			#print "bb"
			
			#print "bc"
			p+=1
	return l
	
transformed = []

for row in im:
	transformed.append(fft(np.copy(row)))
	
shift_vals = []
i_ = []
i=0
rowlen = len(im[0])
for c, row in enumerate(im):
	if c == 0:
		row_p = fft(row)
		shift_num = 0
		
	else:
		r = fft(row)
		con = np.conjugate(r)
		eq = row_p*con
		shift_num = np.argmax(ifft(eq))
	
	shift_vals.append(shift_num)
	
	if shift_num > 0:
		#if shift_num > 482:
		#	im[c] = shifter(row,512-shift_num)
		#elif shift_num < 30:
		#	im[c] = shifter(row,-shift_num)
		im[c] = shifter(row,shift_num-len(row))
	row_p = fft(im[c])
	
plt.imshow(im,cmap=plt.cm.gray)
plt.figure()
plt.imshow(im_org,cmap=plt.cm.gray)
plt.show(block=False)
input()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
