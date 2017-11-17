from scipy import misc
import matplotlib.pyplot as plt
from scipy.fftpack import fft ,ifft
import numpy as np
import sys
#filename
fn = sys.argv[1]
testfilestr = fn[:-4] + "_test.txt"
outimage = fn[:-4] + "_result.pgm"
#Reading file and making it a numpy array
im = misc.imread(fn)
im_org = misc.imread(fn)
testfile = open(testfilestr,'w')

#function that takes a list/array and moves the values i places left/right
#by deleting values at the end and inserting 0 values at the start of the list
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

def shiftlength(i,relshift,rowlen):
	if relshift > rowlen/2:
		l = i +(rowlen - relshift)
	elif relshift <= rowlen/2:
		l = i +(-1*relshift)
	return l
	

for c,shiftnum in enumerate(relative_shifts):
	#getting the amount of pixels a row needs to be shifted
	new_i = shiftlength(i,shiftnum,rowlen)
	shift0 = shiftlength(0,shiftnum,rowlen)
	cutoffperc = 0.05
	#condition for when the relative shift is consider large
	if shiftnum in range(int(rowlen*cutoffperc),int(rowlen*(1-cutoffperc)),1) and c <= (len(relative_shifts) - 3):
		#checking the next 3 rows
		#if a row will be shifted > 5 pixels from the current row and also in the opposite direction then a check is True, else False
		check1 = (shiftlength(0,relative_shifts[c+1],rowlen) > 5) and (shiftlength(0,relative_shifts[c+1],rowlen)*new_i) < 0
		check2 = (shiftlength(0,relative_shifts[c+2],rowlen) > 5) and (shiftlength(0,relative_shifts[c+2],rowlen)*new_i) < 0
		check3 = (shiftlength(0,relative_shifts[c+3],rowlen) > 5) and (shiftlength(0,relative_shifts[c+3],rowlen)*new_i) < 0
		#if no rows shift back then the current row is not shifted
		if not (check1 or check2 or check3):
			new_i = i
	
	#condition for when there is a diagonal feature in the image
	'''
	if c>0:
		prevshift = shiftlength(0,relative_shifts[c-1],rowlen)
		currshift = shiftlength(0,shiftnum,rowlen)
		if c < (len(relative_shifts)-1):
			nextshift = shiftlength(0,relative_shifts[c+1],rowlen)
		else: 
			nextshift = currshift
		
		if prevshift == currshift and currshift == nextshift:
			new_i = i
	'''
	#checking and correcting for diagonal shifts
	if c < (len(relative_shifts) - 4) and abs(shift0) > 0:
		#getting the shift of the next 4 lines 
		shift1 = shiftlength(0,relative_shifts[c+1],rowlen)
		shift2 = shiftlength(0,relative_shifts[c+2],rowlen)
		shift3 = shiftlength(0,relative_shifts[c+3],rowlen)
		shift4 = shiftlength(0,relative_shifts[c+4],rowlen)
		if not(shift1 == shift0 or shift2 == shift0 or shift3 == shift0 or shift4 == shift0) and not(shift1==0 or shift2==0 or shift3==0 or shift4==0):
			grad1 = 1.0/abs(shift0-shift1)
			grad2 = 2.0/abs(shift0-shift2)
			grad3 = 3.0/abs(shift0-shift3)
			grad4 = 4.0/abs(shift0-shift4)
			if 1/grad1 < 5 and 1/grad2 < 5 and 1/grad3 < 5 and 1/grad4 < 5:
				print "row: {0} , shifts: {1} {2} {3} {4} {5}".format(c,shift0,shift1,shift2,shift3,shift4)
				new_i -= shift0
				relative_shifts[c+1] -= shift1
				relative_shifts[c+2] -= shift2
				relative_shifts[c+3] -= shift3
				relative_shifts[c+4] -= shift4
	


	total_shifts.append(new_i)
	i = new_i
		
	testfile.write("row:{0} \t relative_shift:{1} \t\t total_shift:{2}\n".format(c,shiftnum,i))

testfile.close()

#Going through the list of shifts and shifting each row
for c, i in enumerate(total_shifts):
	im[c] = shifter(im[c],i)

lost_pixels = float(sum(total_shifts))
total_pixels = len(im_org)*len(im_org[0])

lost_perc = 100*(lost_pixels/total_pixels)

print "Total Number of Pixels: {2} , Number of pixels lost: {0} , Percentage of pixels lost: {1}".format(lost_pixels, lost_perc, total_pixels)
#Plotting
#plt.imshow(im,cmap=plt.cm.gray)
misc.imsave(outimage,im)
#plt.figure()
#plt.imshow(im_org,cmap=plt.cm.gray)
#plt.show(block=False)
#input()
