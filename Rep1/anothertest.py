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
filey = open("rep1testout3.txt",'w')
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
			l = np.delete(l,len(l)-1)
			#print "ab"
			l = np.insert(l,0,0)
			#print "ac"
			p+=1
	elif i < 0:
		#print "left"	
		while p <= abs(i):
			#print "ba" 
			l = np.delete(l,0)
			#print "bb"
			l = np.append(l,0)
			#print "bc"
			p+=1
	return l



shift_vals = []
i_ = []
i=0
rowlen = len(im[0])
for c in range(len(im)):
	if c == 0:
		shift_num = 0
		
	else:
		shift_num = np.argmax(ifft((np.conjugate(fft(im[c-1])))*fft(im[c])))
	shift_vals.append(shift_num)
	
	if shift_num > rowlen/2:
		i += (rowlen - shift_num)
		#i += (-1*shift_num)
		#i += shift_num - rowlen
	elif shift_num <= rowlen/2:
		i += (-1*shift_num)
		#i += (rowlen - shift_num)
		#i += shift_num

	i_.append(i)
		
	filey.write("row:{0} \t relative_shift:{1} \t\t total_shift:{2}\n".format((c+1),shift_num,i))
#print shift_vals
filey.close()
print len(i_)

print i_
for c, i in enumerate(i_):
	im[c] = shifter(im[c],i)



'''
la = []
i==0
while i <100:
	la.append(im_org[i])
	i+=1




x = range(len(im_org))
#plt.plot(x,im_org[0],'g-')
#plt.plot(x,fft(im_org[8]),'b-')
#plt.plot(x,np.conjugate(fft(im_org[9])),'r-')
l = ifft(fft(im_org[4])*np.conjugate(fft(im_org[5])))
l2 = ifft(np.conjugate(fft(im_org[4]))*fft(im_org[5]))
print np.argmax(l)
print np.argmax(l2)
plt.plot(x,l2,'r-')
plt.plot(x,l,'c--')
#plt.ylim(-5000,5000)
#plt.ylim(-255,255)


plt.figure()
plt.imshow(im_org,cmap=plt.cm.gray)	
plt.figure()
plt.imshow(la,cmap=plt.cm.gray)
'''

plt.imshow(im,cmap=plt.cm.gray)
plt.figure()
plt.imshow(im_org,cmap=plt.cm.gray)
plt.show(block=False)
input()
