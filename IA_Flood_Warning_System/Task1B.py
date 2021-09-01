# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 00:28:59 2018

@author: HP
"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    s = build_station_list()
    stations = stations_by_distance(s, (52.2053, 0.1218))
    n10 = stations[: 10]
    f10 = stations[-10 :]
    near10 = []
    far10 = []
    for i in range(10):
        for j in range(len(s)):
            if n10[i][0] == s[j].name:
                near10.append((n10[i][0], s[j].town, n10[i][1]))
            if f10[i][0] == s[j].name:
                far10.append((f10[i][0], s[j].town, f10[i][1]))
    print(near10)
    print(far10)
    
if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
    