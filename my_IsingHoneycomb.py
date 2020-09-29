import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randint as rd
from numpy.random import rand
import itertools
import time
start_time = time.time()


def GenerateHexLattice(N):
    config = (2*rd(0,2,(N,N)))-1
    #config = (2*rd(0,1,(N,N)))-1
    k = 0
    while k <N:
        i = 0
        j = 2
        while j < N:
            config [j][k] = 0
            config [j+1][k] = 0 
            j = j + 4
        while i < N:    
            config [i][k+1] = 0
            config [i+1][k+1] = 0
            i = i + 4
        k = k+2
    return config            

def intrxEcalc (Lattice, a, b):
    intrxE = 0 # E = -1 if aligned, +1 if not aligned
    s = Lattice [a,b]
    if s == 0:
        return 0   
    elif Lattice [(a+1)%N,b] == 0:
        if Lattice [(a-1)%N,b] == s:
            intrxE += -1
        else:
            intrxE += 1
        if Lattice [(a+1)%N,(b+1)%N] == s:
            intrxE += -1
        else:
            intrxE += 1
        if Lattice [(a+1)%N,(b-1)%N] == s:
            intrxE += -1
        else:
            intrxE += 1
    else:
        if Lattice [(a+1)%N,b] == s:
            intrxE += -1
        else:
            intrxE += 1
        if Lattice [(a-1)%N,(b+1)%N] == s:
            intrxE += -1
        else:
            intrxE += 1
        if Lattice [(a-1)%N,(b-1)%N] == s:
            intrxE += -1
        else:
            intrxE += 1
    return  intrxE 

def graph (df):
    plt.pcolormesh(df, edgecolors='k', linewidth=0.5)
    ax = plt.gca()
    ax.set_aspect('equal')
    return 0

def MetropolisMonteCarlo (Lattice, T):
    for j in range (8):
        for i in range (8):
            a = rd (0,N)
            b = rd (0,N)
            print (Lattice[a,b])
            intrxE0 = intrxEcalc (Lattice, a, b)
            Lattice[a,b] *= -1
            intrxE1 = intrxEcalc (Lattice, a, b)
            if (intrxE1-intrxE0) > 0 and rand() > np.exp(-(intrxE1-intrxE0)/T):
                Lattice[a,b] *=-1
    return a,b

def MagCalc (Lattice):
    mag = np.sum (Lattice)
    return mag

N = 8
seti = GenerateHexLattice(N)
MetropolisMonteCarlo (seti, 1)


myTval = np.linspace(0.5,2.2,25)
 
N=80
N_loops = 10
config = GenerateHexLattice(N)
sites = np.count_nonzero(config)
print (sites)
bank = np.zeros((len(myTval),N_loops))
graph(config)



for i in range (len(myTval)):
    tempo_mag = np.zeros(N_loops, dtype=float)
    config = GenerateHexLattice(N)
    for m in range (N_loops):
        MetropolisMonteCarlo (config, myTval[i])
        #print("--- %s T ---" % (myTval[i]))
        #print("--- %s M ---" % (MagCalc(config)/(N*N)))
        tempo_mag [m] = MagCalc(config)/(sites)
    #plt.matshow(config)
    #plt.show()
    print("--- %s seconds ---" % (time.time() - start_time))
    bank [i] = tempo_mag


plt.matshow(bank)
plt.xlabel("Trial #")
plt.ylabel("Temperature")
cbar= plt.colorbar()
cbar.set_label("Magnetization", labelpad=+1)
plt.show()

#post processing

bank_avg = np.zeros(len(myTval))
for i in range (len(myTval)):
    bank_avg[i] = np.average(bank[i,:])
print (bank_avg)

for i in range (len(myTval)):
    temp = np.full(N_loops,myTval[i])
    plt.scatter(temp, bank[i])
plt.plot (myTval,bank_avg)
plt.title ("Magnetization v T")
plt.xlabel("Temp")
plt.ylabel("Magnetization")
plt.show
