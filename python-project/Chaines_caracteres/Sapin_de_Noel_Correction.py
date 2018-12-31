def ma_fonction(n):
    if n==0:
        return '.'
    else:
        for k in range(n):
            return '.'*(n-k-1)+'^'*(2*k+1)+'.'*(n-k-1)
