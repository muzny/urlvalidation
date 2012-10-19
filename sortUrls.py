#! /usr/bin/python

import sys

# default to sort by length
def default_cmp(a, b):
    return len(a) - len(b)

def quicksort(list, cmp=default_cmp):
    # test
    list.sort(cmp)
    return(list)

def insertionsort(list, cmp=default_cmp):
    pass

def mergesort(list, cmp=default_cmp):
    pass

def bucketsort(list, cmp=default_cmp):
    pass

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
