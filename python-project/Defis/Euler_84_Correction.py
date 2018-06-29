# L'idée est d'utiliser un graphe probabiliste et plus particulièrement utiliser la matrice associée pour déterminer la probabilité d'être sur une case.

import numpy as np

matrice= np.zeros((40,40))

#liste=[0,0,1,2,3,4,5,6,5,4,3,2,1] # liste pour deux dés de 6
liste=[0,0,1,2,3,4,3,2,1] # liste pour deux dés de 4

# Ajouts des probabilités de tomber sur les cases suivantes dans notre matrice
N=sum(liste)
for depart in range(40):
    for i,val in enumerate(liste):
        matrice[depart,(depart+i)%40]=val/N
        
# Ajoutons les probabilités des cartes communautés
for ligne in range(40):
    for numero in [2,17,33]:
        matrice[ligne,0]+=matrice[ligne,numero]*1/16
        matrice[ligne,10]+=matrice[ligne,numero]*1/16
        matrice[ligne,numero]*=14/16
# Ajoutons les probabilités des cartes chances
for ligne in range(40):
    for numero in [7,22,36]:
        matrice[ligne,0]+=matrice[ligne,numero]*1/16
        matrice[ligne,10]+=matrice[ligne,numero]*1/16
        matrice[ligne,11]+=matrice[ligne,numero]*1/16
        matrice[ligne,24]+=matrice[ligne,numero]*1/16
        matrice[ligne,39]+=matrice[ligne,numero]*1/16
        matrice[ligne,5]+=matrice[ligne,numero]*1/16
        if numero==7 : 
            next_R=15
            next_U=12
        elif numero==22: 
            next_R = 25
            next_U= 28
        else :
            next_R= 5
            next_U=12
        matrice[ligne,next_R]+=matrice[ligne,numero]*2/16
        matrice[ligne,next_U]+=matrice[ligne,numero]*1/16
        if numero==36: # Si on recule de 3 cases et qu'on est en 36, on tombe sur carte communauté qu'il faut donc recalculer
            matrice[ligne,0]+=matrice[ligne,numero]*(1/16)*(1/16)
            matrice[ligne,10]+=matrice[ligne,numero]*(1/16)*(1/16)
            matrice[ligne,33]+=matrice[ligne,numero]*(14/16)*(1/16)
        else :  matrice[ligne,numero-3]+=matrice[ligne,numero]*1/16
        matrice[ligne,numero]*=6/16
        
       
# La case aller en prison
for ligne in range(40):
    matrice[ligne,10]+=matrice[ligne,30]
    matrice[ligne,30]=0
    

I=np.eye(40)

nb_lancers=10**12

#On regarde notre matrice après nb_lancers (Ici mille milliard!) :
A= np.linalg.matrix_power(matrice,nb_lancers)

#☺ Comme on commence à 0, il suffit de lire les probabilités sur la première ligne :
# On crée une liste de couple (proba, numero) qu'on ordonne pour avoir les gagnants
liste_resultats = sorted([(proba,numero) for numero,proba in enumerate([A[0,col] for col in range(40)])],reverse=True)


# Reste à afficher le résultat
reponse=""
for (_,numero) in liste_resultats[:3]:
    reponse+="0"*(numero<10)+str(numero)
print(reponse)
