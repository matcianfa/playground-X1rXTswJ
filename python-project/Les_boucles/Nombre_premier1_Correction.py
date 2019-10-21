def ma_fonction(n):
    if n<2:
        return 'PAS PREMIER'
    else:
        for d in range(2,n):
            if n%d==0:
                return 'PAS PREMIER'
        return 'PREMIER'
