def mon_programme(u_0,e):
    if u_0>e: print(0)
    elif u_0<=0 : print('IMPOSSIBLE')
    else:
        n=0
        while u_0<e:
            n+=1
            u_0*=2
        print(n)
