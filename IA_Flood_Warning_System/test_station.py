"""Unit test for the station module"""

import pytest
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import relative_water_level

#1A and 1F
def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (2.3, -3.4445)
    river = "River X"
    town = "My Town"
    latest_level = 3 
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    p = MonitoringStation(s_id, m_id, label, coord, None, river, town)
    
    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town
    assert s.typical_range_consistent() == False
    assert p.typical_range == None
    assert p.typical_range_consistent() == False
    
    
#1F
def test_inconsistent_typical_range_stations():
    
    station1 = MonitoringStation("jh", 99, "Cam", (2, 5.78), (2, -2.3), "River X", "My town")
    station2 = MonitoringStation("jr", 99, "Thames", (2, 7.7), (2, 2.3), "River y", "My town")
    station3 = MonitoringStation("aj", 99, "Seine", (2, 10.34), None, "River z", "My town")
    stations = [station1, station2, station3]
    
    assert inconsistent_typical_range_stations(stations) == ["Cam", "Seine"]
    
#2B
def test_relative_water_level():
    
    station1 = MonitoringStation("jh", 99, "Cam", (2, 5.78), (2, -2.3), "River X", "My town")
    station2 = MonitoringStation("jr", 99, "Thames", (2, 7.7), (2, 2.3), "River y", "My town")
    station3 = MonitoringStation("aj", 99, "Seine", (2, 10.34), None, "River z", "My town")
    station1.latest_level = 2
    station2.latest_level = 2.15
    station3.latest_level = None
 

    
    assert relative_water_level(station1) == None
    assert relative_water_level(station2) == 0.5
    assert relative_water_level(station3) == None
    




    
    
    