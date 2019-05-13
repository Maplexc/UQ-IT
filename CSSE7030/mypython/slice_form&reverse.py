def slice_form(string,start,end):
    """slice_form function which return the characters in string from index start up to, but not including
    
    parameter:
    string (str): enter a string
    start (int): the index start up to
    end (int): the index end up but not including"""
    string=input('plz enter a string:')
    start=inpu
    n=len(enter)
    index=0
    slice=''
    while index<=n-1:
        char=enter[index]
        slice=slice+char
        index+=1
    print(slice)
    
def reverse_string(string):
    """reverse_string function which returns the characters in string in reverse order
    
    parameter:
    string (str): enter a string"""
    enter=input('plz enter a string:')
    n=len(enter)
    index=n-1
    reverse=''
    while index>=0:
        char=enter[index]
        reverse=reverse+char
        index-=1
    print(reverse)

def reverse_string1(string):
    """reverse_string function which returns the characters in string in reverse order
    
    parameter:
    string (str): enter a string"""
    
    """n=len(string)
    index=n-1
    reverse=''
    while index>=0:
        char=string[index]
        reverse=reverse+char
        index-=1
    return reverse"""
    
    slice=string[::-1]
    return slice
