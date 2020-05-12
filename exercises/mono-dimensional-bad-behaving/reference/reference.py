import numpy as np

x = np.linspace(-1.25,1.25,100)

def func(x,alpha=1):
    data = x**2*((1.35*x-1)*(x+1))*alpha
    mn = np.amin(data)
    return data - mn

#import matplotlib.pyplot as plt
#plt.plot(x,func(x,alpha=200))
np.savetxt('reference_fes.dat',np.c_[x,func(x,alpha=200)])
