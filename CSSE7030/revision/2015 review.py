# Q9
def g(x,z):
    x.append(z)
    return x

# Q14
def md(x):
    a,b = x
    a,b = a//b, a%b
    return (a,b)

# Q17
def fi(xs, n, m):
    s = xs[n]
    r = [s]
    while n<m:
        if xs[n] > s:
            s=xs[n]
            r.append(s)
        n += 1
    return r

# Q21
def hti(xs, v, h):
    i = h
    inc = 0
    n = len(xs)
    while xs[i] is not None:
        if xs[i] == v:
            return
        inc += 1
        i = (i+inc) % n
    xs[i] = v
    
# Q40
def t(xs):
    return [[xs[i][j] for i in range(len(xs))] for j in range(len(xs[0]))]






















