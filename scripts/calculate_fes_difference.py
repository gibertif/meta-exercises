import numpy as np
import matplotlib.pyplot as plt
import argparse as ap
import os
import re

parser = ap.ArgumentParser('Calculate the Free Energy Difference between two neighbourhoods in CVs space')
parser.add_argument('--prefix',help='prefix of the FES to calculate the FE difference',required=True)
parser.add_argument('--mina',nargs='+',type=float,help='Neighbourhood of the first minimum. Expecting 2 numbers with 1D CVs and 4 numbers with 2D CVs. Provide the number from smaller (more negatve) to larger (more positive)',required=True)
parser.add_argument('--minb',nargs='+',type=float,help='Neighbourhood of the first minimum. Expecting 2 numbers with 1D CVs and 4 numbers with 2D CVs. Provide the number from smaller (more negatve) to larger (more positive)',required=True)
parser.add_argument('--kt',type=float,help='Boltzmann caliber for the simulation',required=True)

args = parser.parse_args()

kt = args.kt

try:
    len(args.mina) != len(args.minb)
except:
    raise ValueError('You need to use he same number of boundaries for the two minima')

num_fes_files = 0
fes_files = []
for root,dirs,files in os.walk('./'):
    for file in files:
        if args.prefix in file:
            num_fes_files += 1
            fes_files.append(file)


def get_number(str):
    for s in str.replace('.','_').split('_'):
        if s.isdigit():
            return int(s)

free_energy_diff=[]
for i in sorted(fes_files,key=get_number):

    fes = np.loadtxt(i)
    if fes.shape[-1] > 3:
        prob = np.exp(-fes.T[2]/kt)

        prob_a = prob[np.where(
            np.logical_and(
                np.logical_and(fes.T[0]>args.mina[0],fes.T[0]<args.mina[1]),
                np.logical_and(fes.T[1]>args.mina[2],fes.T[1]<args.mina[3])
            )
        )].sum()
        prob_b = prob[np.where(
            np.logical_and(
                np.logical_and(fes.T[0]>args.minb[0],fes.T[0]<args.minb[1]),
                np.logical_and(fes.T[1]>args.minb[2],fes.T[1]<args.minb[3])
            )
        )].sum()

    else:
        prob = np.exp(-fes.T[1]/kt)
        prob_a = prob[np.where(np.logical_and(fes.T[0]>args.mina[0],fes.T[0]<args.mina[1]))].sum()
        prob_b = prob[np.where(np.logical_and(fes.T[0]>args.minb[0],fes.T[0]<args.minb[1]))].sum()

    print(i,prob_a,prob_b)

    if prob_b > 0.0:
        free_energy_diff.append(-kt*np.log(prob_a/prob_b))

free_energy_diff = np.array(free_energy_diff)
plt.plot(free_energy_diff)
plt.show()
