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
        text(str): text want to encrypt
        offset(int): the position of the letter that will replace the letter in text

    Return:
        str: the encrypted text
    """
    offset_lowercase = list(string.ascii_lowercase)
    offset_uppercase = list(string.ascii_uppercase)
    offset_text = ''
    # offset each character in the sentence
    for i in range (0,len(text)):
        if text[i].islower():
            pos_offset = string.ascii_lowercase.index(text[i]) # find the index of the text character in lowercase alphabet
            total_offset = pos_offset + offset
            if total_offset >= 26:
                total_offset = total_offset - 26
            offset_text += offset_lowercase[total_offset]
        elif text[i].isupper():
            pos_offset = string.ascii_uppercase.index(text[i]) # find the index of the text character in upppercase alphabet
            total_offset = pos_offset + offset
            if total_offset >= 26:
                total_offset = total_offset - 26
            offset_text += offset_uppercase[total_offset]
        else:
            offset_text += text[i]
    return offset_text


def decrypt(text,offset):
    """Decrypts text that was encrypted by the encrypt function above

    Parameters:
        text (str): text want to decrypt
        offset: the position of the letter that will replace the letter in text

    Return:
        str: the decrypted text
    """
    offset_text = encrypt(text,-offset)
    return offset_text

  
def find_encryption_offsets(encrypted_text):
    """Return a tuple containing all possible offsets that can decrypt the text into English

    Parameter:
        encrypted_text (str): text want to find the offset number

    Return:
        tuple containing all possible offsets that can decrypt the text into English
    """
    valid = []
    encrypted_text_test = ''
    # to remove all the punctuations and convert text to lowercase
    for i in range (0,len(encrypted_text)):
        if encrypted_text[i].islower() or encrypted_text[i] == ' ':
            encrypted_text_test += encrypted_text[i]
        elif encrypted_text[i].isupper():
            lower_text = encrypted_text[i].lower()
            encrypted_text_test += lower_text
        elif encrypted_text[i] == '-':
            encrypted_text_test += ' '
        else:
            encrypted_text_test += ''   
    # find the offset number where it can decrypt the input text into English
    for offset_all in range (1,26):
        string = decrypt(encrypted_text_test,offset_all)
        words = string.split()
        is_valid = True
        # check if each word in the sentence is English (True if all words are English)
        for is_english in words:
            if a1_support.is_word_english(is_english) == False:
                is_valid = False
                break
        if is_valid:
            valid.append(offset_all)
    return tuple(valid)


def main():
    # Add your main code here
    """This is a simple encryption tool which use to encrypted and decrypted text.

    It has 4 options:
        e: encrypt text
            you will be asked to enter some text that you want to encrypt and a shift offset number between 1 and 25
            it will return an encrypted text, if you enter a valid number
            0 can enter as the offset number, encrypted text should be shown for all offsets (1 to 25, inclusive) when enter 0
            otherwise, it will show 'invalid command'
                        
        d: decrypt text
            you will be asked to enter some text that you want to decrypt and a shift offset number between 1 and 25
            it will return an decrypted text, if you enter a valid number
            0 can enter as the offset number, decrypted text should be shown for all offsets (1 to 25, inclusive)
            otherwise, it will show 'invalid command'
            
        a: automatically decrypt English text
            you will be asked to enter some text that you want to decrypt
            it will return all the possible offset number if the text you enter can be decrypted to English text
                if it cannot find any offset number, it will show 'No valid encryption offset'
                if it finds only one offset number, it will return the offset number and show the decrypted English text
                if it finds more than one offset number, it will return all the offset number
                
        q: quit
    """
    option = ''
    print('Welcome to the simple encryption tool!')
    while option != 'q':
        option = input('\n'
                     'Please choose an option [e/d/a/q]:\n'
                     '  e) Encrypt some text\n'
                     '  d) Decrypt some text\n'
                     '  a) Automatically decrypt English text\n'
                     '  q) Quit\n'
                     '> ')
        if option == 'q':
            break
        # to encrypt text if user choose 'e'
        elif option == 'e':
            text = input('Please enter some text to encrypt: ')
            offset = int(input('Please enter a shift offset (1-25): '))
            if offset >= 1 and offset <= 25:
                print('The encrypted text is:',encrypt(text,offset))
            elif offset == 0:
                print('The encrypted text is:')
                for offset_all in range (1,26):
                    print('  ',"%02d" % offset_all,': ',encrypt(text,offset_all),sep='')
            else:
                print('Invalid command')
        # to decrypt text if user choose 'd'
        elif option == 'd':
            text = input('Please enter some text to decrypt: ')
            offset = int(input('Please enter a shift offset (1-25): '))
            if 1 <= offset <= 25:
                print('The decrypted text is:',decrypt(text,offset))
            elif offset == 0:
                print('The decrypted text is:')
                for offset_all in range (1,26):
                    print('  ',"%02d" % offset_all,': ',decrypt(text,offset_all),sep='')
            else:
                print('Invalid command')
        # to automatically decrypt English text if user choose 'a'
        elif option == 'a':
            text = input('Please enter some encrypted text: ')  
            valid = find_encryption_offsets(text)
            if len(valid) == 1:
                print('Encryption offset:', valid[0])
                print('Decrypted message:',decrypt(text,valid[0]))
            elif len(valid) == 0:
                print('No valid encryption offset')
            else:
                print('Multiple encryption offsets:', end = ' '), print(*valid,sep = ', ')
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






"""
----------------------------------------------
MARKING:   ##### CSSE7030 #####

