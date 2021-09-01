# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 02:53:39 2018

@author: HP
"""

import numpy as np
import matplotlib as mplot

#Task2F
def polyfit(dates, levels, p):
    x = mplot.dates.date2num(dates)
    d0 = np.min(x)
    
    p_coeff = np.polyfit(x - d0, levels, p)
    
    poly = np.poly1d(p_coeff)
    
    return poly, d0

