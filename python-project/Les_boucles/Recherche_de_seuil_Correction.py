def ma_fonction(u0,e):
    u=u0
    n=0
    while u>=e:
        n+=1
        u=0.5*u
    return n
