# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 18:01:46 2019

@author: bdwoo
"""

class Node():
    #Constructor
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
        
    def __str__(self):
        return str(self.data)
    
    #accessor
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def getPrev(self):
        return self.prev
    
    #mutator
    def setData(self, data):
        self.data = data
    def setNext(self, next):
        self.next = next
    def setPrev(self, prev):
        self.prev = prev


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        cur = self.head
        out = 'List:\n'
        
        while (cur != None):
            out += str(cur.getData()) + '\n'
            cur = cur.getNext()
            
        return out
    
    def getHead(self):
        return self.head
    def setHead(self, head):
        self.head = Node(head)
        
    def getTail(self):
        return self.tail
    def setTail(self, tail):
        self.tail = tail
    
    def addFront(self, data):
        node = Node(data)
        node.setNext(self.head)
        self.setHead(node)
        
        if self.length == 1:
            self.setTail(self.node)
            
        
list = LinkedList()
list.addFront(6)
list.addFront(6)
list.setHead(6)
print(list)
