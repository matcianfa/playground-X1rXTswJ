def ma_fonction(N):
    u = 2
    S = u
    for i in range(1,N+1):
        u = 2*u-1
        S+=u
    return S
