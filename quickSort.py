#! /usr/bin/python
import random
from comparators import default_cmp

# Class Definition
class QuickSort:
    def __init__(self, list, cmp=default_cmp):
        self.list = list
        self.cmp = default_cmp

    def sort(self):
        """Sort a list of items using the given comparsion function.

        This method does not modify the input list.
        Note: Although quicksort has a worst-case running time of O(n^2),
        this occurs extremely rarely. In practice, quicksort is often
        faster than other O(nlogn) sorting algorithms.
        Average case running time: O(nlogn) , Worst case: O(n^2)
        """
        def qsort(list, cmp):
            if list == []:
                return list
            else:
                pivot_ndx = random.choice(range(len(list)))
                pivot = list.pop(pivot_ndx)
                left = [x for x in list if cmp(x, pivot) < 0]
                right = [x for x in list if cmp(x, pivot) >= 0]
                return qsort(left, cmp) + [pivot] + qsort(right, cmp)

        list = self.list
        cmp = self.cmp

        return qsort(list[:], cmp)
