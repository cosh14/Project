import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randint as rd
from numpy.random import rand

import time
start_time = time.time()


def GenerateSqLattice(N):
    config = (2*rd(0,2,(N,N)))-1
    return config

#print (GenerateSqLattice(3))

def intrxEcalc (Lattice, a, b):
    intrxE = 0 # E = -1 if aligned, +1 if not aligned
    s = Lattice [a,b]

    if Lattice [(a+1)%N,b] == s:
        intrxE += -1
    else:
        intrxE += 1
    if Lattice [(a-1)%N,b] == s:
        intrxE += -1
    else:
        intrxE += 1
    if Lattice [a,(b+1)%N] == s:
        intrxE += -1
    else:
        intrxE += 1
    if Lattice [a,(b-1)%N] == s:
        intrxE += -1
    else:
        intrxE += 1
    return  intrxE
    

def MetropolisMonteCarlo (Lattice, T):
    for j in range (5000):
        for i in range (5000):
            a = rd (0,N)
            b = rd (0,N) 
            intrxE0 = intrxEcalc (Lattice, a, b)
            Lattice[a,b] *= -1
            intrxE1 = intrxEcalc (Lattice, a, b)
            if (intrxE1-intrxE0) > 0 and rand() > np.exp(-(intrxE1-intrxE0)/T):
                Lattice[a,b] *=-1
    return Lattice

def MagCalc (Lattice):
    mag = np.sum (Lattice)
    return mag



myTval = [0.1, 0.1, 0.5, 1, 2, 2.22, 2.24, 2.26, 2.28, 2.30, 2.5, 3, 5]
#print(myTval)

N=80
config = GenerateSqLattice(N)

plt.matshow(config)
plt.show()

for i in range (len(myTval)):
    plt.matshow(MetropolisMonteCarlo (config, myTval[i]))
    print("--- %s T ---" % (myTval[i]))
    print("--- %s M ---" % (MagCalc(config)))
    plt.show()
    print("--- %s seconds ---" % (time.time() - start_time))

