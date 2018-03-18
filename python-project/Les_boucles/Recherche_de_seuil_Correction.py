def mon_programme(u_0,e):
    u=u_0
    n=0
    while u>=e:
        n+=1
        u=0.5*u
    print(n)
