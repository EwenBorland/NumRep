import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

#defining functions to be used
tau = 2.2
#exponential function
def p(x):
	return (1/tau)*np.exp(-1*x/tau)
#cumulative function of p(x)
def g(t):
	return (1-np.exp(-t/tau))
#inverse of the cumulative function
def g_i(y):
	return (-tau*np.log(1-y))
	
#number of data sets
datasets = 2500

#number of measurements in each data set
datalength = 1000

#array to hold the mean decay time of each data set
times = []

#counter for while loops
j = 0

### Loops for generating the random numbers
# 3 are written out, if statements determine which method will be used   


# using the inverse cumulative method
if True:
	#loop to generate data sets
	while j <= datasets:
		print j
		#creating an empty list to hold the numbers generated for each data set
		randomlist = []
		i=0
		#loop to generate random numbers
		while i <= datalength:
			#generating a random number between 0 and 1
			y = np.random.uniform()
			#scaling it to the range of the function
			y = y*1 # would be y*g(b) but p(x) is normalised to 1 so g(b) = 1
			#getting the inverse 
			y_i = g_i(y)
			#adding the value to the list for this data set
			randomlist.append(y_i)
			i+=1
		#adding the mean of the generated values to the list of results
		times.append(np.mean(randomlist))
		j +=1	

# using the box method
if False:
	#min and max x values of the box
	a = 0.0
	b = 15
	#box max height
	fmax = 1
	while j <= datasets:
		print j
		randomlist = []
		i=0
		while i < datalength:
			#generating a random number in the range a,b
			x1 = np.random.uniform()
			x1 = a + (b-a)*x1
			#getting the function height at this location
			y1 = p(x1)
			#generating a random number in the range 0, fmax
			y2 = np.random.uniform()
			y2 = fmax*y2
			#adding the x value to the list of numbers for this data set if y2<y1, else repeat for a new number
			if y2<y1 :
				randomlist.append(x1)
				i += 1
		times.append(np.mean(randomlist))
		j += 1

# using a numpy method to generate numbers
if False:
	while j <= datasets:
		print j
		listthing = []
		i=0
		while i < datalength:	
			randomlist.append(np.random.exponential(scale=tau))
			i += 1
		times.append(np.mean(randomlist))
		j += 1					

# getting the mean time and printing it to the terminal
result_mean=np.mean(times)
print("Mean of the Simulated Times : %.3f microseconds" % result_mean)
print("Standard Deviation of the Simulated times: %.3f microseconds"% np.std(times))
print("True Decay Time : %.3f microseconds" % tau)

#writing the final data set to a file
file1 = open("muonfile.txt",'w')
for item in randomlist:
	file1.write(str(item) + ", ")
file1.close()


#plotting the histogram of the final data set
y,x,_ = plt.hist(randomlist,50)
plt.plot([tau,tau],[0,y.max()],'r--',label="true decay time")
plt.plot([np.mean(randomlist),np.mean(randomlist)],[0,y.max()],'g--',label="mean simulated decay time")
#plotting an example exponential function
x=np.arange(0,16,0.01)
exparr = y.max()*np.exp(-x/tau)
plt.plot(x,exparr,'r-',linewidth=2,label="Example Exponential")

plt.title("Simulated Decay Times Histogram")
plt.xlabel("Decay Time(microseconds)")
plt.ylabel("Frequency")
plt.legend(fontsize=12)
plt.show()



#plotting the histogram
#number of bins
nbins = 50
#making and plotting the histogram, returns an array of the bin sizes (y) and other stuff
y,x, _ = plt.hist(times,nbins)

#plotting a line to represent the mean value of the results
plt.plot([result_mean,result_mean],[0,y.max()],'g--',linewidth=2,label="Mean Decay Time")
plt.plot([tau,tau],[0,y.max()],'r--',linewidth=1,label="True Decay Time")
#plotting a gaussian function roughly the size of the histogram
#sigma of the gaussian = sqrt of the variance of the results
sigma = np.sqrt(np.var(times))
x = np.arange(0,5,0.01)
plt.plot(x, y.max()/5*mlab.normpdf(x, tau,sigma), label = 'Example Gaussian')


plt.xlabel("Muon Lifetime (microseconds)")
plt.ylabel("Frequency")
plt.title("{}{}{}{}{}".format("Muon Lifetime Histogram (bins: ",nbins," , Data Sets: ",datasets,")"))
plt.xlim(1.8,2.6)
plt.legend(fontsize=12)
plt.show()
