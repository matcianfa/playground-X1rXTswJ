def ma_fonction(u0,e):
    if u0>e: return 0
    elif u0<=0 : return 'IMPOSSIBLE'
    else:
        n=0
        while u0<e:
            n+=1
            u0*=2
        return n
