# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 20:10:17 2018

@author: HP
"""

from floodsystem.station import MonitoringStation
from floodsystem.station import relative_water_level 
from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    stationsover = []
    for i in range(len(stations)): 
        if relative_water_level(stations[i]) != None:
            if relative_water_level(stations[i]) > tol:
                newstationsover = (stations[i].name, relative_water_level(stations[i]))
                stationsover.append(newstationsover) 
            else: 
                pass
        stationsover = sorted_by_key(stationsover, 1, reverse=True)
    return (stationsover)

def stations_highest_rel_level(stations, N):
    stationsrellevel = []
    for i in range(len(stations)): 
        if relative_water_level(stations[i]) != None:
            newstationsrellevel = (stations[i].name, relative_water_level(stations[i]))
            stationsrellevel.append(newstationsrellevel) 
        else: 
            pass
        stationsrellevel = sorted_by_key(stationsrellevel, 1, reverse=True)
    return (stationsrellevel[0:N])

    