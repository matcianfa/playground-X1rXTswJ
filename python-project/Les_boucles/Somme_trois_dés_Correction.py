def ma_fonction(k):
    compteur=0
    for i in range(1,7):
        for j in range(1,7):
            for l in range(1,7):
                if i+j+l==k:
                    compteur+=1
    return compteur
