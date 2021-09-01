# -*- coding: utf-8 -*-
"""
Created on Sun May 13 21:15:10 2018

@author: HP
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 50)

def f(x):
    return np.sin(x) + (np.cos(10*x))/5

def average(x, f):
    av = []
    for i in range(len(x)-2):
        sum = f(x[i]) + f(x[i+1]) + f(x[i+2])
        av.append(sum/3)
        
        if i == len(x)-3:
            av.append((f(x[i+1])+f(x[i+2]))/2)
            av.append(f(x[i+2]))
            
    return av


plt.plot(x, f(x), label = "original")
plt.plot(x, average(x, f), label = "smoothed")
plt.legend()
plt.show()