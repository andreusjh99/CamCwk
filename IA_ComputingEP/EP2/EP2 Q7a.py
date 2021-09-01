# -*- coding: utf-8 -*-
"""
Created on Mon May 14 01:12:40 2018

@author: HP
"""
import numpy as np

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

class Rosenbrock:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def f(self, x):
        return (self.a - x[0])**2 + self.b*(x[1] - x[0]**2)**2
    
    def g(self, x):
        dfdx0 = -2*(self.a-x[0]) - 4*self.b*(x[1] - (x[0])**2)*(x[0])
        dfdx1 = 2*self.b*(x[1] - (x[0])**2)
        return np.array([dfdx0, dfdx1])
    
    def J(self, x):
        d2fdx02 = 2 - 4*self.b*(x[1] - x[0]**2) + 8*self.b*x[0]**2
        d2fdx12 = 2*self.b
        d2fdx0dx1 = -4*self.b*x[0]
        return np.array([[d2fdx02, d2fdx0dx1],
                         [d2fdx0dx1, d2fdx12]])
    
R1 = Rosenbrock(3, 150)    

newton([1.1, 1.1], R1.g, R1.J, 1e-9)
