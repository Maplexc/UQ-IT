def read_scores(file_name):
    """

    Parameter:
        file_name (str)

    Return:
        dict
    ...
    """
    dict_score = {}
    scrabble_score = []
    file_object = open(file_name,'r')
        # 2 differences for 2 open ways:
        # remember to close the file at the end, if not you we use many memory and have many file open on the background
        # in this way, the file open can be used in other function BUT in the way below, can only used in its own function, as it will automatically close the file for you
    for line in file_object:
        line = line.strip()
        scrabble_score = line.split(',')
        key = int(scrabble_score[1])
        if key not in dict_score.keys():
            dict_score[key] = [scrabble_score[0],]
        else:
            dict_score[key].append(scrabble_score[0])
    file_object.close()
    return dict_score

def read_scores_ans(filename):
    scores = {}
    with open(filename, 'r') as file: # using this way, it will automatically close the file for you at the end
        # your code goes, the file is open
        for line in file:
            line = line.strip()
            letter, _, value = line.partition(',')
            scores[letter]=int(value)
    # file closed

    return scores
            
        
    
    

    
        
def get_score(scores, word):
    """

    Parameter:
        scores (dict)
        word (str)

    ...
    """
    score = 0
    for n in range (0,len(word)):
        for key,value in scores.items():
            if word[n] in value:
                score += key
    return score
                
def get_score_ans(scores, word):
    total_score = 0
    
    for letter in word.lower():
        # letter = letter.lowercase() # case sensitive
        
        total_score += scores.get(letter,0)
    return total_score



    
    
