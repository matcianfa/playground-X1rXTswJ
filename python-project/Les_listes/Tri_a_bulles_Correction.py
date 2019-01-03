def ma_fonction(liste):
    for fin in range(len(liste)-1,0,-1):#indice où on arrete les comparaisons
        for i in range(fin): # indice de notre bulle
            if liste[i]>liste[i+1]:
                liste[i],liste[i+1]=liste[i+1],liste[i]
    return liste
