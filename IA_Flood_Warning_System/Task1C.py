# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 18:27:21 2018

@author: HP
"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_radius

def run():
    s = build_station_list()
    print(stations_by_radius(s, (52.2053, 0.1218), 10))
    
if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()