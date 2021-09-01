# -*- coding: utf-8 -*-
"""
Created on Sun May 13 23:14:46 2018

@author: HP
"""
import numpy as np
import matplotlib.pyplot as plt

A = plt.imread("https://github.com/CambridgeEngineering/PartIA-Computing-Examples-Papers/raw/master/images/southwing.png")
plt.imshow(A, cmap='gray');
print("Image array shape (pixels): {}".format(A.shape))
print(type(A))
print(A.shape)

def convol(g, a, i, j):
    sum = 0
    d = np.floor_divide(len(g), 2)
    for k in range(len(g)):
        for l in range(len(g)):
            sum += (g[k][l])*a[i-d+k][j-d+l]
    return sum

B = np.zeros(A.shape)

g = [[-1, -1, -1],
     [-1,  8, -1],
     [-1, -1, -1]]

for i in range(1, B.shape[0]-1):
    for j in range(1, B.shape[1]-1):
        B[i, j] = convol(g, A, i, j)
        
plt.imshow(B, cmap = "gray");