# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:02:47 2019

@author: bdwoo
"""

class arrayCollection():
    def __init__(self, ms):
        self.maxSize = ms
        self.arr = []
        self.length = 0
        
    def __str__(self):
        s='Array: \n'
        
        for i in range(self.length):
            s+=str(self.arr[i]) + '\n'
        
        return s
    
    def append(self, n):
        self.arr.append(n)
        self.length += 1
        
    def getAt(self, i):
        if i < self.length:
            return  self.arr[i]
        else:
            return None
    
    def setAt(self, i, val):
        if i < self.maxSize:
            self.arr[i] = val
            


ac = arrayCollection(10)
ac.append(5)
ac.append(3)
print(ac.getAt(0))
print(ac.getAt(4))
print(ac)
    