# -*- coding: utf-8 -*-
"""
Created on Sun May 13 12:47:53 2018

@author: HP
"""
import math

def linear(n, m):
    return m*(10**(-8))*n

def binary(n, m):
    return 2*(10**(-5))*n*math.log(n) + m*((10**(-6))*math.log(n))

n = 26*10e6
m = [10**3, 10**4, 3*10e5, 5*10e5]

for i in range(len(m)):
    print ("linear: ", linear(n, m[i]))
    print ("binary: ", binary(n, m[i]))
    if linear(n, m[i]) > binary(n, m[i]):
        print("BINARY")
    else:
        print("LINEAR")