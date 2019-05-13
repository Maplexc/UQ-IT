def int_exception():
    """Input a number and return it as an integer.
    If the input cannot be converted into an integer return -1

    ...
    """
    num = input('Enter a number:')
    try:    # try can skip the error (will using if/else, it will have error msg and stop the program
        return int(num)
    except Exception:   # if cannot do, do the following code
        print('You have entered a non-numerical value')
        return -1
    

def int_exception1(in_num):
    """ Asks for user input and attempts to divide in_num by
    the number input by the user. If a non-numerical input is given then -1 will be return.
    If any exception occurs -1 will be returned.

    ...
    """
    num = input('Enter a number:')
    try:
        num = int(num)
        return in_num/num
    except Exception as e:
        print('Error:', str(e)) # show the error
        return -1
            
                
def int_exception2(in_num):
    """ Asks for user input and attempts to divide in_num by
    the number input by the user. If a non-numerical input is given then -1 will be return.
    If any exception occurs -1 will be returned.

    ...
    """
    num = input('Enter a number:')
    try:
        num = int(num)
        return in_num/num
    except ValueError:
        print('That is not a number')
    except ZeroDivisionError:
        print('Divide by zero')
    except Exception as e:
        print('Error:', str(e)) # show the error
        return -1


def addnums():
    num1 = input('Enter number 1: ')
    num2 = input('Enter number 2: ')
    try:
        num1 = int(num1)
        num2 = int(num2)
        return num1 + num2
    except Exception as e:
        print('Error: ', str(e))
    return -1


def function1(number):
    if number == 0:
        raise ZeroDivisionError('Divide by zero')
    return 15/number

try:
    function1(0)
except Exception:
    print('Divide by zero')








    
