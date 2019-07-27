def u(mu,u0,n):
    liste = [u0]
    u = u0
    for _ in range(n):
        u = mu*u*(1-u)
        liste.append(u)
    return liste
