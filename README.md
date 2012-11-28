Url Validation
==============

To run the program:

    $ python sortUrls.py [options]

If you do either of the following:
    
    $ python sortUrls.py -h
    $ python sortUrls.py --help

you will see a verbose explaination of the command line arguments. Here is that output:

    usage: sortUrls.py [-h] -i INPUT -o OUTPUT [-s {1,2,3,4,5,6,7,8}]
                   [-k {valid,invalid,None}]

    Sorting Madness! Given an input file containing one url per line, prints the
    sorted list of urls to the output file. The desired sorting algorithm can be
    supplied as a command-line argument. The default is quicksort. You may also
    specify if you wish to only sort valid or invalid urls. Note: If one of the
    validation options is chosen, all output urls will be normalized.

    optional arguments:
        -h, --help            show this help message and exit
        -i INPUT, --input INPUT
                            the input file
        -o OUTPUT, --output OUTPUT
                            the output file
        -s {1,2,3,4,5,6,7,8}, --sort {1,2,3,4,5,6,7,8}
                        the sorting algorithm. Must be an integer. possible
                        values are: 1:insertionsort 2:mergesort 3:quicksort
                        4:bucketsort 5:selectionsort_alphabetical
                        6:radixsort_alphabetical 7:mergesort_alphabetical
                        8:heapsort_alphabetical
        -k {valid,invalid,None}, --kind {valid,invalid,None}
                        kind of urls to sort
    
    

