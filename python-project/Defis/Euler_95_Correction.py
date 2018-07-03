# Méthode naturelle, rien d'original sur l'idée


N_max=10**6
# On met dans une liste la somme des diviseurs des nombres inférieurs à  un million en faisant un crible d'Erathostene. Cela évite les fastidieux calculs de decompositions en nombres premiers
liste_somme_diviseurs=[0]+[1]*N_max

for i in range(2,N_max//2+1):
    for k in range(2,N_max//i +1):
        liste_somme_diviseurs[k*i]+=i
        

# Fonction qui cherche
# Pour cela on parcourt notre liste_somme_diviseurs. 
# si C'est un 1 on passe
# Sinon on enchaine les diviseurs en les sauvegardant dans une liste. Si à un moment on retombe sur un élément qui est déjà tombé, on a une chaine (en ne considérant que les derniers). Comme ca ne sert à rien de reconsidérer les nombres d'une chaine déjà étudiée, on met à 1 les valeurs sur lesquelles on tombe au fur et à mesure.
def chercher():
    long_max=0
    liste_max=[]
    for i in range(2,N_max):
        valeurs=[i]
        val= i
        while val<N_max and val>=2 :
            liste_somme_diviseurs[val] , val = 1 , liste_somme_diviseurs[val] # Echange simultané
            try : # Pour éviter les conditions couteuse val in valeurs
                k = valeurs.index(val)
            except : 
                valeurs.append(val)
            else : # Executé s'il n'y a pas d'exception c'est à dire ici si on a trouvé val dans valeurs autrement dit si on a trouvé une chaine
                if len(valeurs[k:])> long_max :
                    liste_max = valeurs[k:].copy()
                    long_max=len(liste_max)
    return min(liste_max)
    
print(chercher())
