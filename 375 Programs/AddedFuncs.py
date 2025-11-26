def bisec(a, b, tol, func, target):
    n=0
    while (b-a)*.5 > tol:
        n += 1
        c = (a + b)/2
        adj_c = func(c)-target
        if adj_c == 0:
            return c, n
        if (func(a)-target)*(adj_c) < 0:
            b = c
        else:
            a = c
    err = (b-a)/(2**(n+1))
    return c, n, err

def base_fpi(x1, tol, func):
    x2 = func(x1)
    n=0
    while abs(x2-x1) > tol and n < 100:
        n += 1
        x1 = x2
        x2 = func(x1)
    return(x2, n)


def newt_fpi(x1, tol, func, dfunc, target):
    x2 = x1-((func(x1)-target)/dfunc(x1))
    n = 0
    while abs(x2-x1) > tol and n < 100000:
        n += 1
        x2 = x1-((func(x1)-target)/dfunc(x1))
    return x2, n

def false(a, b, tol, func, target):
    n=0
    adj_c = 1
    while abs(b-a)*.5 > tol and abs(adj_c) > tol:
        n += 1
        adj_a = func(a)-target
        adj_b = func(b)-target
        c = (b*adj_a-a*adj_b)/(adj_a-adj_b)
        adj_c = func(c)-target
        if(c) == 0:
            return c, n
        if adj_a * adj_c < 0:
            b = c
        else:
            a = c
        #print(adj_b-adj_a, adj_c)
    return c, n