Total: 10

Meeting comments:
   

General comments:
   Programming Constructs
       Program is Well Structured & Readable
           Code structure highlights logical blocks and is easy to understand. Code does not employ unnecessary global variables. Constants clarify code meaning.
       Variable and function names are meaningful
           All identifier names are informative, clearly describing their purpose, and aiding code readability.
       Algorithmic logic is appropriate
           Algorithm design is simple, appropriate, and has no logical errors.
   Documentation
       Clear & Concise Docstring Descriptions
           All docstrings are accurate, complete & unambiguous descriptions of how item is to be used.
       Parameter & Return Types
           All parameters and return types, and expected values, are described clearly.
       Clear Inline Comments
           Comments provide useful information that clarifies the intent of the code, making it easier to understand. Comments do not repeat logic already clear in code.
       Relevant Inline Comments
           Important or complex blocks of logic (e.g. significant loops or conditionals) are clearly explained and summarised (i.e. stating a loop iterates over a list is not a useful explanation or summary).
   Functionality
       encrypt
           All functionality is implemented correctly
       decrypt
           All functionality is implemented correctly
       find_encryption_offsets
           All functionality is implemented correctly
       main
           Functionality for at least two of encrypt/decrypt/invalid cases is implemented correctly
   Extension
       Offsets
           Handling of zero offsets is implemented perfectly
       find_encryption_offsets
           Handling of contractions, hyphens, and arbitrary characters is not implemented perfectly
   General

----------------------------------------------
TEST RUN:
/------------------------------------------------------------------------------\
|                              Summary of Results                              |
\------------------------------------------------------------------------------/
TestDesign
    + 1. test_clean_import
    + 2. test_defined
    + 3. test_documentation
TestEncrypt
    + 1. test_sample
    + 2. test_lower_no_overflow
    + 3. test_lower_overflow
    + 4. test_upper_no_overflow
    + 5. test_upper_overflow
    + 6. test_mixed_overflow
    + 7. test_complex
    + 8. test_zero_offset
TestDecrypt
    + 1. test_sample
    + 2. test_lower_no_overflow
    + 3. test_lower_overflow
    + 4. test_upper_no_overflow
    + 5. test_upper_overflow
    + 6. test_mixed_overflow
    + 7. test_complex
    + 8. test_zero_offset
TestFindEncryptionOffsets
    + 1. test_sample
    + 2. test_lower_vs_upper
    - 3. test_contractions_ignored
    + 4. test_hyphens
    + 5. test_ignores_punctuation
    + 6. test_complex
TestMain
    + 1. test_sample
    + 2. test_encrypt
    + 3. test_decrypt
    + 4. test_invalid
    + 5. test_extension_autodecrypt_sample
    + 6. test_extension_encrypt_zero_sample
    + 7. test_extension_decrypt_zero
    + 8. test_not_recursive
--------------------------------------------------------------------------------
/------------------------------------------------------------------------------\
|                                 Failed Tests                                 |
\------------------------------------------------------------------------------/
================================================================================
FAIL: TestFindEncryptionOffsets 3. test_contractions_ignored
--------------------------------------------------------------------------------
    Traceback (most recent call last):
      File "test_a1_marking.py", line 204, in test_contractions_ignored
        self.assertEqual(feo("ai'vi ksswi'h"), tuple(range(1, 26)))
    AssertionError: Tuples differ: (4,) != (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13[44 chars], 25)

    First differing element 0:
    4
    1

    Second tuple contains 24 additional elements.
    First extra element 1:
    2

    - (4,)
    + (1,
    +  2,
    +  3,
    +  4,
    +  5,
    +  6,
    +  7,
    +  8,
    +  9,
    +  10,
    +  11,
    +  12,
    +  13,
    +  14,
    +  15,
    +  16,
    +  17,
    +  18,
    +  19,
    +  20,
    +  21,
    +  22,
    +  23,
    +  24,
    +  25)

--------------------------------------------------------------------------------
Ran 33 tests in 0.116 seconds with 32 passed/0 skipped/1 failed.


END TESTS
"""

