# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 22:27:55 2019

@author: bdwoo


"""
import sys
import numpy as np

#Placeholder for additional features
class Vertex:
    def __init__(self, name):
        self.name = str(name)
        
    def __str__(self):
        return self.name
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = str(name)
        
#The MinHeapNode has to store its distance, and its index in the graph so we can edit its position
class MinHeapNode:
    def __init__(self, ind, dist):
        self.ind = ind
        self.dist = dist
        
class MinHeap:
    def __init__(self):
        self.heap = []
        self.length = 0 #We don't remove from the heap: just move to the back and shrink this length value
        self.pos = []  #Position array to allow O(1) lookup of a node
    def __str__(self):
        out = ''
        for data in self.heap:
            out += str(data.ind) + '-' + str(data.dist) + ' '
        return out
    
    def push(self, ind, dist):
        self.length += 1
        
        self.heap.append(MinHeapNode(ind, dist))
        self.pos.append(self.length-1) #Initial position is at the end of the heap
        
        #Unnecessary to siftUp. We will be adding inf, and a 0 initially. Add manually and siftUp as needed
        #self.siftUp(self.length-1)  #Give siftUp the vertex #
    
    #Update distance and siftUp
    def siftUp(self, index, dist):
        #Get ind of item
        heapInd = self.pos[index]
        
        #Update weight
        self.heap[heapInd].dist = dist
        #sift up
        while heapInd>0 and self.heap[heapInd].dist < self.heap[(heapInd-1)//2].dist:
            
            #Update positions. We use the graph position stored in the heap to get them
            self.pos[self.heap[heapInd].ind] = (heapInd-1)//2
            self.pos[self.heap[(heapInd-1)//2].ind] = heapInd
            
            #Swap nodes
            temp = self.heap[heapInd]
            self.heap[heapInd] = self.heap[(heapInd-1)//2]
            self.heap[(heapInd-1)//2] = temp
            heapInd = (heapInd-1)//2                        
        
    def pop(self):
        #Save head to return, then swap first and last and decrement length
        val = self.heap[0]
        
        last = self.length-1
        
        #Update positions. We use the graph position stored in the heap to get them
        self.pos[self.heap[0].ind] = last
        self.pos[self.heap[last].ind] = 0
        
        temp = self.heap[0]
        self.heap[0] = self.heap[last]
        self.heap[last] = temp
        self.length -= 1
        
        self.siftDown(0)
        return val
    
    def siftDown(self, i):
        min = i
        left = (i*2)+1
        right = left+1
        
        if left < self.length and self.heap[left].dist < self.heap[min].dist:
            min = left
        if right < self.length and self.heap[right].dist < self.heap[min].dist:
            min = right
        
        if min != i:
            #Update positions. We use the graph position stored in the heap to get them
            self.pos[self.heap[i].ind] = min
            self.pos[self.heap[min].ind] = i
            
            #Swap the smallest and current index
            temp = self.heap[min]
            self.heap[min] = self.heap[i]
            self.heap[i] = temp
            
            self.siftDown(min)
        

#adacency matrix
class Graph:
    def __init__(self, name):
        self.name = name
        self.adjMat = []
        self.vertexList = []
        self.tempVList = [] #Used to store if we have been to a vertex for some algorithms
        
    def __str__(self):
        out = str(self.name) + '\n'
        length = len(self.vertexList)
        
        out += '     '
        for i in range(length):
            out += str(self.vertexList[i]).ljust(4) + ' '
        out += '\n'
        
        for i in range (length):
            out += str(self.vertexList[i]).ljust(4) + ' '
            for j in range (length):
                temp = self.adjMat[i][j]
                if temp == sys.maxsize:
                    out += u"\u221E".ljust(4) + ' ' 
                else: 
                    out += str(self.adjMat[i][j]).ljust(4) + ' '
            out += '\n'
            
        out += '\nAdjacency list:\n'
        
        for i in range(length):
            out += str(self.vertexList[i])
            
            for j in range(length):
                #Don't print edges between a vertex and itself
                if i != j:   
                    if self.adjMat[j][i] != sys.maxsize and self.adjMat[i][j] != sys.maxsize:
                        out += ' <-> ' + str(self.vertexList[j])
                    elif self.adjMat[j][i] != sys.maxsize:
                        out += ' <-  ' + str(self.vertexList[j])
                    elif self.adjMat[i][j] != sys.maxsize:
                        out += '  -> ' + str(self.vertexList[j])
            out += '\n'
        
        return out
    
    #Vertex and edge management
    def addVertex(self, name):

        #Check if a vertex with that name already exists
        if name not in self.vertexList: 
            #Add the vertex to the list
            self.vertexList.append(name)
            self.tempVList.append(0)
            
            #get new length
            length = len(self.vertexList)
            
            #Add a new column to the adjacency matrix
            list = []
            self.adjMat.append(list)
            
            #fill in the new column in the matrix with zeros
            for i in range(length):
                self.adjMat[length-1].append(sys.maxsize)
                
            #add a new row to the end of the matrix
            for i in range(len(self.vertexList)):
                self.adjMat[i].append(sys.maxsize)
                
            #Set the matrix so the the vertex can reach itself
            self.adjMat[length-1][length-1] = 0
            
    def addEdge(self, name1, name2, weight):
        vertex1 = self.findVertex(name1)
            
        if vertex1 != None:
            vertex2 = self.findVertex(name2)
            
            if vertex2 != None:
                self.adjMat[vertex1][vertex2] = weight
            else:
                print('Cannot add edge: Vertex ' + str(name1) + ' not found')
        else:
            print('Cannot add edge: Vertex ' + str(name2) + ' not found')
                
    def add2WayEdge(self, name1, name2, weight):
        self.addEdge(name1, name2, weight)
        self.addEdge(name2, name1, weight)
        
    def removeEdge(self, name1, name2):
        #A vertex can always reach itself. Do not remove an edge between a node and itself
        if name1 != name2:
            vertex1 = self.findVertex(name1)
            
            if vertex1 != None:
                vertex2 = self.findVertex(name2)
                
                if vertex2 != None:
                    self.adjMat[vertex1][vertex2] = sys.maxsize
                else:
                    print('Cannot remove edge: Vertex ' + str(name1) + ' not found')
            else:
                print('Cannot remove edge: Vertex ' + str(name2) + ' not found')
                
    def remove2WayEdge(self, name1, name2):
        self.removeEdge(name1, name2)
        self.removeEdge(name2, name1)
        
    #Utilities
    def loadGraph(self, filename):
        file = open(str(filename), 'r')
        
        #Get graph name
        line = file.readline()
        print('Name: ' + line)
        self.setName(line)

        #Get vertices
        line = file.readline()
        vertices = line.split()
        
        #Add vertices
        for i in vertices:
            self.addVertex(i)
           
        numEdges = int(file.readline())
        for i in range(numEdges):
            line = file.readline()
            edge = line.split()
            if (len(edge) == 3):
                v1 = Vertex(str(edge[0]))
                v2 = Vertex(str(edge[1]))
                self.addEdge(v1, v2, edge[2])      
        
        file.close()

    def findVertex(self, name):
        for i in range(len(self.vertexList)):
            if str(name) == str(self.vertexList[i]):
                return i
        return None
        
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
        
    #Searches
    def bfs(self, start):   #Breadth first search
        #Find initial vertex
        index = self.findVertex(start)
        
        #If vertex exists
        if (index != None):
            print('Breadth first Search: ')
            
            #Initialize visited array to all false, no locations visited yet
            length = len(self.vertexList)
            for i in range(length):
                self.tempVList[i] = False
                
            #Create a queue and add the index of the first vertex
            queue = []
            queue.append(index)
            self.tempVList[index] = True
            
            #While queue is not empty
            while queue:
                
                #Pop the visited vertex off the queue and print it
                cur = queue.pop(0)
                print(self.vertexList[cur])
                
                #Check adjacency list for vertices connected to the current one
                for j in range(length):
                    #If vertex has not already been visited
                    if self.tempVList[j] != True:
                        #If vertex is connected / is not unreachable (∞)
                        if self.adjMat[cur][j] != sys.maxsize:
                            #Add it to the queue and mark it as visited
                            queue.append(j)
                            self.tempVList[j] = True
            print()
        else:
            print('Vertex not found')
                
    #Breadth first search from a starting vertex to an ending vertex
    def bfsSE(self, start, end):   #Breadth first search
        #Find initial vertex
        index = self.findVertex(start)
        
        #If vertex exists
        if (index != None):
            print('Breadth first Search: ')
            
            #Initialize visited array to all false, no locations visited yet
            length = len(self.vertexList)
            for i in range(length):
                self.tempVList[i] = False
                
            #Create a queue and add the index of the first vertex
            queue = []
            queue.append(index)
            self.tempVList[index] = True
            
            #While queue is not empty
            while queue:
                
                #Pop the visited vertex off the queue and print it
                cur = queue.pop(0)
                print(self.vertexList[cur])
                
                if self.vertexList[cur] == end: #End if we are at the end node
                    print()
                    return
                else:
                    #Check adjacency list for vertices connected to the current one
                    for j in range(length):
                        #If vertex has not already been visited
                        if self.tempVList[j] != True:
                            #If vertex is connected / is not unreachable (∞)
                            if self.adjMat[cur][j] != sys.maxsize:
                                #Add it to the queue and mark it as visited
                                queue.append(j)
                                self.tempVList[j] = True
            print()
        else:
            print('Vertex not found')
            
    def dfs(self, start):
        #Find initial vertex
        index = self.findVertex(start)
        
        #If vertex exists
        if (index != None):
            print('Breadth first Search: ')
            
            #Initialize visited array
            for i in range(len(self.vertexList)):
                self.tempVList[i] = False
                
            self.tempVList[index] = True
            self.dfsRecursive(index)
            
            print()
        else:
            print('Vertex not found')
        
    def dfsRecursive(self, cur):
        print(self.vertexList[cur])
        for i in range(len(self.vertexList)):
            if self.tempVList[i] != True:
                if self.adjMat[cur][i] != sys.maxsize:
                    self.tempVList[i] = True
                    self.dfsRecursive(i)
                    
    def dfsSE(self, start, end):
        #Find initial vertex
        startIndex = self.findVertex(start)
        endIndex = self.findVertex(end)
        
        #If vertex exists
        if (startIndex != None):
            print('Breadth first Search: ')
            
            #Initialize visited array
            for i in range(len(self.vertexList)):
                self.tempVList[i] = False
                
            self.tempVList[startIndex] = True
            self.dfsSERecursive(startIndex, endIndex)
            
            print()
        else:
            print('Vertex not found')
        
    def dfsSERecursive(self, cur, end):
        print(self.vertexList[cur])
        
        #Only proceed if we have not reached the end goal. Otherwise, do nothing and return
        if (cur != end):
            for i in range(len(self.vertexList)):
                if self.tempVList[i] != True:
                    if self.adjMat[cur][i] != sys.maxsize:
                        self.tempVList[i] = True
                        if self.dfsSERecursive(i, end) == 0:
                            return 0    #Return 0 to indicate we have reached the end
        else:
            return 0    #Return 0 to indicate we have reached the end
        
    def topSort(self):
        print('Topological Sort: ')
        
        stack = []
        
        #Initialize visited array
        for i in range(len(self.vertexList)):
            self.tempVList[i] = False
               
        #Start at the first vertex, check all of the unvisited ones
        for i in range(len(self.vertexList)):
            if self.tempVList != True:
                stack = self.topSortRecursive(i, stack)
                stack.append(i)
        #print stack
        for i in range(len(self.vertexList)):
            print(self.vertexList[stack.pop()])
        
    def topSortRecursive(self, cur, stack):
        #Mark cur as visited
        self.tempVList[cur] = True
        
        for i in range(len(self.vertexList)):
            #If not visited
            if self.tempVList[i] != True:
                #If there is an edge
                if self.adjMat[cur][i] != sys.maxsize:
                    stack = self.topSortRecursive(i, stack)
                    stack.append(i)
        return stack
    
    def bellmanFordCheck(self, start):
        ind = self.findVertex(start)
        if ind != None:
            print('Bellman-Ford shortest path')
            
            #Initialize distances
            for i in range(len(self.tempVList)):
                self.tempVList[i] = sys.maxsize
            self.tempVList[ind] = 0
            
            for i in range(len(self.tempVList)):
                #Update all edges. Loop through the vertices
                for j in range(len(self.tempVList)):
                    #Don't bother checking vertices with infinite distance: can't update edges yet
                    if (self.tempVList[j] != sys.maxsize):
                        #Loop through looking for edges
                        for k in range(len(self.tempVList)):
                            #Relax
                            val = self.tempVList[j] + int(self.adjMat[j][k])
                            if val < self.tempVList[k]:
                                self.tempVList[k] = val
            #Any edges reduced after this are in a negative edge cycle
            for j in range(len(self.tempVList)):
                #Don't bother checking vertices with infinite distance: can't update edges yet
                if (self.tempVList[j] != sys.maxsize):
                    #Loop through looking for edges
                    for k in range(len(self.tempVList)):
                        #Relax
                        val = self.tempVList[j] + int(self.adjMat[j][k])
                        if val < self.tempVList[k]:
                            print('Negative cycle exists')
                            return True
            print('No negative cycle found')
            return False

                
        else:
            print('Starting vertex does not exist')
    def bellmanFord(self, start):
        ind = self.findVertex(start)
        if ind != None:
            print('Bellman-Ford shortest path')
            
            #Initialize distances
            for i in range(len(self.tempVList)):
                self.tempVList[i] = sys.maxsize
            self.tempVList[ind] = 0
            
            for i in range(len(self.tempVList)):
                #Update all edges. Loop through the vertices
                for j in range(len(self.tempVList)):
                    #Don't bother checking vertices with infinite distance: can't update edges yet
                    if (self.tempVList[j] != sys.maxsize):
                        #Loop through looking for edges
                        for k in range(len(self.tempVList)):
                            #Relax
                            val = self.tempVList[j] + int(self.adjMat[j][k])
                            if val < self.tempVList[k]:
                                self.tempVList[k] = val
                                
            #Any edges reduced after this are in a negative edge cycle
            for j in range(len(self.tempVList)):
                #Don't bother checking vertices with infinite distance: can't update edges yet
                if (self.tempVList[j] != sys.maxsize):
                    #Loop through looking for edges
                    for k in range(len(self.tempVList)):
                        #Since we are working with -ve infinity, -inf + sys.maxsize will trigger relaxing
                        #This means it could add a -ve edge where there is no edge
                        #This extra check is necessary to prevent that
                        if int(self.adjMat[j][k] != sys.maxsize):
                            #Relax
                            val = self.tempVList[j] + int(self.adjMat[j][k])
                            if val < self.tempVList[k]:
                                self.tempVList[k] = float('-inf')
                            
            #print spt
            for i in range(len(self.tempVList)):
                print(self.tempVList[i])
    
        else:
            print('Starting vertex does not exist')
            
    #TODO: Modify minHeap to store position in minHeap
    #Update distances using this, and siftUp on this node
    #Don't discard from the minHeap: Shrink length. Lets us check if is in heap(visited) by if pos is > heap.length
    #Use np.array for speed instead of list
    def djikstra(self, name):
        ind = self.findVertex(name)
        if (ind != None):
            #Set up min heap as priority queue
            heap = MinHeap()
            for i in range(len(self.vertexList)):
                heap.push(i, float('inf'))
            heap.siftUp(ind, 0)
            
            #Tracking distances is redundant since they are stored in the heap
            while heap.length > 0:
                heapNode = heap.pop()                
                #Check neighbours
                for i in range(len(self.tempVList)):
                    #If is unvisited edge
                    if heap.pos[heapNode.ind] >= heap.length and self.adjMat[heapNode.ind][i] != sys.maxsize:
                        newDist = heapNode.dist + int(self.adjMat[heapNode.ind][i])
                        if newDist < heap.heap[heap.pos[i]].dist:
                            heap.siftUp(i, newDist)                
            #Print results from heap. Will be sorted by weight largest->smallest
            for heapNode in heap.heap:
                print(str(self.vertexList[heapNode.ind]) + ' ' + str(heapNode.dist))
            
        else:
            print('Vertex does not exist')


graph = Graph('test graph')
graph.loadGraph('djikstra_graph.txt')
print(graph)
graph.djikstra('s')
