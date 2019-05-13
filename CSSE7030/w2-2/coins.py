# How many coin flips does it take on average?

# 0. Setup
# 1. Flip a coin
# 2. Move the pirate according to the rules
#    Increment (add one to) the flip tally
# 3. Check whether in the ocean
#       Yes => Record the flip tally;
#              Increment number of trials run;
#              Reset (go to 0) unless done
#       No => Go to 1
# 4. Calculate the average

# What to be told?
# - Total number of trials
# - Plank length

# What to keep track of?
# - Number of flips (so far)
# - Number of trials run (so far)
# - Position

import random

def flip_coin():
    """Flips a coin

    Return:
        bool: Returns True for a head, else False for a tail
    """
    if random.randint(0, 1) == 1:
        return True
    else:
        return False

def move(position, is_head):
    """..."""

    if is_head == True:  # head
        return position + 1
    else:  # tail
        if position == 0:  # at the start
            return 0
        else:  # not at the start
            return position - 1

def run_trial(plank_length):
    """..."""

    flips = 0
    position = 0

    while position < plank_length:
        is_head = flip_coin()
        position = move(position, is_head)

        #flips = flips + 1
        flips += 1

    return flips

def run_trials(plank_length, total_trials):
    """..."""

    trials = 0
    flips = 0

    current_trial = 0

    while current_trial < total_trials:
        flips += run_trial(plank_length)
        trials += 1

        current_trial += 1

    return flips / trials
    # return flips / total_trials
    
    












