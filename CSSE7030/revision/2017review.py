## 2017 sem1
# Q12
##value = input("Enter one of: 'a', 'b', 'c' or 'd' ")
###if value in ('a','b','c','d'):
###if value == ('a' or 'b' or 'c' or 'd'):
##if value in 'abcd':
##    print(True)
##else:
##    print(False)


# Q13
def logic(x,y,z):
    return x and y or z


# Q14
def test(count):
    x = True
    while count > 0 :
        if count > 100:
            x = True
        else:
            x = False
        count -= 1
    return x

# Q20
def rec(x):
    if x==1:
        return x
    else:
        return rec(x-1)*x

# Q21
def product(nums):
    total = 0
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    return (product(nums[:len(nums) // 2]) * product(nums[len(nums) // 2:]))

# Q22
def get_days(years):
    total_days = 0
    while years >= 0:
        total_days += 365
        years -= 1
    return total_days

# Q28
##class A:
##    def __init__(self,x):
##        self.x = x
##
##    def f(self,x):
##        return self.g(x)-1
##
##    def g(self,x):
##        return 2*x
##
##class B(A):
##    def g(self, y):
##        return self.x + y
##
##class C(B):
##    def __init__(self,x,y):
##        super().__init__(x)
##        self.y = y
##
##    def f(self,x):
##        return self.x + self.y
##
##class D(B):
##    def __init__(self, x, y):
##        super().__init__(x)
##        self.x += y
##        self.y = y
##
##    def g(self,y):
##        return self.y + y
##
##    def f(self,x):
##        return super().f(x) - x
##
##a = A(3)
##b = B(2)
##c = C(2,4)
##d = D(1,3)

## 2017 sem2
# Q10
def g(p):
    z = p.pop(0)
    p.extend(z)
    return p

# Q14
##def f(x,y):
##    y = y + [x]
##    return y

# Q21
def m(x):
    a,b = x
    if a>b:
        return(b, a*a+b*b)
    elif a<b:
        return(a,b*b+a*a)
    else:
        return (a,b)

# Q28
def f(xs):
    i = 0
    r = []
    while i >= 0 and i < len(xs):
        d,v = xs[i]
        r.append(v)
        i += d
    return r

# Q31
class A(object):
    def __init__(self, x):
        self.x = x

    def g(self, x):
        return self.f(x)

    def f(self, x):
        return 3*x

class B(A):
    def g(self, y):
        return self.x + 2*y
    
class C1(B):
    def __init__(self, x, y):
        B.__init__(self, x)
        self.y = y

    def f(self, x):
        return self.x + self.y

class C2(B):
    def __init__(self, x, y):
        B.__init__(self, x)
        self.y = y

    def f(self, x):
        return x + self.x + 2* self.y
    
a = A(2)
b = B(1)
c1 = C1(2, 4)
c2 = C2(2, 4)

# Q39
def recursiveIndex(nested, indexes):
    if indexes == []:
        return nested
    else:
        return recursiveIndex(nested[indexes[0]], indexes[1:])


