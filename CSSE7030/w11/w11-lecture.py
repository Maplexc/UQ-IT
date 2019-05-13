def is_palindrome(s):
    """ Function to check whether or not a string is a palindrome
            e.g.'abba' spell from forward and backward is the same
            can use recursion e.g. check the first and last letter is_palindrome or not,
            then the second and second last letter is_palindrom...
        s (str) => (return) Boolean"""
    if len(s)<2:
        return True
    return s[0]==s[-1] and is_palindrome(s[1:-1]) # s[1:-1] means get select the string from second letter to the end but didnt include the last letter
    
## function to sum the number between 1 to n
#  break into sumto(n) = n + sumto(n-1)
def sumto(n):
    """ Return the sum of numbers from 0 to n

        sumto(int) -> int

        Precondition: n >= 0"""
    if n == 1:
        # base case
        return 1
    else:
        return n + sumto(n-1)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def max_of_list(xs):
    """ finding the maximum element in an non-empty list

        max_of_list(list(X)) -> X"""

    if len(xs) == 1:
        return xs[0]
    else:
        m = max_of_list(xs[1:])
        if m < xs[0]:
            return xs[0]
        else:
            return m

def max_list(xs):
    if len(xs) == 1:
        return xs[0]
    else:
        return max(xs[0], max_list(xs[1:]))
