def ma_fonction(c):
    compteur=0
    for a in range(c+1):
        for b in range(c+1):
            if a**2+b**2==c**2:
                compteur+=1
    return compteur
