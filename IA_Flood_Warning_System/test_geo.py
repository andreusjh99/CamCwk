# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 23:27:44 2018

@author: HP
"""

import pytest
#Task1B
from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation

def test_stations_by_distance():
    
    #create a list
    station1 = MonitoringStation("jh", 99, "Cam", (2, 5.78), (2, 2.3), "River X", "My town")
    station2 = MonitoringStation("jr", 99, "Thames", (2, 7.7), (2, 2.3), "River y", "My town")
    station3 = MonitoringStation("aj", 99, "Seine", (2, 10.34), (2, 2.3), "River z", "My town")
    stations = [station1, station2, station3]
    
    s = stations_by_distance(stations, (2, 5))
    
    assert s[0][0] == "Cam"
    assert s[1][0] == "Thames"
    assert s[2][0] == "Seine"
    

#Task1C
from floodsystem.geo import stations_by_radius

def test_stations_by_radius():
    
    #create a list
    station1 = MonitoringStation("jh", 99, "Cam", (2, 5.78), (2, 2.3), "River X", "My town")
    station2 = MonitoringStation("jr", 99, "Thames", (2, 7.7), (2, 2.3), "River y", "My town")
    station3 = MonitoringStation("aj", 99, "Seine", (2, 10.34), (2, 2.3), "River z", "My town")
    stations = [station1, station2, station3]
      
    assert stations_by_radius(stations, (2, 5), 10) == []
    assert stations_by_radius(stations, (2, 5), 400) == ['Cam', 'Thames']
    
#Task1D
from floodsystem.geo import rivers_with_station

def test_rivers_with_station():
    station1 = MonitoringStation("jh", 99, "Cam", (2, 5.78), (2, 2.3), "River X", "My town")
    station2 = MonitoringStation("jr", 99, "Thames", (2, 7.7), (2, 2.3), "River y", "My town")
    station3 = MonitoringStation("aj", 99, "Seine", (2, 10.34), (2, 2.3), "River z", "My town")
    station4 = MonitoringStation("aj", 99, "Meh", (2, 10.34), (2, 2.3), "River z", "My town")
    stations = [station1, station2, station3, station4]
    
    riversettest = rivers_with_station(stations)
    
    assert riversettest == (3, ['River X', 'River y', 'River z'])
    
from floodsystem.geo import stations_by_river

def test_stations_by_river():
    station1 = MonitoringStation("jh", 99, "Cam", (2, 5.78), (2, 2.3), "River X", "My town")
    station2 = MonitoringStation("jr", 99, "Thames", (2, 7.7), (2, 2.3), "River y", "My town")
    station3 = MonitoringStation("aj", 99, "Seine", (2, 10.34), (2, 2.3), "River z", "My town")
    station4 = MonitoringStation("aj", 99, "Meh", (2, 10.34), (2, 2.3), "River z", "My town")
    stations = [station1, station2, station3, station4]
    
    riverdicttest = stations_by_river(stations)
    stationsonriver = riverdicttest["River z"]
    stationsonriver.sort()
    
    
    
    assert stationsonriver == ["Meh", "Seine"]

#Task1E
from floodsystem.geo import rivers_by_station_number

def test_rivers_by_station_number():
    station1 = MonitoringStation("jh", 99, "Cam", (2, 5.78), (2, 2.3), "River X", "My town")
    station2 = MonitoringStation("jr", 99, "Thames", (2, 7.7), (2, 2.3), "River y", "My town")
    station3 = MonitoringStation("aj", 99, "Seine", (2, 10.34), (2, 2.3), "River z", "My town")
    station4 = MonitoringStation("aj", 99, "Meh", (2, 10.34), (2, 2.3), "River z", "My town")
    stations = [station1, station2, station3, station4]
    
    riversbystationnumber = rivers_by_station_number(stations, 2)
    
    assert riversbystationnumber == [('River z', 2), ('River X', 1), ('River y', 1)]


    

