# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:07:10 2018

@author: GL553VW FY101T
"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import relative_water_level
from floodsystem.flood import stations_level_over_threshold

def run():
    s = build_station_list()
    update_water_levels(s)
    ss = stations_level_over_threshold(s, 1.2)
    for i in ss:
       print (i[0], ": ", i[1], sep="")
        
    
   
if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()