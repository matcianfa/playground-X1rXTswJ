def ma_fonction(n):
    n-=1
    mot='G'
    while n>0:
        mot_renversé=''
        for lettre in mot:
            if lettre=='G':
                mot_renversé='D'+mot_renversé
            else :
                mot_renversé='G'+mot_renversé
        mot=mot+'G'+mot_renversé
        n-=1
    return mot
