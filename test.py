import numpy as np
from numpy.random import randint as rd
import matplotlib.pyplot as plt
 
L = 6

for i in range (L):
    if (i%2==0):
        for j in range (2):
            a  = np.resize([1,0],(2*L,))  
            plt.matshow(a)
    else:
        for j in range (2):
            a  = np.resize([0,1],(2*L,))
            plt.matshow(a)

plt.plot()

