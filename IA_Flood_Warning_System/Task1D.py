# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 22:00:07 2018

@author: GL553VW FY101T
"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    s = build_station_list()
    stationsonriver = stations_by_river(s) 
    print (rivers_with_station(s))
    print (sorted(stationsonriver["River Aire"]))
    print (sorted(stationsonriver["River Cam"]))
    print (sorted(stationsonriver["Thames"]))
    

    
if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()

  