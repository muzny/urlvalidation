import unittest
import sortUrls
from comparators import length

class TestUrlsSorting(unittest.TestCase):

    def setUp(self):
        self.urls = ["www.google.com", "http://www.google.com", "a", "blarg@gmail.com", "facebook.com", "CS.WASHINGTON.EDU", "HTTPS://WWW.YAHOO.COM/"]
        self.sortedByLength = ["a", "facebook.com", "www.google.com", "blarg@gmail.com", "CS.WASHINGTON.EDU", "http://www.google.com", "HTTPS://WWW.YAHOO.COM/"]
        self.sortedByAlphabetical = ["CS.WASHINGTON.EDU", "HTTPS://WWW.YAHOO.COM/", "a", "blarg@gmail.com", "facebook.com", "http://www.google.com", "www.google.com"]

    def test_insertionsort(self):
        sortedList = sortUrls.insertionsort(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByLength)
    
    def test_mergesort(self):
        sortedList = sortUrls.mergesort(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByLength)
        
    def test_quicksort(self):
        sortedList = sortUrls.quicksort(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByLength)
    
    def test_bucketsort(self):
        sortedList = sortUrls.bucketsort(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByLength)
        
    def test_selectionsort_alphabetical(self):
        sortedList = sortUrls.selectionsort_alphabetical(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByAlphabetical)
    
    def test_radixsort_alphabetical(self):
        sortedList = sortUrls.radixsort_alphabetical(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByAlphabetical)
        
    def test_mergesort_alphabetical(self):
        sortedList = sortUrls.mergesort_alphabetical(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByAlphabetical)
    
    def test_heapsort_alphabetical(self):
        sortedList = sortUrls.heapsort_alphabetical(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByAlphabetical)
    
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
    
if __name__ == "__main__":
    unittest.main()