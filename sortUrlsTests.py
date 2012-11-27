#! /usr/bin/env python
import unittest
import sortUrls
from sortfunctions.comparators import length
from urltools import validator, normalizer

class TestUrlsSorting(unittest.TestCase):

    #Setup for the tests, runs automatically before each test
    def setUp(self):
        #A list of urls to sort
        self.urls = ["www.google.com", "http://www.google.com", "a", "blarg@gmail.com", "facebook.com", "CS.WASHINGTON.EDU", "HTTPS://WWW.YAHOO.COM/"]
        #Expected output of validator
        self.validUrls = ["http://www.google.com", "HTTPS://WWW.YAHOO.COM/"]
        #Expected output of the sort-by-length functions
        self.sortedByLength = ["a", "facebook.com", "www.google.com", "blarg@gmail.com", "CS.WASHINGTON.EDU", "http://www.google.com", "HTTPS://WWW.YAHOO.COM/"]
        #Expected output of the sort-by-alphabetical functions
        self.sortedByAlphabetical = ["CS.WASHINGTON.EDU", "HTTPS://WWW.YAHOO.COM/", "a", "blarg@gmail.com", "facebook.com", "http://www.google.com", "www.google.com"]
        #Edge case where list is empty
        self.emptyUrls = []
        #Edge case where list has a single url
        self.singleUrl = ["google.com"]

    #Insertion Sort (by length) tests
    def test_insertionsort(self):
        sortedList = sortUrls.insertionsort(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByLength)

    def test_insertionsort_empty(self):
        sortedList = sortUrls.insertionsort(self.emptyUrls).sort()
        self.assertEquals(sortedList, self.emptyUrls)

    def test_insertionsort_single(self):
        sortedList = sortUrls.insertionsort(self.singleUrl).sort()
        self.assertEquals(sortedList, self.singleUrl)

    #Merge Sort (by length) tests
    def test_mergesort(self):
        sortedList = sortUrls.mergesort(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByLength)

    def test_mergesort_empty(self):
        sortedList = sortUrls.mergesort(self.emptyUrls).sort()
        self.assertEquals(sortedList, self.emptyUrls)

    def test_mergesort_single(self):
        sortedList = sortUrls.mergesort(self.singleUrl).sort()
        self.assertEquals(sortedList, self.singleUrl)

    #Quick Sort (by length) tests
    def test_quicksort(self):
        sortedList = sortUrls.quicksort(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByLength)

    def test_quicksort_empty(self):
        sortedList = sortUrls.quicksort(self.emptyUrls).sort()
        self.assertEquals(sortedList, self.emptyUrls)

    def test_quicksort_single(self):
        sortedList = sortUrls.quicksort(self.singleUrl).sort()
        self.assertEquals(sortedList, self.singleUrl)

    #Bucket Sort (by length) tests
    def test_bucketsort(self):
        sortedList = sortUrls.bucketsort(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByLength)

    def test_bucketsort_empty(self):
        sortedList = sortUrls.bucketsort(self.emptyUrls).sort()
        self.assertEquals(sortedList, self.emptyUrls)

    def test_bucketsort_single(self):
        sortedList = sortUrls.bucketsort(self.singleUrl).sort()
        self.assertEquals(sortedList, self.singleUrl)

    #Selection Sort (alphabetical) tests
    def test_selectionsort_alphabetical(self):
        sortedList = sortUrls.selectionsort_alphabetical(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByAlphabetical)

    def test_selectionsort_alphabetical_empty(self):
        sortedList = sortUrls.selectionsort_alphabetical(self.emptyUrls).sort()
        self.assertEquals(sortedList, self.emptyUrls)

    def test_selectionsort_alphabetical_single(self):
        sortedList = sortUrls.selectionsort_alphabetical(self.singleUrl).sort()
        self.assertEquals(sortedList, self.singleUrl)

    #Radix Sort (alphabetical) tests
    def test_radixsort_alphabetical(self):
        sortedList = sortUrls.radixsort_alphabetical(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByAlphabetical)

    def test_radixsort_alphabetical_empty(self):
        sortedList = sortUrls.radixsort_alphabetical(self.emptyUrls).sort()
        self.assertEquals(sortedList, self.emptyUrls)

    def test_radixsort_alphabetical_single(self):
        sortedList = sortUrls.radixsort_alphabetical(self.singleUrl).sort()
        self.assertEquals(sortedList, self.singleUrl)

    #Merge Sort (alphabetical) tests
    def test_mergesort_alphabetical(self):
        sortedList = sortUrls.mergesort_alphabetical(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByAlphabetical)

    def test_mergesort_alphabetical_empty(self):
        sortedList = sortUrls.mergesort_alphabetical(self.emptyUrls).sort()
        self.assertEquals(sortedList, self.emptyUrls)

    def test_mergesort_alphabetical_single(self):
        sortedList = sortUrls.mergesort_alphabetical(self.singleUrl).sort()
        self.assertEquals(sortedList, self.singleUrl)

    #Heap Sort (alphabetical) tests
    def test_heapsort_alphabetical(self):
        sortedList = sortUrls.heapsort_alphabetical(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByAlphabetical)

    def test_heapsort_alphabetical_empty(self):
        sortedList = sortUrls.heapsort_alphabetical(self.emptyUrls).sort()
        self.assertEquals(sortedList, self.emptyUrls)

    def test_heapsort_alphabetical_single(self):
        sortedList = sortUrls.heapsort_alphabetical(self.singleUrl).sort()
        self.assertEquals(sortedList, self.singleUrl)

    #Tests for our comparator by length function
    def test_comparator_length(self):
        res = length("asdfasdf", "asdf")
        self.assertEquals(res, 4)
        res = length("", "")
        self.assertEquals(res, 0)
        res = length("","asdf")
        self.assertEquals(res, -4)
        res = length("a", "")
        self.assertEquals(res, 1)
        res = length(".dfk1", "9)-.'")
        self.assertEquals(res, 0)
        res = length("a", "9358")
        self.assertEquals(res, -3)

    #########################################
    # URL Validation & Normalization Tests  #
    #########################################

    def test_append_slash(self):
        url = 'HTTP://WWW.fakeurl.COM/testdir'
        exp = 'http://www.fakeurl.com/testdir'
        self.assertEquals(normalizer._lowercase(url), exp)
        self.assertEquals(normalizer._lowercase(exp), exp)

    def test_capitalize_escapes(self):
        url = 'http://WWW.example.com/a%c2%b1b'
        exp = 'http://WWW.example.com/a%C2%B1b'
        self.assertEquals(normalizer._capitalize_escapes(url), exp)

    def test_remove_default_port(self):
        url = 'http://www.google.com:80/'
        exp = 'http://www.google.com/'
        self.assertEquals(normalizer._remove_default_port(url), exp)

    def test_add_trailing_slash(self):
        url1 = 'http://www.fakeurl.com/testfile.html'
        exp1 = url1
        url2 = 'http://www.fakeurl.com/testdir'
        exp2 = 'http://www.fakeurl.com/testdir/'
        self.assertEquals(normalizer._add_trailing_slash(url1), exp1)
        self.assertEquals(normalizer._add_trailing_slash(url2), exp2)

    def test_remove_dot_segments(self):
        url = 'http://www.testsite.com/dir1/dir2a/../dir2b/./file.txt'
        exp = 'http://www.testsite.com/dir1/dir2b/file.txt'
        self.assertEquals(normalizer._remove_dot_segments(url), exp)

    def test_remove_empty_querystring(self):
        url = 'http://www.google.com/?'
        exp = 'http://www.google.com/'
        self.assertEquals(normalizer._remove_empty_querystring(url), exp)

    def test_validator(self):
        res = validator.validate(self.urls)
        self.assertEquals(res, self.validUrls)

if __name__ == "__main__":
    unittest.main()
