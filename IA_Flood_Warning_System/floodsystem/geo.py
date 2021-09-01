"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key

from haversine import haversine

from collections import Counter

# Build list of stations

#Task1B
def stations_by_distance(stations, p):
    stationList = []
    for i in range(len(stations)):
        distance = haversine(stations[i].coord, p)
        stationTuple = (stations[i].name, float(distance))
        stationList.append(stationTuple)
    sortedList = sorted_by_key(stationList, 1)
    return sortedList

#Task1C
def stations_by_radius(stations, centre, r):
    stationsList = stations_by_distance(stations, centre)
    stationsListR = []
    for i in range(len(stationsList)):
        if stationsList[i][1] <= r:
            stationsListR.append(stationsList[i][0])
        else:
            break
    stationsListR.sort()
    return stationsListR

#Task1D
riverset = set()
def rivers_with_station(stations):
    
    for i in range(len(stations)):
        if stations[i].name == None:
            pass 
        elif stations[i].river == None:
            pass
        else:
            riverset.add(stations[i].river)
    alphabeticalriverset = sorted(riverset)
    riversetx = set()
    for i in range(len(alphabeticalriverset)): 
        if i <=9:
            riversetx.add(alphabeticalriverset[i])
            
    riversety = sorted(riversetx)
    
    return len(riverset), riversety
    


def stations_by_river(stations):
    riverdict = {}
    for i in range(len(stations)):  
        if stations[i].river not in riverdict:
            riverdict[stations[i].river] = [stations[i].name]
        else:
            riverdict[stations[i].river].append(stations[i].name)
            
    return riverdict

#Task1E
    

def rivers_by_station_number(stations, N):
    rivers = (station.river for station in stations)
    most_common = Counter(rivers).most_common()
    
    x=0
    for i in range(len(most_common)):
        
        if most_common[i][1] == most_common[(N-1)][1]:
            x+=1
        else:
            pass 
       
 
    return most_common[:(N+x-1)]




    #riverTuples = []
    #rivers = (station.river for station in stations)
    #for i in range(len(stations)):
        #if stations[i].river not in riverTuples:
            #n = rivers.count(stations[i].river)
            #riverTuple = (stations[i].river, n)
            #riverTuples.append(riverTuple)
        #else:
            #pass
    #return riverTuples
    
        
    
    

            
            