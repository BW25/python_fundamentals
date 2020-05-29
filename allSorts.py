# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Python is designed for researchers
But it is slower
Power comes from libraries
Libraries are written in C, so they still have speed
\
Multi-line comments are executed as strings

** is power
// is integer division
Casting: int(5/3)
str is string
float
ord is converting char to int

Use single quotes for strings

No {} brackets in Python. EVER
Use : automatically indents to indicate brackets

    No arrays in python! Can import numpy if need them
    Use numpy for math with speed
Lists
Tuples
Dictionaries
"""
#insertion, selection, linear search, binary search, mergesort, quicksort, make an array from a list
#linked list, binary search tree, radix sort

#to import, just import filename
import random


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
    
    #Utilities
    def append(self, n):
        self.arr.append(int(n))
        self.length += 1
        
    def getAt(self, i):
        if i < self.length:
            return  self.arr[i]
        else:
            return None
    
    def setAt(self, i, val):
        if i < self.maxSize:
            self.arr[i] = val
            
    def getLength(self):
        return self.length
    
    def swap(self, i, j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp
            
    #Searches
    def linearSearch(self, x):
        for i in range(self.getLength()):
            if (self.arr[i] == x):
                return i
        return None
    
    def binarySearchHelper(self, x):
        return self.binarySearch(x, 0, self.length-1)
    def binarySearch(self, x, low, high):
        
        if low <= high:
            mid = int( low + (high - low)/2 )
            
            if self.arr[mid] == x:
                return mid
            
            elif x < self.arr[mid]:
                return self.binarySearch(x, low, mid-1)
            else:
                return self.binarySearch(x, mid+1, high)
        else:
            return None



    #Sorts
    def selectionSort(self):
        #Don't need to sort last item
        for i in range( len(self.arr)-1 ) :
            
            smallest=i
            for j in range(i, len(self.arr)) :
                if self.arr[j] < self.arr[smallest]:
                    smallest = j
            
            temp=self.arr[smallest]
            self.arr[smallest]=self.arr[i]
            self.arr[i]=temp
            
    def insertionSort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            
            j=i-1
            while self.arr[j] > key and j >= 0:
                self.arr[j+1] = self.arr[j]
                j -= 1
            self.arr[j+1] = key
        
    def mergeSortHelper(self):
        self.mergeSort(0, self.length-1)
    def mergeSort(self, low, high):
        if (low < high):
            mid = (high+low) // 2
            self.mergeSort(low, mid)
            self.mergeSort(mid+1, high)
            self.merge(low, mid, high);
    def merge(self, low, mid, high):
        len1 = mid - low + 1
        len2 = high - mid
        
        arrLow = []
        arrHigh = []
        for i in range(0, len1):
            arrLow.append(self.arr[low+i])
            
        for i in range(0, len2):
            arrHigh.append(self.arr[mid+1+i])
            
        i = 0
        j = 0
        k = low

        while(i < len1 and j < len2):
            #print(str(k) + " " + str(i) + " " + str(j))
            if (arrLow[i] <= arrHigh[j]):
                self.arr[k] = arrLow[i]
                i+=1
            else:
                self.arr[k] = arrHigh[j]
                j+=1
            k+=1
        
        while (i < len1):
            self.arr[k] = arrLow[i]
            i+=1
            k+=1
        
        while (j < len2):
            self.arr[k] = arrHigh[j]
            j+=1
            k+=1
            
    def quickSortHelper(self):
        self.quickSort(0, self.length-1)
    def quickSort(self, low, high):
        if (low<high):
            pivot = self.partition(low, high)
            
            self.quickSort(low, pivot-1)
            self.quickSort(pivot+1, high)
    def partition(self, low, high):
        #Choose random pivot
        a = random.randint(low, high)
        
        #Swap the pivot with the last item
        temp = self.arr[a]
        self.arr[a] = self.arr[high]
        self.arr[high] = temp

        pivot = self.arr[high]
        
        #Track the location of the next smallest item
        x = low - 1
        i = low
        for i in range(low, high):    #Stop before high so we don't move the pivot
            if (self.arr[i] <= pivot):
                x+=1
                self.swap(x, i)
        
        #Swap the pivot into place and return it
        temp = self.arr[x+1]
        self.arr[x+1] = self.arr[high]
        self.arr[high] = temp
        return x+1

    def toMinHeap(self):
        heap = []
        heap.append(0)
        for i in range(self.length):
            x = self.arr[i]
            heap.append(x)
            heap[0]+=1
            self.siftUpMin(heap)
        #Copy the heap back to the original array, minus the arr[0] with length
        for i in range(self.length):
            self.arr[i] = heap[i+1]
    def siftUpMin(self, heap):
        i = heap[0]
        while i > 1 and heap[i] < heap[i//2]:
            temp = heap[i]
            heap[i] = heap[i//2]
            heap[i//2] = temp
            i = i//2
    def minHeapSort(self):
        heapSize = self.length - 1
        for i in range (heapSize, 0, -1):
            #take first item off and swap it with the last
            #The decrementing from self.length shortens the length of the list
            temp = self.arr[i]
            self.arr[i] = self.arr[0]
            self.arr[0] = temp
            
            self.siftDownMin(0, i)
    def siftDownMin(self, i, heapSize):
        smallest = i
        left = i*2 + 1
        right = left + 1
        
        #Find largest item
        if (left < heapSize and self.arr[left] < self.arr[smallest]):
            smallest = left
        if (right < heapSize and self.arr[right] < self.arr[smallest]):
            smallest = right
        
        #If largest
        if (smallest != i):
            temp = self.arr[i]
            self.arr[i] = self.arr[smallest]
            self.arr[smallest] = temp

            self.siftDownMin(smallest, heapSize)
            
    def toMaxHeap(self):
        heap = []
        heap.append(0)
        for i in range(self.length):
            x = self.arr[i]
            heap.append(x)
            heap[0]+=1
            self.siftUpMax(heap)
        #Copy the heap back to the original array, minus the arr[0] with length
        for i in range(self.length):
            self.arr[i] = heap[i+1]
    def siftUpMax(self, heap):
        i = heap[0]
        while i > 1 and heap[i] > heap[i//2]:
            temp = heap[i]
            heap[i] = heap[i//2]
            heap[i//2] = temp
            i = i//2
    def maxHeapSort(self):
        heapSize = self.length - 1
        for i in range (heapSize, 0, -1):
            #take first item off and swap it with the last
            #The decrementing from self.length shortens the length of the list
            temp = self.arr[i]
            self.arr[i] = self.arr[0]
            self.arr[0] = temp
            
            self.siftDownMax(0, i)
    def siftDownMax(self, i, heapSize):
        largest = i
        left = i*2 + 1
        right = left + 1
        
        #Find largest item
        if (left < heapSize and self.arr[left] > self.arr[largest]):
            largest = left
        if (right < heapSize and self.arr[right] > self.arr[largest]):
            largest = right
        
        #If largest
        if (largest != i):
            temp = self.arr[i]
            self.arr[i] = self.arr[largest]
            self.arr[largest] = temp

            self.siftDownMax(largest, heapSize)
    def heapSort(self):
        self.toMaxHeap()
        numbers.maxHeapSort()
        
    def radixSort(self):
        
        
    
    
def getNums(numbers):
    a = input('Enter a number: ')
    while a.isdigit():
        numbers.append(a)
        a = input('Enter a number: ')
    
def getRandNums(numbers, x):
    for i in range(x):
        numbers.append(random.randint(0, 20))
        
def getTestNums(numbers):
    numbers.append(5)
    numbers.append(8)
    numbers.append(9)
    numbers.append(3)
    numbers.append(4)
    numbers.append(1)
    numbers.append(7)
    numbers.append(6)
    numbers.append(2)
    numbers.append(0)


numbers=arrayCollection(50)

getRandNums(numbers, 10)
print(numbers)
numbers.heapSort()
print(numbers)

