#! /usr/bin/python
import sys

# Static Definition Methods
def default_cmp(a, b):
    return len(a) - len(b)

# Static Helper Methods
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

# Class Definition
class BucketSort:
    def __init__(self, list, cmp=default_cmp):
        self.list = list
        self.cmp = default_cmp

    def sort(self):
        list = self.list
        cmp = self.cmp

        '''
        Recursively performs bucket sort on the list
        of strings, using their lengths to index
        them.
        '''
        return self.bucketsort(self.list, self.cmp)

    def bucketsort(self, list, cmp):
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
                    bucket_list[i] = self.bucketsort(bucket_list[i], cmp)

        # Concatenate all of the sorted buckets
        ret_val = []
        for i in range(len(bucket_list)):
            ret_val += bucket_list[i]

        return ret_val
