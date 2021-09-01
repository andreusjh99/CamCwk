# -*- coding: utf-8 -*-
"""
Created on Mon May 14 00:36:32 2018

@author: HP
"""

import numpy as np

def f(x):
    return (2 - x[0])**2 + 100*(x[1] - x[0]**2)**2

def g(x):
    dfdx0 = -2*(2-x[0]) - 400*(x[1] - (x[0])**2)*(x[0])
    dfdx1 = 200*(x[1] - (x[0])**2)
    return np.array([dfdx0, dfdx1])
    
def J(x):
    d2fdx02 = 2 - 400*(x[1] - x[0]**2) + 800*x[0]**2
    d2fdx12 = 200
    d2fdx0dx1 = -400*x[0]
    return np.array([[d2fdx02, d2fdx0dx1],
            [d2fdx0dx1, d2fdx12]])
    
def newton(x0, g, J, tol):
    xn = x0
    counter = 1
    while np.linalg.norm(g(xn))/np.linalg.norm(g(x0)) >= tol:
        xn1 = xn - np.linalg.solve(J(xn), g(xn))
        print(xn1)
        print(counter)
        xn = xn1
        
        counter += 1
        if counter > 2000:
            print("error")
            break
        
newton([1.1, 1.1], g, J, 1e-9)