def sort_string(word):
    # the thing in () is an arguement
    """ Return the sorted string corresponding to word

    ...
    """
    chars = sorted(word)
    return ''.join(chars)

def load_anag(d, filename):
    # first arguement is d, second arguement is a filename
    """ Add anagrams from filename to the dictionary, d

    ...
    """
    fd = open(filename, 'r') # 'r' means read the file
    for line in fd: # go through every line in the file
        word = line.strip() # strip() will remove all the space and empty line
        key = sort_string(word)
        value = d.get(key)
        if value is None:
            value = [word]
            d[key] = value
        elif word not in value: # or using else:
            value.append(word)
        #print(key,value)
    return d
    fd.close()
