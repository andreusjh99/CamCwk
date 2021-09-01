# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 17:46:33 2018

@author: HP
"""
import numpy as np
x = [1, 0, 0]
#x = 0
print(x)
print(type(x))

x_list = []

"""x_list.append(x)
print(x_list)
y = [2, 0, 0]
x = y

x_list.append(y)"""

"""y = x[0]
y += 10
print(y)
print(x_list)
x_list.append(y)"""


"""for i in range(10):
    x += 10
    print(x)
    x_list.append(x)"""
    

for i in range(10):
    z = []
    for j in range(len(x)):
        x[j] += 1
        z.append(x[j])
    x_list.append(z)

print(x_list)
print(type(x_list))
print(type(x_list[0]))

a = [1, 2]
print(len(a))
print(a[-1])
print(a[-2])