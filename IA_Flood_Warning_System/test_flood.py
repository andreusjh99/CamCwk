# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 17:45:34 2018

@author: GL553VW FY101T
"""

import pytest
from floodsystem.station import MonitoringStation
from floodsystem.station import relative_water_level
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level


#2B
def test_stations_level_over_threshold(): 
    station1 = MonitoringStation("jh", 99, "Cam", (2, 5.78), (2, -2.3), "River X", "My town")
    station2 = MonitoringStation("jr", 99, "Thames", (2, 7.7), (2, 2.3), "River y", "My town")
    station3 = MonitoringStation("aj", 99, "Seine", (2, 10.34), None, "River z", "My town")
    station4 = MonitoringStation("meh", 99, "xxxx", (2, 8.7), (1, 4.3), "River y", "My town")
    stations = [station1, station2, station3, station4]
    station1.latest_level = 2
    station2.latest_level = 2
    station3.latest_level = 2
    station4.latest_level = 4.3
    

    
    assert stations_level_over_threshold(stations, 0.8) == [('xxxx', 1.0)]


#2C
def test_stations_highest_rel_level(): 
    station1 = MonitoringStation("jh", 99, "Cam", (2, 5.78), (2, -2.3), "River X", "My town")
    station2 = MonitoringStation("jr", 99, "Thames", (2, 7.7), (2, 2.3), "River y", "My town")
    station3 = MonitoringStation("aj", 99, "Seine", (2, 10.34), None, "River z", "My town")
    station4 = MonitoringStation("meh", 99, "xxxx", (2, 8.7), (1, 4.3), "River y", "My town")
    stations = [station1, station2, station3, station4]
    station1.latest_level = 2
    station2.latest_level = 2.15
    station3.latest_level = 2
    station4.latest_level = 4.3


    assert stations_highest_rel_level(stations,2) == [('xxxx', 1.0), ('Thames', 0.5)]

    
    