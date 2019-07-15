def ma_fonction(u0,q,i,j):
    return u0*(q**i)*(1-q**(j-i+1))/(1-q)
