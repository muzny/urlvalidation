#! /usr/bin/python

class AlphabeticalSelectionSort:
    def __init__(self, lst):
        self.lst = lst

    def sort(self):
        lst = self.lst
        n = len(lst)
        for i in range(n):
            low = i
            for j in range(i + 1, n):
                if lst[j] < lst[low]:
                    low = j
            lst[i], lst[low] = lst[low], lst[i]
        return lst
