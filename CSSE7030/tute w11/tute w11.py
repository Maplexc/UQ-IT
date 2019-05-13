def add(listy):
    if listy==[]:
        # base case
        return 0
    else:
        # recursive asee
        return listy[0] + add(listy[1:])

##add([1,2,3,4])
##
##    1 + add([2,3,4])
##
##        + 2 + add([3,4])
##
##            + 3 + add([4])
##
##                + 4 + add([])
##
##                    + 0


def minimum(listy):
    if listy == []:
        raise ValueError('Empty list')

    if len(listy) == 1:
        return listy[0]
        # base case

    else:
        # recursive case
        if listy[0] <= minimum(listy[1:]):
            return listy[0]
        else:
            return minimum(listy[1:])
##    alternative:
##        if listy[0] > listy[1]:
##            return minimum(listy[1:])
##        else:
##            return minimum([listy[0] + listy[2:])
##
##    minimum([3,4,2,5])
##
##    minimum([3,2,5])
##
##    minimum([2,5])
##
##    minimum([2])
##
##    2



def add2(listy):
    if len(listy) == 1:
        return listy[0]
    else:
        mid = len(listy)//2
        return add2(listy[:mid]) + add2(listy[mid:])

    # // return the integer
    # % return the reminder


import os
# os is using to access file
# os.listdir(directory) -> list of files/folders in directory
# os.path.join(directoy, file) -> full path (need to use this before next using the next one
# os.path.isdir(path) -> true if folder, false is file
    
def list_files(directory):
    filenames = []

    # look at everything in directory
    for f in os.listdir(directory):
        # is f a file or a folder?
        path = os.path.join(directory, f)
        if os.path.isdir(path):
            # folder - recursion
            files = list_files(path) # would give a list
            filenames.extend(files)
##            for x in files:
##                filenames.append(x)
        else:
            # file - base case
            filenames.append(path)
    return filenames

from pprint import pprint
res = list_files('D://Maple/Documents/1 CSSE7030/assign3/')
pprint(res)

import math

def dec2base(n, b):
    result = []
    if math.ceil(math.log(n,b)) == 0:
        result.append(int(n/b**0))
        print(result)
        return result
    else:
        x = n//(b**math.ceil(math.log(n,b)))
        if x<b and x>0:
            n = n - x*b**math.ceil(math.log(n,b))
            result.append(x)
        power = math.ceil(math.log(n,b)) - 1
        return dec2base(n,b)
        
        
