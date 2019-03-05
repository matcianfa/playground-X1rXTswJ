def données(N):
    maximum=0
    u=N
    n=0
    while u!=1:
        if u%2==0 :
            u//=2
        else:
            u=3*u+1
        maximum=max(u,maximum)
        n+=1
    print(maximum,n)
