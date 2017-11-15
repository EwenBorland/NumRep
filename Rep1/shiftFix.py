from scipy import misc
import matplotlib.pyplot as plt
from scipy.fftpack import fft ,ifft
import numpy as np

#filename
fn = "desync3.pgm"
#Reading file and making it a numpy array
im = misc.imread(fn)
im_org = misc.imread(fn)
testfile = open("rep1testout3.txt",'w')

#function that takes a list/array and moves the values i places left/right by deleting values at the end and inserting 0 values at the start of the list
# example = [1,2,3,4,5]
# shifter(example,2) returns [0,0,1,2,3]
def shifter(l,i):
	counter = 0
	if i == 0:
		return l
	elif i > 0:
		#if list is shifting right, insert i number of 0's at start and delete i number of values from the end
		while counter <= i:
			l = np.delete(l,len(l)-1)
			l = np.insert(l,0,0)
			counter+=1
	elif i < 0:
		#if list is shifting left, insert 0's at the end and delete values from the start	
		while counter <= abs(i): 
			l = np.delete(l,0)
			l = np.append(l,0)
			counter+=1
	return l



relative_shifts = []
total_shifts = []
i=0
rowlen = len(im[0])
for rownum in range(len(im)):
	#Calculating the relative shift between the current row and the previous row
	if rownum == 0:
		#0th row is not shifted
		shift_num = 0
	else:
		#fourier transform both rows, conjugate one, multiply together and inverse FT the result.
		#The location of the peak of the result is the amount current row is shifted relative to previous row
		shift_num = np.argmax(ifft((np.conjugate(fft(im[rownum-1])))*fft(im[rownum])))
	
	relative_shifts.append(shift_num)
	
	#Calculating amount the current row needs to be shifted
	if shift_num > rowlen/2:
		i += (rowlen - shift_num)
	elif shift_num <= rowlen/2:
		i += (-1*shift_num)

	total_shifts.append(i)
		
	testfile.write("row:{0} \t relative_shift:{1} \t\t total_shift:{2}\n".format((rownum+1),shift_num,i))

filey.close()

#Going through the list of shifts and shifting each row
for c, i in enumerate(total_shifts):
	im[c] = shifter(im[c],i)

#Plotting
plt.imshow(im,cmap=plt.cm.gray)
plt.figure()
plt.imshow(im_org,cmap=plt.cm.gray)
plt.show(block=False)
input()
