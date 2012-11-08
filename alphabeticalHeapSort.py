#! /usr/bin/python
from heapq import *

class AlphabeticalHeapSort:
    def __init__(self, lst):
        self.lst = lst

    def sort(self):
        lst = self.lst
        
        heap = list(lst)
        heapify(heap)
        for i in range(len(lst)):
            lst[i] = heappop(heap)
        return lst
