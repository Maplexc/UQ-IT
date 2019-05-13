#guess a number

import random
target=random.randint(1,100)
print('Try to guess the number I am thinking of between 1 and 100')

n=int(input('Please enter your guess:'))
while n!=-1:
    if n==target:
        print('Congratulations! You have guessed correctly.')
        break
    elif n>target:
        print('sorry that is not correct. \n'
              'tips: enter a smaller number')
        n=int(input('Please enter your guess:'))
    elif n<target:
        print('sorry that is not correct. \n'
              'tips: enter a bigger number')
        n=int(input('Please enter your guess:'))
print('The number you were trying to guess was',target)
