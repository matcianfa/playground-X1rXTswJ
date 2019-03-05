from random import randint

#Copiez collez ci-dessous vos fonctions est_triée et mélanger
def est_triée(liste):
    for i in range(len(liste)-1):
        if liste[i]>liste[i+1]:
            return False
    return True

#mélanger
def mélanger(liste):
    for i in range(len(liste)-1,0,-1):
        k=randint(0,i)
        liste[k],liste[i]=liste[i],liste[k]
    return liste



def mon_programme(liste):
    while not est_triée(liste):
        liste=mélanger(liste)
    return liste
