# A leap year occurs when the year is a multiple of four
# unless the year is a multiple of 100
# However, if the year is a multiple of 400, then it is a leap year
#   For instance, 2016 and 2000 are leap years, but 1900 is not

#print True if the year is a leap year, and False if not

n=int(input('Please enter a year: '))


if n%400==0:
    print(True)
elif n%4==0:
    if n%100==0:
        print(False)
    else:
        print(True)
else:
    print(False)


#challenge 1: days of the week
#prints the day of the week corresponding to that date

d=input('Please enter the day of the month:')
d=int(d)
m=input('Please enter the month:')
m=int(m)
y=input('Please enter the year:')
y=int(y)
