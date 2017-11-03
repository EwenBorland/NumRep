#------------------
# Discrete fourier transform usinf numpy.fft
#
# Its hard to make it more difficult than this !
#
# This example shows th power of numpy arrays which parallelises everything
#

import numpy as np
from numpy import fft
import matplotlib.pyplot as plt

fig = plt.figure()

#-----------------
# Create the input waveform in the time domain

samples = 100
increments = np.arange(samples)

#Make up a list of times in in a single period of 0 ->> 2*pi
times = 2.0*3.14159/float(samples)*increments

#Create the time domain signal with the required number of samples
amplitudeTime = (1+3*(np.cos(16.*times))) + np.sin(3.6*times)

fig.add_subplot(211)
plt.plot( times, amplitudeTime, drawstyle='steps-mid' )
plt.title('Time domain')

#-----------------
# Create the transform in the frequency domain

# Perform fft
amplitudeF = fft.fft(amplitudeTime)

fig.add_subplot(212)
plt.plot( increments, amplitudeF.real, increments, amplitudeF.imag, drawstyle='steps-mid')
plt.title('Frequency domain')


plt.show()
