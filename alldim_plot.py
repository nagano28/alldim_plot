# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:27:05 2018

@author: Nagano Masatoshi
"""

import numpy as np
import matplotlib.pyplot as plt
#import os

x = np.loadtxt('000.txt')

plt.figure()
t = range(len(x))
for d in range(len(x[0])):
    plt.plot( t, x[:,d] )
plt.savefig("./alldim_000.png")

