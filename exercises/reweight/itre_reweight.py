import itre
import json
import os
import matplotlib.pyplot as plt
import numpy as np

#LOAD THE CVs AND THE BIAS
colvars = np.loadtxt('colvar')
bias = colvars[1:,-1]
new_cvs = colvars[1:,1:-1]

# LOAD AND REPEAT C(T) TO HAVE THE RIGHT WEIGHT
c_t = np.loadtxt('ct.dat')
ct = np.repeat(c_t,10)
weights = np.exp(1.0*(bias-ct))

# READ THE REFERENCE BIN FROM THE REFERENCE
ref_2d = np.loadtxt('reference/reference_fes.dat')
bins = np.loadtxt('reference/bins_x.dat')
new_bin = bins+np.abs(bins[1]-bins[0])/2

# CALCULATE THE FES
h_2d,e1,e2 = np.histogram2d(new_cvs.T[0],new_cvs.T[1],weights=weights,bins=bins)
h_2d = h_2d/h_2d.sum()
fes_2d = -1.0*np.log(h_2d)

levs = np.linspace(0,50,10)


# PLOT!
points = int(np.sqrt(len(ref_2d)))
plt.contour(bins,bins,ref_2d.reshape(points,points).T,levs,colors='k')
plt.colorbar()
plt.contourf(new_bin[:-1],new_bin[:-1],fes_2d.T,levs)
plt.colorbar()

plt.show()
