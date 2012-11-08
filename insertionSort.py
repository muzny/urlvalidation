#! /usr/bin/python
from comparators import default_cmp

# Class Definition
class InsertionSort:
    def __init__(self, list, cmp=default_cmp):
        self.list = list
        self.cmp = default_cmp

    def sort(self):
        list = self.list
        cmp = self.cmp

        for i in range(1, len(list)):
            save = list[i]
            j = i
            while j > 0 and cmp(list[j - 1], save) > 0:
                list[j] = list[j - 1]
                j -= 1
            list[j] = save
        return list
