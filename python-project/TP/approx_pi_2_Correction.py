def ma_fonction(n):
    c = 2**0.5
    for i in range(n-2): # On part de c_2 donc pour arrive à c_n il faut n-2 étapes
        c = (c*c/4+(1-(1-c*c/4)**2)**0.5)**0.5
    return n*c/2
