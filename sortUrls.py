#! /usr/bin/python

import sys
import random

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
    return qsort(list[:], cmp)

def qsort(list, cmp):
    if list == []:
        return list
    else:
        pivot_ndx = random.choice(range(len(list)))
        pivot = list.pop(pivot_ndx)
        left = [x for x in list if cmp(x, pivot) < 0]
        right = [x for x in list if cmp(x, pivot) >= 0]
        return qsort(left, cmp) + [pivot] + qsort(right, cmp)

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

def msvalue(n):
    '''
    Returns the most significant value of n, i.e. n rounded
    down to the nearest significant digit.

    So msvalue(1)   -> 1
       msvalue(25)  -> 10
       msvalue(987) -> 100
    '''
    if n < 10:
        return 1
    else:
        return 10 * msvalue(n / 10)

def bucketsort(list, cmp=default_cmp):
    '''
    Recursively performs bucket sort on the list
    of strings, using their lengths to index
    them.
    '''

    # Pre-parse the length of each string in the list
    # so that we can find the min and max with which to set
    # up the buckets.
    len_list = []
    max_val = 0
    min_val = sys.maxint
    for i in range(len(list)):
        length = len(list[i])
        len_list.append((length, list[i])) # store list item as tuple (length, item)
        if length > max_val:
            max_val = length
        if length < min_val:
            min_val = length

    # Range of values that each bucket holds.
    bucket_size = msvalue(max_val - min_val)

    # Set up the empty buckets.
    num_buckets = (max_val / bucket_size) - (min_val / bucket_size)
    bucket_list = []
    for i in range(num_buckets + 1):
        bucket_list.append([])

    # Index the list elements into their respective buckets.
    n = len(list)
    for i in range(n):
        # Items are indexed by rounding down to the nearest bucket.
        index = (len_list[i][0] / bucket_size) - (min_val / bucket_size)

        bucket_list[index].append(len_list[i][1])

    # Sort the buckets. If all elements indexed
    # to the same bucket, use another sorting
    # algorithm to perform the final sort on
    # that bucket.
    for i in range(len(bucket_list)):
        if len(bucket_list[i]) > 0:
            if len(bucket_list[i]) == len(list):
                bucket_list[i] = insertionsort(bucket_list[i], cmp)
            else:
                bucket_list[i] = bucketsort(bucket_list[i])

    # Concatenate all of the sorted buckets
    ret_val = []
    for i in range(len(bucket_list)):
        ret_val += bucket_list[i]

    return ret_val

"""
Main

Parse command line arguments and execute sort functions.
"""
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./sortUrls.py <input file> <output file (opt)>")
        sys.exit()

    outfile = None
    if len(sys.argv) == 3:
        outfile = open(sys.argv[2], 'w')
    else:
        outfile = sys.stdout

    algos = {1: insertionsort, 2: mergesort, 3: quicksort, 4: bucketsort}

    lines = open(sys.argv[1]).readlines()
    urls = lines[1:]

    sel = int(lines[0])
    outfile.write("".join(algos[sel](urls)))


# vim: set ai et ts=4 sw=4 sts=4 :
