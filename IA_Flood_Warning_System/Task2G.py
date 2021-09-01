# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 22:39:34 2018

@author: GL553VW FY101T
"""

# 2 main criteria involved: 1. rel level, 2. rate of change 

import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit, gradient_plot
from floodsystem.flood import stations_level_over_threshold
import numpy as np

def run():
    stations = build_station_list()
    update_water_levels(stations)
    stationsR = stations_level_over_threshold(stations, 0.5)
    
    for i in range(len(stationsR)):
        print(stationsR[i][0])
    
        if stationsR[i][1] < 0.6 :
            p = 1
        elif 0.6 <= stationsR[i][1] < 0.8:
            p = 2
        elif 0.8 <= stationsR[i][1] < 1:
            p = 3
        elif 1 <= stationsR[i][1] < 1.2:
            p = 4
        elif 1.2  <= stationsR[i][1] < 1.6:
            p = 5
        elif 1.6 <= stationsR[i][1] < 2:
            p = 6
        elif 2 <= stationsR[i][1] :
            p = 7
        
                
        dates, levels = fetch_measure_levels(stations[i].measure_id,
                                         dt=datetime.timedelta(days=2)) 
        rateofchange = gradient_plot(dates, levels, 4)
        
        
        if rateofchange == None:
            print ('Missing data for this station')
            
        else:
            rateofchange = float(rateofchange)
            
            if rateofchange < 1e-05 :
                p += 1
                
            elif 1e-05 <= rateofchange < 1e-04 :
                p += 2
                 
            elif 1e-04 <= rateofchange < 5e-04 :
                p += 3
            
            elif 5e-04 <= rateofchange < 1e-03 :
                p += 4
            
            elif 1e-03 <= rateofchange :
                p += 5
                
            if p >= 7:
                print('Severe Risk: Run for your life!!!')
            elif p >= 5: 
                print('High Risk: Prepare to evacuate!!')
            elif p >= 4:
                print('Moderate Risk: Stay alert!')
            elif p >= 3:
                print('Low Risk: Will probably be fine' )
            else:
                print('Congratulations, if this prediction system works properly, you should be deemed safe')
        
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
    