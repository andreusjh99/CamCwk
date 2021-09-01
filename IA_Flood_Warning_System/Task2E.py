# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 19:28:32 2018

@author: HP
"""

import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    stationsR = stations_highest_rel_level(stations, 5)
    
    for i in range(len(stationsR)):
        print(stationsR[i])
        for j in stations:
            if j.name == stationsR[i][0]:
                s = j
        dates, levels = fetch_measure_levels(s.measure_id,
                                         dt=datetime.timedelta(days=10))
        plot_water_levels(s, dates, levels)
        
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
    