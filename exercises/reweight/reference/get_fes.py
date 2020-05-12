import numpy as np
import matplotlib.pyplot as plt

pes = np.loadtxt('pes',usecols=1)
pes -= np.amin(pes)
pes.shape
levs = np.arange(0,50,5)
pes[pes>40]=40
pes.shape
plt.contourf(pes.reshape(200,200).T)
plt.contour(pes.reshape(200,200).T,colors='k')
plt.colorbar()
np.savetxt('reference_fes.dat',pes)

prob = np.exp(-pes.reshape(200,200))
prob_x = prob.sum(axis=0)
prob_y = prob.sum(axis=1)
pes_x = -np.log(prob_x/prob_x.sum())
pes_y = -np.log(prob_y/prob_y.sum())

pes_x -= np.amin(pes_x)
pes_y -= np.amin(pes_y)

x = np.linspace(-2,2,200)

np.savetxt('reference_proj_x.dat',np.c_[x,pes_x])
np.savetxt('reference_proj_y.dat',np.c_[x,pes_y])
