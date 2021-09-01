# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:10:08 2018

@author: GL553VW FY101T
"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import relative_water_level
from floodsystem.flood import stations_highest_rel_level

def run():
    s = build_station_list()
    update_water_levels(s)
    ss = stations_highest_rel_level(s, 10)
    for i in ss:
        print (i[0], ": ", i[1], sep="")
        
    
    
if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()