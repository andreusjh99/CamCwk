# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 17:56:10 2018

@author: HP
"""

import matplotlib as mplot
import matplotlib.pyplot as plt

from floodsystem.analysis import polyfit

import numpy as np 

#Task2E
def plot_water_levels(station, dates, levels):
    
    plt.plot(dates, levels, label = 'actual level')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation = 45)
    
    station_typical_low = [station.typical_range[0]]*(len(dates))
    station_typical_high = [station.typical_range[1]]*(len(dates))
            
    plt.plot(dates, station_typical_low, label = 'typical low')
    plt.plot(dates, station_typical_high, label = 'typical high')
    
    plt.title(station.name)
    plt.legend()
    
    plt.tight_layout()
    plt.show()

#Task2F
def plot_water_level_with_fit(station, dates, levels, p):
    plt.plot(dates, levels, label = 'actual level')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation = 45)
    
    poly, d0 = polyfit(dates, levels, p)
    
    x = mplot.dates.date2num(dates)
    polylist = poly(x - d0)
    plt.plot(dates, polylist, label = "polyfit")
    
    station_typical_low = [station.typical_range[0]]*(len(dates))
    station_typical_high = [station.typical_range[1]]*(len(dates))
            
    plt.plot(dates, station_typical_low, label = 'typical low')
    plt.plot(dates, station_typical_high, label = 'typical high')
    
    plt.title(station.name)
    plt.legend()
    plt.tight_layout()
    plt.show()
    
# Task 2G
# took average of last 3 gradient values to determine most recent change in water levels (predicting trends)
def gradient_plot(dates, levels, p):
    for i in range(len(levels)):
        try:
            len(levels[i])
            levels[i]=levels[i][0]
        except:
            pass
    if len(levels) == 0:
        return None
    poly, d0 = polyfit(dates, levels, p)
    
    x = mplot.dates.date2num(dates) 
    polylist = poly(x - d0)
    
    gradient = np.gradient(polylist, 0.1)
    averagegradient = (gradient[-1] + gradient[-2] + gradient[-3])/3
    return averagegradient

    

    