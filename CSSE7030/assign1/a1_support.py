"""Supporting functions for assignment 1

CSSE1001
Semester 2, 2018
"""
from functools import partial

def load_words(word_file):
    """list<str> Returns a list of words loaded from a word file

    Parameter:
        word_file (str): The filename of the word file
    """
    with open(word_file) as f:
        lines = [line.strip() for line in f]
        return [word.strip() for word in lines if word]


_is_word_english = partial(lambda words, word: word in words, set(load_words('words.txt')))


def is_word_english(word):
    """(bool) Returns True iff 'word' is an all-lowercase English word, contained in words.txt

    Parameters:
        word (str): The word to check

    Examples:
        >>> is_word_english('pickle')
        True
        >>> is_word_english('malarkey')
        True
        >>> is_word_english('gregarious')
        True
        >>> is_word_english('GReGarIoUs')
        False
    """
    return _is_word_english(word)


def is_numeric(value):
    """(bool) Returns True iff 'value' is numeric"""

    try:
        float(value)
        return True
    except:
        return False



