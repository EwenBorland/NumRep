from scipy import misc
import matplotlib.pyplot as plt
from scipy.fftpack import fft ,ifft
import numpy as np
# 184,216
#filename
fn = "desync1.pgm"
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
			l = np.delete(l,len(l)-1)
			#print "ab"
			l = np.insert(l,0,100)
			#print "ac"
			p+=1
	elif i < 0:
		#print "left"	
		while p <= abs(i):
			#print "ba" 
			l = np.delete(l,0)
			#print "bb"
			l = np.append(l,100)
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
for c, row in enumerate(transformed):
	if c == 0:
		row_p = np.copy(row)
		shift_num = 0
		
	else:
		con = np.conjugate(np.copy(row_p))
		eq = con*row
		shift_num = np.argmax(ifft(eq))
	shift_vals.append(shift_num)
	
	if shift_num > rowlen-(rowlen*0.1):
		i += (rowlen - shift_num)
		#i += (-1*shift_num)
		#i += shift_num - rowlen
	elif shift_num <= rowlen-(rowlen*0.9):
		i += (-1*shift_num)
		#i += (rowlen - shift_num)
		#i += shift_num
	else:
		i += 0
	i_.append(i)
		
	filey.write("row:{0} \t maxarg:{1} \t i:{2}\n".format((c+1),shift_num,i))
#print shift_vals
filey.close()
print len(i_)
for c, i in enumerate(shift_vals):
	im[c] = np.copy(shifter(im[c],i))



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
