def mult_args(*args):   # input multiple arguments
    total = 0
    for i in args:
        total += i
    return total

def mult_args_kwargs(*args, **kwargs):
    for i in args:
        print(i)
    for key,value in kwargs.items(
