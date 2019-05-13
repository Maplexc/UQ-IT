print('this is the first line')
print('this is the second line')

#same as below

print('this is the first line \n'
      'this is the second line')
print('this is the first line \n' 'this is the second line')


#combine the string
string_1='abcdef'
string_1=string_1+'adsag'
#same as
string_1+='adsag'

print(string_1)

#index of string using [] (start from 0) - pick up the characters in string
#string_1[-1] show the last character of string_1 (will go error if the number input is greater than the number of char have in the string)

#string_1[3:5] pick up the characters from index3(4th char) to index5(6th char) (BUT do not include index5)
#string_1[3:9:2] start index3 to index9(BUT do not include) get the 2nd char (have one char break)
#(will not show error, if put end number greater than the character number)



#print out all char of the string
for char in string_1:
    print(char)

#give the index (position) & the char (useful in assignment)
for char in enumerate(string_1):
    print(char)
    
#seperate index(i) and char out
for i,char in enumerate(string_1):
    print(i,char)

#search for the particular char and find the index of that char
def find(substr, string, start):
    """return the position of the first substr in string, starting from start.
    return none if not found

    parameters:
        substr(str): substring being searched for
        string(str): string being searched
        start(str): index where the search begines

    return:
        int: index where substr is found within string
    """
    pos = start
    size = len(substr)
    while pos < len(string):
        if substr == string[pos:pos+size]:
            return pos
        pos += 1
    return None

#tuple
tuple_1=('',1, 19,0)
#can add tuples together (if only 1 element in tuple, should write it with comma, e.g. (5,) )

