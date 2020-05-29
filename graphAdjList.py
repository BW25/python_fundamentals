# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:53:23 2019

@author: bdwoo
"""

class Edge:
    def __init__(self, dest, weight):
        self.dest = dest
        self.weight = weight
    
class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []

class GraphAdjList:
    def __init__(self):
        self.vertices = []
        
    def getIndex(self, name):
        
    def addVertex(self, name):
        self.vertices.append(Vertex(name))
        
    def addEdge(self, dest, source, weight):
        
        
    
        