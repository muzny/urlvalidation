#! /usr/bin/python

import sys

"""
Comparison functions

Arguments:
    a - first element to compare
    b - second element to compare
Returns:
    negative integer if the first precedes the second
    0 if both arguments have equal ordering
    positive integer if the first succeeds the second
"""

# default to sort by length
def default_cmp(a, b):
    return len(a) - len(b)

"""
Sorting functions

Arguments:
    list - list of elements (url strings)
    cmp  - comparison function
Returns:
    sorted list of elements
"""

def quicksort(list, cmp=default_cmp):
    # test
    list.sort(cmp)
    return(list)

def insertionsort(list, cmp=default_cmp):
    pass

def mergesort(list, cmp=default_cmp):
    size = len(list)
    if (size <= 1):
        return list
    left = mergesort(list[0 : size/2], cmp)
    right = mergesort(list[size/2 : size], cmp)
    return merge(left, right, cmp)

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

def bucketsort(list, cmp=default_cmp):
    pass

"""
Main

Parse command line arguments and execute sort functions.
"""
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Incorrect usage. Please specify an input & output file.")
        sys.exit()

    algos = {1: insertionsort, 2: mergesort, 3: quicksort, 4: bucketsort}

    lines = open(sys.argv[1]).readlines()
    urls = lines[1:]

    sel = int(lines[0])
    output = open(sys.argv[2], 'w')
    output.write("".join(algos[sel](urls)))


# vim: set ai et ts=4 sw=4 sts=4 :
