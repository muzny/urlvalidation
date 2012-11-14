Our project was to take a file of URLs and sort them, using four different sorting algorithms.  These algorithms needed to have efficiency of O(n^2), O(n), and two at O(n log n).


We decided that our sorting metric was going to be the length of the URL.  While sorting URLs by length is not particularly useful in many cases (except possibly finding those that are more likely to be shortened aliases or higher-level domains), we wanted the same sorting metric to be applied to all algorithms, and that the metric would allow us to implement bucket sort without using a tremendous amount of time and memory (since we don't expect the length of URLs to be very long).  In order to keep bucket sort within the runtime constraint as well as remain consistent across all our sorting implementations, we do not explicitly handle ties when comparing URLs of the same length.

Given this metric we came up with the following searches.
* Insertion Sort - O(n^2)
* Merge Sort - O(n log n)
* Quick Sort - O(n log n)**
* Bucket Sort - O(n)***

** While the worst-case performance of quick sort is O(n^2), it is expected to run in O(n log n) on average, given that an average dataset is varied enough such that partitioning based on a randomly chosen pivot results in nearly equally sized partitions on each level of recursion.

** Similar to the previous note, the worst-case performance of bucket sort is O(n^2) rather than O(n).  However, we expect bucket sort to perform in O(n + b) on average, where b is the total number of buckets, assuming that the average input is relatively random such that there aren't many collisions in which URLs of different lengths get mapped to the same bucket, in which case the bucket itself would also need to be sorted.  Bucket sort appeared to be the next-best choice since it is possible to achieve O(n) performance if b is also in O(n).

The intended usage of our file is "sortUrls.py -i <input file> -o <output file> [-s <sorting algorithm>]".  
The program requires that you specify an input file consisting of a line-delimited list of URLs to sort, and an output file to which to write the sorted results.  The location of the output file will be determined by 
In addition, you may also optionally specify the sorting algorithm to use.  Otherwise, the sorting algorithm defaults to quick sort based on length (3).  The argument accepts integers corresponding to the following algorithms and orderings:

Sorting by length -
* 1: Insertion Sort
* 2: Merge Sort
* 3: Quick Sort
* 4: Bucket Sort

Sorting by alphabetical order.  These implementations originate from [https://github.com/caylan/403Section] and are unaltered -
* 5: Selection Sort
* 6: Radix Sort
* 7: Merge Sort
* 8: Heap Sort

Since our team has seven people, we divided the jobs for this assignment into seven tasks.
* Implementing Insertion Sort
* Implementing Merge Sort
* Implementing Quick Sort
* Implementing Bucket Sort
* Writing All Input/Output Related Functionality
* Creating the Test Suite
* Writing the Summary Paper

##URL Validation
### High Level Specification
You can optionally specify which types of urls to sort: valid, invalid, or all urls. NB: If a 'valid' or 'invalid' is chosen, then all output urls will be normalized.
To specify which urls to sort, simply use the command line option -k or --kind and then 'valid', 'invalid', or 'None'

It is important to note:   
If 'valid' or 'invalid' is chosen, URLs will be normalized, then sorted and written out to file according to their normalized form (while it may be unintuitive to see, in the output, that the input is mutated, it makes our normalization method more transparent). If a URL is not normalized ('None'), it will be sorted and output according to its original form.

### Definition of a Valid Form
A string is considered a valid URL if it matches the following regular expression: [Django source code](https://github.com/django/django/blob/stable/1.3.x/django/core/validators.py#L45).

To validate our URLs we decided to use the same validation regex used by the Django project. We copied the regex over
to our validation module instead of adding a Django dependency for such a small piece of functionality.
We chose this regex because it has been tested and implemented in a mature web framework. It should be more than
adequate for our needs.

Valid URLs
* begin with `http|https|ftp|ftps` followed by `://`
    - The regex does not allow username/passwords typically used in the `ftp` and `ftps` schemes (e.g. `ftp://username@ftp.example.org` is not valid) 
* followed by a domain, or `localhost`, or an ip address
    - IP addresses are not checked for validity (e.g. `http://999.999.999.999` is a valid IPv4 address)
* followed by an port, eg `:80` (optional)
    - Port numbers are not checked for validity (i.e. may be out of range; greater than 2^16)
* followed by a valid path (optional)
* followed by a query string and/or fragment (optional)
For more specific information about specific number and types of characters allowed in each component,
see the URL regex in `urltools/validator.py`

### Canonical Form
Before validation, the following normalizations are performed (The first three are guaranteed to preserve semantics):
* convert scheme and host to lowercase
* capitalize letters in escape sequences
* remove the default port
* add trailing slash
* remove dot segments
* remove empty query string

### Canonicalizer
After performing any necessary validation, URLs that are returned as valid through the validator are canonicalized through a normalizer module. This module contains methods that implement each component of our definition of the canonicalized form. These normalization methods are executed in fixed order. The normalizer returns only the normalized form of the URL, so there is no mapping with its original form.

### Comparators
Based on our command line sorting options, we define two different comparators on URLs as strings:   
* Order by length, ascending
* Order alphabetically   

### Task Division
We divided the url sorting exercise into the following tasks:
* Command-line option for url validation
* Normalization methods
* URL validation
* Summary paper & documentation
* Additional unit tests

