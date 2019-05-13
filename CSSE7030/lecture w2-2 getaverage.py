import random

def toss():

    """simulate the toss of a coin to obtain a head or tail

    parameters:
        no input arguments

    return:
        str:'head' or 'tail' """
    if random.randint(0,1)==0:
        return 'head'
    else:
        return 'tail'


def move(pos,coin_toss_result):
    """return the new position of the pirate given the current postion and the result of a coin toss

    Parameters:
        pos(int): the position along the plank
        coin_toss_result: 'head' or 'tail'
        
    
    """
    if coin_toss_result=='head':
        pos=pos+1
    elif pos==0:
        pos=0
    else:
        pos=pos-1
    print(pos)
    return pos
        
