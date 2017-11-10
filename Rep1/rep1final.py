from scipy import misc
import matplotlib.pyplot as plt
from scipy.fftpack import fft ,ifft
import numpy as np

#filename
fn = "desync1.pgm"
#Reading file and making it a numpy array
im = misc.imread(fn)
im_org = misc.imread(fn)



#function to shift a numpy array l by an amount i
#e.g. shifter(l,2) will make l = [1,2,3,4] become l = [0,0,1,2]
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
cl=[]
ar_iftl = []

#pr_ft = previous row FT
#cr_ft = current row FT

for c,row in enumerate(im):
	#if c> 10:
	#	break
		
	if c == 0:
		prev_ft = fft(row)
		pmaxift = 0
		maxift = 0
		wentleft = True
		
	else:
		#get fourier transform, and conjugate of current row
		if wentleft:
			curr_ft = fft(row[:(len(row)-pmaxift)])
			
		else:
			curr_ft = fft(row[len(row)-pmaxift:])
			pmaxift = 0
		curr_con = np.conjugate(curr_ft)
		
		#multiply previous row FT and current row FT conjugate
		prevcurrc_mult = prev_ft*curr_con
		
		#get inferse FT
		prevcurrc_mult_ift = ifft(prevcurrc_mult)
		
		#get peak of ift, peak is shift value
		maxift = np.argmax(prevcurrc_mult_ift)
		print maxift
		if maxift > len(curr_ft)/2:
			im[c] = shifter(row,len(row)- maxift)
			wentleft = False
		else:
			im[c] = shifter(row,-1*(pmaxift+maxift))
			wentleft = True
			
		if wentleft:
			prev_ft = fft(im[c][:(len(row)-maxift-pmaxift)])
			pmaxift += maxift
		else:
			prev_ft = fft(im[c][len(row)-maxift:])
			pmaxift = maxift
		#print maxift
		cl.append(c)
		ar_iftl.append(maxift)



plt.figure()
plt.imshow(im,cmap=plt.cm.gray)		
plt.figure("org")
plt.imshow(im_org,cmap=plt.cm.gray)
plt.show(block=False)
input()
