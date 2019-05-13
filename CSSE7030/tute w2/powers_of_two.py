#takes a positive integer as an input
#output a simple table that lists the powers of two up to the interger value passed to the program

n=input('enter the power:')
n=int(n)
m=0
table='0'
while m<=n:
    temp=str(2**m)
    m+=1
    print(table,temp)
    table=temp
