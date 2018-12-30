def ma_fonction(n):
    somme=0
    for d in range(1,n):
        if n%d==0: somme+=d
    if somme == n:
        return 'PARFAIT'
    else:
        return 'PAS PARFAIT'
