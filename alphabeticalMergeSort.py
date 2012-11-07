#! /usr/bin/python

# Static Helper Methods
def merge(left, right):
    merged = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    return merged + left[l:] + right[r:]

# Class Definition
class AlphabeticalMergeSort:
    def __init__(self, lst):
        self.lst = lst

    def sort(self):
        return self.mergesort(self.lst)

    def mergesort(self, lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        return merge(self.mergesort(lst[:mid]),
                     self.mergesort(lst[mid:]))
