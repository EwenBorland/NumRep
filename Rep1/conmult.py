from scipy import misc
import matplotlib.pyplot as plt
from scipy.fftpack import fft ,ifft
import numpy as np
import sys

fn = "desync1.pgm"
im = misc.imread(fn)
rownum = 10
outrow  = ifft((np.conjugate(fft(im[rownum-1])))*fft(im[rownum]))
maxpixel  = np.argmax(outrow)
pixels = range(0,len(im[rownum]))
plt.plot([maxpixel,maxpixel],[min(outrow),max(outrow)],'r--',label="Location of Maximum")
plt.plot(pixels,outrow,'b-',label="iFT of cross correlation product")
plt.xlabel("Pixel")
plt.ylabel("iFT of cross-correlation product")
plt.title("Inverse FT of the cross correlation product\n between lines 9 and 10 in desync1.pgm against pixel.\n Maximum shows shift length of line 10",fontsize = 11)
plt.legend()
plt.savefig("crosscol.eps")
plt.show()
