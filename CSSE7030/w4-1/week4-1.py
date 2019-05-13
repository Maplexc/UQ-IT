def double(xs):
    """return the list of the doubles of the elems of xs

    ...
    """
    result = []
    #start with an empty list
    for x in xs:
        result.append(2*x)
        # OR result+=[2*x,]
    return result

def change_fn(x):
    x=5
    return x

def evens(xs):
    """return the even elems of xs

    ...
    """
    result = []
    for i,x in enumerate(xs):
        if i%2 == 0:
        # i is index
            result.append(x)
    return result
            
        
