def Julia(mu,u0):
    n = 0
    u = u0
    while abs(u) < 1000 and n < 200:
        u = mu*u*(1-u)
        n += 1
    return n
