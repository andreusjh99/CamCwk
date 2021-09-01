# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 22:56:00 2018

@author: HP
"""

from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    s = build_station_list()
    print(inconsistent_typical_range_stations(s))
    
if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
