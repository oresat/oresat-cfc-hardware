# This script takes raw images from OreSat CFC sensor and plots a histogram
# of the values along with a line plot of the cumulative distribution function.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
import sys
bins=200
# For Mac OS X:
# set MPLBACKEND environment variable or
# put backend: MACOSX in matplotlibrc file
# or uncomment the following line:
# mp.use("MACOSX")

def plothisto(file):
    data = np.fromfile(file, dtype=np.uint16)
    fig, ax = plt.subplots(ncols=1)
    ax1 = ax.twinx()
    ax1.tick_params(axis='y',colors='red')
    ax.hist(data,density=False, bins=bins, range=[0,16384])
    N = data.size
    X2 = np.sort(data)
    F2 = np.array(range(N))/float(N)
    ax1.plot(X2, F2,alpha=0.3,color='red')
    plt.show()

if __name__ == "__main__" and "get_ipython" not in dir():
    plothisto(sys.argv[1])
