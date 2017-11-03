from ChargeDistribution import ChargeDistribution
import numpy as np

#-------------
# Helpers

#Printing
def printArray( a ):
    print("\n")
    for i in range(len(a)):
        print "%0.2f" %a[i].real, "  +  "+ "%0.2f" %a[i].imag + " j"

# The horrible divide by Kn thing
def divideKn( input ):
    pi = math.pi
    L = len(input)
    output = []
    #Set element 0 to zero as we cant fivide by zero -  this is taken care of by boundary conditions.
    output.append(0)
    #Now fill rest of array
    for n in range(1,L):
        if( n <= samples/2 ):
            kn = float(n) * pi / ((xhi-xlo)/2.)
        else:
            kn = - float(samples-n) * pi / ((xhi-xlo)/2.)
        output.append( input[n] / np.complex(0.,kn ) )
    return np.array(output)

#------------------
# Discrete fourier transform using numpy.fft
#

import math
import numpy as np
from numpy import fft
import matplotlib.pyplot as plt

fig = plt.figure()

#-----------------
# Create the input waveform in the time domain

samples = 100
increments = np.arange(samples)

#Make up a list of distances and charge values for x axis going from -2 to 2
xlo = -2.
xhi = 2.
distances = ((xhi-xlo)/samples)*(increments - samples/2.)

chargeFunction = ChargeDistribution()
chargeDensity= []
for i in range(samples):
    chargeDensity.append( chargeFunction.evaluate(distances[i]) )

fig.add_subplot(511)
plt.plot( distances, chargeDensity )
plt.title('Charge Density')


#-----------------
# Create the transform

chargeTilde = fft.fft(chargeDensity)

#printArray(chargeTilde)

#-------------------
#Create field transform

pi = math.pi

fieldTilde = divideKn( chargeTilde )

#-------------------
#Do inverse transform to get field

#printArray( fieldTilde )

field = fft.ifft(fieldTilde)

#Put in boundary condition that field=0 at x-0
field = field - field[0]

fig.add_subplot(513)
plt.plot( distances, field.real, distances, field.imag )
plt.title('Electric Field')


#-------------------
#Do fft again of field to get voltage transform
# We divide by ik_n which is pi*n/L  = pi*n/twoL/2

fieldTilde = fft.fft(-field)

voltageTilde = divideKn( fieldTilde )
#voltageTilde = voltageTilde * (-1.)

#-------------------
#Do inverse transform to get voltage

voltage = fft.ifft(voltageTilde)

#Add boundary condition that v = 0 t x = o
voltage = voltage - voltage[0]

#Add in the m*x term proportional to fieldTilde[0]/2
#Alsoneeds normalising by samples/2 this is fft.fft feature
voltage = voltage + (fieldTilde[0]/2.)*distances * (2./samples)

fig.add_subplot(515)
plt.plot( distances, voltage.real, distances, voltage.imag )
plt.title('Voltage')




plt.show()



