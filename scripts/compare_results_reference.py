import numpy as np
import matplotlib.pyplot as plt
import argparse as ap

parser = ap.ArgumentParser('Check that the Metadynamics results are on top of analytical results')
parser.add_argument('--fes',help='the fes we just calculated')
parser.add_argument('--reference',help='the reference fes')
#parser.add_argument('--referece',help='the reference fes')

args  = parser.parse_args()

fes = np.loadtxt(args.fes)

if fes.shape[1] < 5:

    plt.plot(fes.T[0],fes.T[1],label='fes')
    if args.reference:
        ref = np.loadtxt(args.reference)
        plt.plot(ref.T[0],ref.T[1],label='ref')
    plt.legend()
    plt.show()

else:


    points = int(np.sqrt(len(fes)))
    x=np.unique(fes.T[0])
    y=np.unique(fes.T[1])
    levs = np.linspace(0,np.amax(fes[2]),10)
    plt.contourf(x,y,fes.T[2].reshape(points,points),levs)

    if args.reference:
        ref = np.loadtxt(args.reference)
        points = int(np.sqrt(len(ref)))
        x = y = np.linspace(-2,2,points)
        plt.contour(x,y,ref.reshape(points,points).T,levs,colors='k')

    plt.show()
