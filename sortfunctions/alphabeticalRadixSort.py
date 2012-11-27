
# Static Helper Methods
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

def merge_radix(a_list):
    new_list = []
    for sublist in a_list:
       new_list.extend(sublist)
    return new_list

# Class Definition
class AlphabeticalRadixSort:
    def __init__(self, a_list):
        self.a_list = a_list

    def sort(self):
        a_list = self.a_list
        try:
            passes = len(max(a_list, key=len))
            base = 256
            new_list = list(a_list)
            for digit_num in range(passes):
                new_list = merge_radix(split(new_list, base, passes - digit_num - 1))
            return new_list
        except ValueError:
            return []
