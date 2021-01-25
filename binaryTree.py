# -*- coding: utf-8 -*-
"""
Created on Fri May 15 17:54:55 2020

@author: bdwoo
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def __str__(self):
        return str(self.data)
    
    #accessors    
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def getData(self):
        return self.data
        
    #mutators
    def setLeft(self, left):
        self.left = left
    def setRight(self, right):
        self.right = right
    def setData(self, data):
        self.data = data

class BsTree:
    def __init__(self):
        self.root = None
        
    #Modified level order, insert None into queue as placeholder
    #Track number in row to know when to make a newline
    #If a row is all None, then it is the end of the tree
    #Still need number of levels to control spacing
    def __str__(self):
        q = []
        out = ''
        temp = ''
        n = 1   #Tracks how many to print on each level
        
        if self.root is not None:
            q.append(self.root)
            
        level = self.findLevels()
        
        while True:
            j = False #If a row is all None, then it is the end of the tree
            temp = '' #Temporary storage for this row. Used to avoid printing empty final row
            
            temp += ' '*level #Add spacing for each level
            
            for i in range(n):
                cur = q.pop(0)

                #Not a placeholder
                if cur is not None:
                    j = True    #Note this is not an empty row
                    
                    temp += str(cur.data) + ' '*(level)
                    
                    #Add children to queue
                    #We want None placeholders, so don't check for None
                    q.append(cur.left)
                    q.append(cur.right)
                                        
                else:
                    temp += ' ' + ' '*(level) #None is a placeholder, print a space
                    
                    #If this is None, add two None children as placeholders
                    q.append(None)
                    q.append(None)
                    
            temp += '\n'
            
            #If it is an empty row, we are at the end of the tree
            if j:
                out += temp
            else:
                break
            
            n*=2 #increase number of elements in row
            level-=1 #Decrement the level
        return out
        
    #Mutators
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insertR(self.root, data)
    def insertR(self, cur, data):
        if data < cur.data:
            if cur.left is None:
                cur.left = Node(data)
            else:
                self.insertR(cur.left, data)
        elif data > cur.data:
            if cur.right is None:
                cur.right = Node(data)
            else:
                self.insertR(cur.right, data)
     
    #Recursively search           
    #def delete(self, data):
        
        
    #Accessors
    def search(self, data):
        return self.__searchR(self.root, data)
    def __searchR(self, cur, data):
        if data < cur.data and cur.left is not None:
            self.__searchR(cur.left, data)
        elif data > cur.data and cur.right is not None:
            self.__searchR(cur.right, data)
        elif data == cur.data:
            return cur
    
    def levelOrder(self):
        q = []
        
        if self.root is not None:
            q.append(self.root)
        
        while len(q) > 0:
            cur = q.pop(0)
            
            if cur.left is not None:                
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
                
            print(str(cur.data))
    
    def preOrder(self):
        self.__preOrderR(self.root)
    def __preOrderR(self, cur):
        print(cur.data)
        if cur.left is not None:
            self.__preOrderR(cur.left)
        if cur.right is not None:
            self.__preOrderR(cur.right)
        
    def inOrder(self):
        self.__inOrderR(self.root)
    def __inOrderR(self, cur):        
        if cur.left is not None:
            self.__inOrderR(cur.left)
        print(cur.data)
        if cur.right is not None:
            self.__inOrderR(cur.right)
    
    def postOrder(self):
        self.__postOrderR(self.root)
    def __postOrderR(self, cur):        
        if cur.left is not None:
            self.__postOrderR(cur.left)
        if cur.right is not None:
            self.__postOrderR(cur.right)
        print(cur.data)
        
    def findLevels(self):
        if self.root is not None:
            return self.__findLevelsR(self.root, 1)
        else:
            return 0
    def __findLevelsR(self, cur, level):
        maxLevel = level
        if cur.left is not None:
            maxLevel = max(maxLevel, self.__findLevelsR(cur.left, level+1))
        if cur.right is not None:
            maxLevel = max(maxLevel, self.__findLevelsR(cur.right, level+1))
        return maxLevel
        
tree = BsTree()
tree.insert(5)
tree.insert(1)
tree.insert(0)
tree.insert(2)
tree.insert(7)
tree.insert(6)
tree.insert(8)
print(tree)
print(tree.findLevels())
print(tree.inOrder())
