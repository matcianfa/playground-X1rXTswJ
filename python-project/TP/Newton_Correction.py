def Newton(f,x0,n):
    x = x0
    for i in range(n):
        x = x - f(x)/deriver(f,x,0.000001)
    return x
