def mult_args(*args): # input more than 1 argument
    for i in args:
        print(i)

def mult_args_kwargs(*args, **kwargs): # args - normal argument, kwargs - keyword arguments
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(key, value)
    
"""
'underscore' _: return the last value OR for saving the temperary variable

"""
