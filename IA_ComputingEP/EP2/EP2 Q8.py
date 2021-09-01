# -*- coding: utf-8 -*-
"""
Created on Mon May 14 01:30:09 2018

@author: HP
"""

nodes = {}

nodes["town 0"] = [("town 2", 3), ("town 3", 8)]
nodes["town 1"] = [("town 4", 14), ("town 2", 2), ("town 5", 14)]
nodes["town 2"] = [("town 0", 3),  ("town 1", 2),  ("town 3", 4)]
nodes["town 3"] = [("town 0", 8),  ("town 2", 4),  ("town 4", 3)]
nodes["town 4"] = [("town 1", 14), ("town 3", 3)]
nodes["town 5"] = [("town 1", 14)]


dist = []
path = []
def distance(nodes, towni, townf):
    for i in range(len(nodes[towni])):
        
        if nodes[towni][i][0] != townf:
            townn = nodes[towni][i][0]
            path.append(towni)
            return nodes[towni][i][1] + distance(nodes, townn, townf)
        elif nodes[towni][i][0] == townf:
            return nodes[towni][i][1]
            break