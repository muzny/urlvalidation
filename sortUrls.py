#! /usr/bin/python

import sys
import argparse

def insertionsort(*args):
    import insertionSort
    return insertionSort.InsertionSort(*args)

def mergesort(*args):
    import mergeSort
    return mergeSort.MergeSort(*args)

def quicksort(*args):
    import quickSort
    return quickSort.QuickSort(*args)

def bucketsort(*args):
    import bucketSort
    return bucketSort.BucketSort(*args)

def selectionsort_alphabetical(*args):
    import alphabeticalSelectionSort
    return alphabeticalSelectionSort.AlphabeticalSelectionSort(*args)

def radixsort_alphabetical(*args):
    import alphabeticalRadixSort
    return alphabeticalRadixSort.AlphabeticalRadixSort(*args)

def mergesort_alphabetical(*args):
    import alphabeticalMergeSort
    return alphabeticalMergeSort.AlphabeticalMergeSort(*args)

def heapsort_alphabetical(*args):
    import alphabeticalHeapSort
    return alphabeticalHeapSort.AlphabeticalHeapSort(*args)


"""
Main

Parse command line arguments and execute sort functions.
"""
if __name__ == "__main__":
    algos = {1: insertionsort, 2: mergesort, 3: quicksort, 4: bucketsort,
             5: selectionsort_alphabetical, 6: radixsort_alphabetical, 
             7: mergesort_alphabetical, 8: heapsort_alphabetical}

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

    sorter = algos[sel](urls)
    sortedList = sorter.sort()
    outfile.write("".join(sortedList))


# vim: set ai et ts=4 sw=4 sts=4 :
