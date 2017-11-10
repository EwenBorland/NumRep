import scipy.misc
#from scipy import misc      # Import misc 
import matplotlib.pyplot as plt
from scipy.fftpack import fft ,ifft
import numpy as np

#         Get the filename as string
#fn = str(raw_input("File : "))
fn = "desync1.pgm"
#         Read file it np array
im = scipy.misc.imread(fn) 
print len(im[0])
#         Display with grayscale colour map 


#         Show the image

#b = fft(im[0])
#c = fft(im[1])
#cc = np.conjugate(c)
#print c
#f = b*cc
#iff = ifft(f)
#print iff
#print "kjhgfsfdgfcvhjb"
#print f
#print max(iff)
#
#x = range(len(im))
#plt.plot(x,b,'g')	
#plt.plot(x,c,'r')
#plt.plot(x,f)
#im2 = fft(im)
#plt.imshow(im2,cmap=plt.cm.gray)
#plt.show()
cl=[]
ar_iftl = []
def shift(xs, n):
    if n >= 0:
        return np.r_[np.full(n, 0), xs[:-n]]
    else:
        return np.r_[xs[-n:], np.full(-n, 0)]
for c,row in enumerate(im):
	if c == 0:
		pr_ft = fft(row)
	else:
		cr_ft = fft(row)
		cr_con = np.conjugate(cr_ft)
		
		ar_m = pr_ft*cr_con
		ar_m_ift = ifft(ar_m)
		cl.append(c)
		maxift = ar_m_ift.tolist().index(max(ar_m_ift))
		ar_iftl.append(maxift)
		if maxift > 0:
			im[c] = np.roll(row,maxift-512)
			#if maxift > 20:
			#	im[c] = shift(row,maxift-512)
			#else:
			#	im[c] = shift(row,maxift)
		pr_ft = fft(im[c])

plt.imshow(im,cmap=plt.cm.gray)		
#plt.plot(cl,ar_iftl,'.')
#print ar_iftl
plt.show()
