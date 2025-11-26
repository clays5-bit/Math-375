import pandas as pd
import numpy as np

def bisec(a, b, tol, func, target):
    data = []
    n=0
    while (b-a)*.5 > tol:
        n += 1
        c = (a + b)/2
        adj_c = func(c)-target
        data.append([n, a, c, b])
        if adj_c == 0:
            return table
        if (func(a)-target)*(adj_c) < 0:
            b = c
        else:
            a = c
    columns = ["Iterations", "a", "c", "b"]
    table = pd.DataFrame(data, columns = columns)
    xr = np.asarray(table["c"])
    fe = abs(c - xr)
    table["F-Error"] = fe
    return table

def base_fpi(x1, tol, func):
    data = []
    n=0
    x2 = func(x1)
    while abs(x2-x1) > tol and n < 100:
        n += 1
        data.append([n, x2])
        x1 = x2
        x2 = func(x1)
    columns = ["Iterations", "x2"]
    table = pd.DataFrame(data, columns = columns)
    xr = np.asarray(table["x2"])
    fe = abs(x2 - xr)
    table["F-Error"] = fe
    return table

def newt_fpi(x1, tol, func, dfunc, target):
    data = []
    x2 = x1-((func(x1)-target)/dfunc(x1))
    n = 0
    while abs(x2-x1) > tol and n < 100:
        x1= x2
        n += 1
        data.append([n, x2])
        x2 = x1-((func(x1)-target)/dfunc(x1))
    print(func(x2))
    columns = ["Iterations", "x2"]
    table = pd.DataFrame(data, columns = columns)
    xr = np.asarray(table["x2"])
    fe = abs(x2 - xr)
    table["F-Error"] = fe
    return table

def false(a, b, tol, func, target):
    data = []
    n=0
    adj_c = 1
    while abs(b-a)*.5 > tol and abs(adj_c) > tol:
        n += 1
        adj_a = func(a)-target
        adj_b = func(b)-target
        c = (b*adj_a-a*adj_b)/(adj_a-adj_b)
        adj_c = func(c)-target
        data.append([n, a, c, b])
        if(c) == 0:
            return data
        if adj_a * adj_c < 0:
            b = c
        else:
            a = c
    columns = ["Iterations", "a", "c", "b"]
    table = pd.DataFrame(data, columns = columns)
    xr = np.asarray(table["c"])
    fe = abs(c - xr)
    table["F-Error"] = fe
    return table