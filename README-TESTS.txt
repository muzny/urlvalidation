########################################################################
To run tests navigate to the directory where sortUrlsTests.py is located and type:
python sortUrlsTests.py

It will run 25 tests and report success or failure of the tests
########################################################################
Test Design:

The tests were designed around a few certain areas of interest.  

For each sort it is given a list of urls to sort, an empty list, and a list with a single url to sort.
The first 4 sorts sort by length (they take a comparator and we give it our length comparator), so they use self.sortedByLength to check the answer
The last 4 sorts sort alphabetically so they use self.sortedByAlphabetical to check the answer

To test the length comparator I tested the following cases (a and b refer to lengths of the strings passed as parameters):
a=b
a>b
a<b
a=0, b=0
a=0, b>0
a>0, b=0
#########################################################################
