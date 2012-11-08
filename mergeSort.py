#! /usr/bin/python
from comparators import length

# Static Helper Methods
def merge(left, right, cmp):
    result = []
    while (len(left) > 0 or len(right) > 0):
        # both non empty
        if (len(left) > 0 and len(right) > 0):
            c = cmp(left[0], right[0])
            if (c <= 0):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        # right is empty
        elif (len(left) > 0):
            result.append(left.pop(0))
        # left is empty
        else:
            result.append(right.pop(0))
    return result

# Class Definition
class MergeSort:
    def __init__(self, list, cmp=length):
        self.list = list
        self.cmp = cmp

    def sort(self):
        return self.sort_helper(self.list, self.cmp)

    def sort_helper(self, list, cmp):
        size = len(list)
        if (size <= 1):
            return list
        left = self.sort_helper(list[0 : size/2], cmp)
        right = self.sort_helper(list[size/2 : size], cmp)
        return merge(left, right, cmp)
