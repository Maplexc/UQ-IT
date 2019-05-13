def div_3_5(start, end):
    """Return the number of integers from start up to, but not including end that are divisible by 3 or 5

    Parameters:
        start (int): the start number
        end (int): end number (but not included)
    
    Return:
        range of number that are divisible by 3 or 5
    """
    div_3_5=()
    while start<end:
        if start%3==0 or start%5==0:
            div_3_5=div_3_5+tuple(start)
        start+=1
        
    return div_3_5
            
