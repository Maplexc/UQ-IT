#!/usr/bin/env python3
"""
Assignment 1
CSSE1001/7030
Semester 2, 2018
"""
import a1_support
import string
from a1_support import is_word_english

__author__ = "Xin Chen 45189915"

# Write your functions here
def encrypt(text,offset):
    """Encrypts text by replacing each letter with the letter some fixed number of positions(the offset) down the alphabet      

    Parameters:
        text(str): text will encrypt
        offset(int): the position of the letter that will replace the letter in text

    Return:
        str: the encrypted text
    """
    offset_lowercase=list(string.ascii_lowercase)
    offset_uppercase=list(string.ascii_uppercase)
    offset_text=''
    for pos_text in range (0,len(text)):
        if text[pos_text].islower():
            pos_offset=string.ascii_lowercase.index(text[pos_text])
            total_offset=pos_offset+offset
            if total_offset>=26:
                total_offset=total_offset-26
            offset_text+=offset_lowercase[total_offset]
        elif text[pos_text].isupper():
            pos_offset=string.ascii_uppercase.index(text[pos_text])
            total_offset=pos_offset+offset
            if total_offset>=26:
                total_offset=total_offset-26
            offset_text+=offset_uppercase[total_offset]
        else:
            offset_text+=text[pos_text]
    return offset_text


def decrypt(text,offset):
    """Decrypts text that was encrypted by the encrypt function above

    Parameters:
        text (str): text will decrypt
        offset: the position of the letter that will replace the letter in text

    Return:
        str: the decrypted text
    """
    offset_text = encrypt(text,-offset)
    return offset_text

  
def find_encryption_offsets(encrypted_text):
    """Return a tuple containing all possible offsets that could have been used if to encrypt some English text into encrypted_text

    Parameter:
        encrypted_text (str): text want to be 

    Return:
        tuple containing all possible offsets that could 
    """
    valid=[]
    encrypted_text_test=''
    for i in range (0,len(encrypted_text)):
        if encrypted_text[i].islower() or encrypted_text[i] == ' ':
            encrypted_text_test+=encrypted_text[i]
        elif encrypted_text[i].isupper():
            lower_text = encrypted_text[i].lower()
            encrypted_text_test+=lower_text
        elif encrypted_text[i] == '-':
            encrypted_text_test+=' '
        else:
            encrypted_text_test+=''
    for offset_all in range (1,26):
        string=decrypt(encrypted_text_test,offset_all)
        words=string.split()     
        is_valid=True
        for is_english in words:
            if a1_support.is_word_english(is_english)==False:
                is_valid = False
                break    
        if is_valid:
            valid.append(offset_all)
    return tuple(valid)



#alterntive methods
##def find_encryption_offsets(encrypted_text):
##    """Return a tuple containing all possible offsets that could have been used if to encrypt some English text into encrypted_text
##
##    Parameter:
##        encrypted_text (str): text want to be 
##
##    Return:
##        tuple containing all possible offsets that could 
##    """
##    valid=()
##    for offset_all in range (1,26):
##        string=decrypt(encrypted_text,offset_all)
##        words=string.split()
##        is_valid=()
##        for n in range (0,len(words)):
##            is_english=words[n]
##            if a1_support.is_word_english(is_english)==False:
##                is_valid+=(False,)
##            else:
##                is_valid+=(True,)
##        if all(is_valid):
##            valid+=(offset_all,)
##    return valid





def main():
    # Add your main code here
    print('Welcome to the simple encryption tool!')
    option=''
    while option != 'q':
        option=input('\n'
                     'Please choose an option [e/d/a/q]: \n'
                     'e) Encrypt some text \n'
                     'd) Decrypt some text \n'
                     'a) Automatically decrypt English text \n'
                     'q) Quit \n'
                     )
        # to quit
        if option == 'q':
            break
        # to encrypt text
        elif option == 'e':
            text=input('Please enter some text to encrypt:')
            offset=int(input('Please enter a shift offset (1-25):'))
            if offset>=1 and offset<=25:
                print('The encrypted text is:',encrypt(text,offset))
            elif offset==0:
                for offset_all in range (1,26):
                    print("%02d" % offset_all,': ',encrypt(text,offset_all),sep='')
            else:
                print('Invalid command')
        # to decrypt text 
        elif option == 'd':
            text=input('Please enter some text to decrypt:')
            offset=int(input('Please enter a shift offset (1-25):'))
            if offset>=1 and offset<=25:
                print('The decrypted text is:',decrypt(text,offset))
            elif offset==0:
                for offset_all in range (1,26):
                    print("%02d" % offset_all,': ',decrypt(text,offset_all),sep='')
            else:
                print('Invalid command')
        # to automatically decrypt English text
        elif option == 'a':
            text=input('Please enter some encrypted text:')  
            valid=find_encryption_offsets(text)
            if len(valid)==1:
                print('Encryption offset:', valid[0])
                print('Decrypted message:',decrypt(text,valid[0]))
            elif len(valid)==0:
                print('No valid encryption offset')
            else:
                print('Multiple encryption offsets:', end=' '), print(*valid,sep=', ')
        # if users input the invalid command
        else:
            print('Invalid command')
    print('Bye!') 
                


##################################################
# !! Do not change (or add to) the code below !! #
#
# This code will run the main function if you use
# Run -> Run Module  (F5)
# Because of this, a "stub" definition has been
# supplied for main above so that you won't get a
# NameError when you are writing and testing your
# other functions. When you are ready please
# change the definition of main above.
###################################################

if __name__ == '__main__':
    main()





