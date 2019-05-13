#def → start to write a function
def add(n,m):
    """program to return the addition of two numbers
    add(int,int) → int
    
    Parameters:
    n (int): the first number to be added
    m (int): the second number to be added  
    """
    temp=n+m  #temp indicate a temperary variable
    return temp

def add2(n,m):
    """program to return the addition of two numbers
    add(int,int) → int
    
    Parameters:
    n (int): the first number to be added
    m (int): the second number to be added  
    """
    temp=n+m
    print(temp)



def mult(n,m,o):
    #have to enter 3 variable, if not it will show error
    #(4 spaces 缩进)
    temp=n*m*o
    return temp

def mult1(n,m,o):
    return n*m*o
#it does work if do not use temp variable
# """ & # both are comments
# but when using tripple quote """ as a comment when writing a function
# the comments will come out at the same time when you run the function
# """ comments are more useful (need to use it in the exam, loss mark if not use)
# """ comments help readers to understand

def size(n):
    """program to determine size of number"""
    # : called colon
    if n==1:
        result = 'One'
    else:
        result = 'Many'
    return result


def size1(n):
    """program to determine size of number, large or small"""
    if n<=5:
        return 'small'
    else:
        return 'large'

def sumto(n):
    """program to add all the numbers between 1 and n"""
    total=0
    for m in range(n+1):
        #why using n+1 instead of n???
        total=total+m
    return total





