def syracuse(N):
    u=N
    liste=[N]
    while u!=1:
        if u%2==0 :
            u//=2
        else:
            u=3*u+1
        liste.append(u)
    return liste
