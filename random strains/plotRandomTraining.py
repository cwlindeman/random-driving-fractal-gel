import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv
import random
import time
import sys
import os
import scipy.signal


matplotlib.rc('xtick', labelsize=10)
matplotlib.rc('ytick', labelsize=10)
plt.figure(figsize=(3.4, 1.5))

file = "3%_readout_notraining/3%_random-training/3%_random-training-11_cycles.csv"
data = np.transpose(np.loadtxt(file, skiprows=1, delimiter=','))

t = data[1,:] 
V = data[2,:] # recorded data is in volts
gamma_per_V = 3/np.max(V) # convert to strain

plt.plot(t, gamma_per_V*V, '-', color='k')

plt.xlabel("time (s)")
plt.ylabel("strain (%)")
plt.yticks([-3,0,3])
plt.ylim([-5,5])
plt.tight_layout()
#plt.savefig("random-training.pdf")
plt.show()
plt.clf()
