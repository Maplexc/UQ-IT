import random
n=random.randint(10,99)
m=random.randint(10,99)
print(n,'+',m,'=')
ans=input()
ans=int(ans)
if ans==n+m:
    print('Correct!')
else:
    print('No, the correct answer is', ans)
