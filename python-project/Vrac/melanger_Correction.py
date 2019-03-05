from random import randint

def mélanger(liste):
    for i in range(len(liste)-1,0,-1):
        k=randint(0,i)
        liste[k],liste[i]=liste[i],liste[k]
    return liste
    
   
