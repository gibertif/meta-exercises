import itre
import json
import os
import matplotlib.pyplot as plt
import numpy as np
import time

hills = np.loadtxt('HILLS')
cvs = hills.T[1]
sigmas = hills.T[2]
heights = hills.T[3]

limit = [1000,len(cvs)]

for ss in limit:

    new_it=itre.Itre()
    new_it.use_numba=True
    new_it.colvars=cvs[:ss]
    new_it.kT=1.0

    new_it.wall=np.zeros(len(cvs[:ss]))
    new_it.sigmas=sigmas[:ss]
    new_it.heights=heights[:ss]/heights[0]*1.0
    new_it.stride=10
    new_it.n_evals=int(ss/10)
    new_it.calculate_c_t()


np.savetxt('ct.dat',new_it.ct[-1].T)

colvars = np.loadtxt('colvar')
bias = colvars[1:,-1]

plt.plot(bias[::10],label='meta bias')
plt.plot(new_it.instantaneous_bias,label='ITRE bias')
plt.plot(new_it.ct[-1].T,label='c(t)')
plt.legend()
plt.show()
