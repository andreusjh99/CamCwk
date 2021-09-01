# -*- coding: utf-8 -*-
"""
Created on Mon May 14 00:12:28 2018

@author: HP
"""
import numpy as np

def newton(x0, fprime, fpprime, tol):
    xn = x0
    counter = 1
    while np.abs(fprime(xn))/np.abs(fprime(x0)) >= tol:
        xn1 = xn - ((fpprime(xn))**(-1))*fprime(xn)
        print(xn1)
        print(counter)
        xn = xn1
        
        counter += 1
        if counter > 2000:
            print("error")
            break
    
def f(x):
    return 2*(x**2) + 6*x
def fprime(x):
    return 4*x + 6
def fpprime(x):
    return 4

newton(5, fprime, fpprime, 1e-10)

def g(x):
    return x**3 + x**2
def gprime(x):
    return 3*(x**2) + 2*x
def gpprime(x):
    return 6*x + 2

newton(-5, gprime, gpprime, 1e-6)