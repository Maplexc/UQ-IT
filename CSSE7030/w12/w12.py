def add_half(a,b):
    """ add a to b/2 """
    return a+b/2

def second_function(function1):
    return function1(3,10)

# create function add_quarter; then call third_function which returns add_half(3,10) + add_quarter(3,10)
def add_quarter(a,b):
    """ add a to b/4"""
    return a+b/4

def third_function(function1,function2):
    return function1(3,10)+function2(3,10)



def my_iter(xs):
    for x in xs:
        yield x

def my_iter2(xs):
    for x in xs:
        print('start', x)
        yield x
        print('finish',x)

def mycount(n):
    while True:
        yield n
        n += 1
    # cannot change it to normal list
        
def myzip(xs,ys):
    xs = iter(xs)
    ys = iter(ys)
    while True:
        try:
            x = next(xs)
            y = next(ys)
            yield x,y
        except:
            break

import random # have a method to get random number between 0 and 1
def myshuffle(xs):
    """returns a shuffle of xs
    myshuffle(list(int)) -> list(int)"""
    ys = [(random.random(),x) for x in xs] # insert a random number to each x in xs
    ys.sort() # sort the random number
    return [x for y,x in ys] # select the second element of the tuples

import operator
def cube(x):
    return x**3

xs = [3,4,5,6]
g = map(cube, xs)
print(list(g))
    ## list(<iterator>) => turn a iterator into a list
print(list(map(operator.mul, [1,2,3,4],[5,6,7,8]))) # operator.mul -> multiply the elements of 2 lists
print(list(map(operator.mul, [1,2,3,4],2*[5,6,7,8]))) # get the exactly same result as the previous one
    # 2*[5,6,7,8] => [5,6,7,8,5,6,7,8]

print(sum(list(map(operator.mul, [1,2,3,4], [5,6,7,8]))))




