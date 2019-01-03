def ma_fonction(liste):
    for curseur in range(len(liste)-1): #curseur indiquant la limite entre partie déja triée et partie à trier
        minimum=liste[curseur]
        indice_minimum=curseur
        for j in range(curseur+1,len(liste)): # On cherche le minimum dans la partie droite du curseur
            if liste[j]<minimum:
                minimum=liste[j]
                indice_minimum=j
        #maintenant qu'on connait le minimum, on le met à sa place en l'échangeant
        liste[curseur],liste[indice_minimum]=liste[indice_minimum],liste[curseur]
    return liste   
