# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 20:56:17 2018

@author: GL553VW FY101T
"""


from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    s = build_station_list()
    print (rivers_by_station_number(s,11))
    

    
if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()