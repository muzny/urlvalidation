#! /usr/bin/python

import sys
import random
import argparse
from heapq import *

"""
The following sorting algorithms are taken from the Bulletin group.
They sort based on the default comparator.

They correspond to the following numbers:
5 - selectionsort_alphabetical
6 - radixsort
7 - mergesort_alphabetical
8 - heapsort
"""
def selectionsort_alphabetical(lst):
    n = len(lst)
    for i in range(n):
        low = i
        for j in range(i + 1, n):
            if lst[j] < lst[low]:
                low = j
        lst[i], lst[low] = lst[low], lst[i]
    return lst

def getChar(url, digit_num):
    if digit_num >= len(url):
        return 0
    else:
        return ord(url[digit_num])

def makeBlanks(size):
    # create a list of empty lists to hold the split by digit
    return [ [] for i in range(size) ]

def split(a_list, base, digit_num):
    buckets = makeBlanks(base)
    for num in a_list:
        # append the number to the list selected by the digit
        buckets[getChar(num, digit_num)].append(num) # getDigit(num, base, digit_num)].append(num)
    return buckets

# concatenate the lists back in order for the next step
def merge_radix(a_list):
    new_list = []
    for sublist in a_list:
       new_list.extend(sublist)
    return new_list

def maxAbs(a_list):
    # largest abs value element of a list
    return max(abs(num) for num in a_list)

def radixsort(a_list): # , base):
    # there are as many passes as there are digits in the longest number
    # passes = int(log(maxAbs(a_list), base) + 1)
    try:
        passes = len(max(a_list, key=len))
        base = 256
        new_list = list(a_list)
        for digit_num in range(passes):
            new_list = merge_radix(split(new_list, base, passes - digit_num - 1))
        return new_list
    except ValueError:
        return []

def mergesort_alphabetical(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    return merge_alphabetical(mergesort_alphabetical(lst[:mid]), mergesort_alphabetical(lst[mid:]))

def merge_alphabetical(left, right):
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

def heapsort(lst):
    heap = list(lst)
    heapify(heap)
    for i in range(len(lst)):
        lst[i] = heappop(heap)
    return lst

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

    return qsort(list[:], cmp)

def insertionsort(list, cmp=default_cmp):
    for i in range(1, len(list)):
        save = list[i]
        j = i
        while j > 0 and cmp(list[j - 1], save) > 0:
            list[j] = list[j - 1]
            j -= 1
        list[j] = save
    return list

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
    algos = {1: insertionsort, 2: mergesort, 3: quicksort, 4: bucketsort,
             5: selectionsort_alphabetical, 6: radixsort, 7: mergesort_alphabetical,
             8: heapsort}

    parser = argparse.ArgumentParser(description="""Sorting Madness!
        Given an input file containing one url per line, prints the sorted list
        of urls to the output file. The desired sorting algorithm can be supplied using
        an integer, either as a command-line argument or as the first line of the
        input file. If both methods are used, the command-line argument wins. If no
        sorting algorithm is supplied, the default is quicksort. """)
    parser.add_argument('-i', '--input', help='the input file', required=True)
    parser.add_argument('-o', '--output', help='the output file', required=True)
    parser.add_argument('-s', '--sort', type=int, help='the sorting algorithm. \
                        Must be an integer. possible values are:\n' +
                        '\n'.join(['%d:%s' % (k, algos[k].__name__) for k in algos.keys()]) )
    args = parser.parse_args()

    outfile = None
    urls = None

    try:
        outfile = open(args.output, 'w')
    except IOError:
        print "Error: Unable to open output file \"%s\"." % args.output
        sys.exit()

    try:
        urls = open(args.input).readlines()
    except IOError:
        print "Error: File \"%s\" not found." % args.input
        sys.exit()

    sel = 3  # default selection is quicksort

    try:
        if len(urls) > 0:
            sel = int(urls[0]) # try getting the sorting alg from the file
            urls = urls[1:] # this line isn't executed if above failes
    except ValueError:
        pass

    if args.sort is not None: # command line always wins
        sel = args.sort

    outfile.write("".join(algos[sel](urls)))


# vim: set ai et ts=4 sw=4 sts=4 :
