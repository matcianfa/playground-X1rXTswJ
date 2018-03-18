def mon_programme(n):
    somme=0
    for d in range(1,n):
        if n%d==0: somme+=d
    if somme == n:
        print("PARFAIT")
    else:
        print("PAS PARFAIT")
