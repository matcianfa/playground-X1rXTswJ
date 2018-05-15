# En raisonnant avec le critère de divisibilité par 3, on peut facilement se convaincre qu'il ne peut pas y avoir 8 nombres premiers obtenus en modifiant 1 seul chiffre ou bien 2 chiffres (ni 4 ou 5 ou 7 ou 8... bref pour tous les nombres non multiples de 3)
# Donc nous allons chercher une solution pour laquelle on modifie 3 chiffres. On commence donc avec des nombres d'au moins 4 chiffres
# On remarque aussi qu'il suffit de chercher ceux avec trois 0 ou trois 1 ou trois 2 car parmi les 8 nombres premiers obtenus par modifications, il y en a forcément un qui aura ces chiffres.

#  Ressortons de notre boite à outils la fonction qui permet de savoir si un nombre est premier
def est_premier(n):
    if n < 2 or n%2==0: return False
    for x in range(3, int(n**0.5) + 1,2):
        if n % x == 0:
            return False
    return True

# Créons une fonction qui donne le nombre premier suivant le nombre impair n donné en entrée :
def premier_suivant(n):
    n+=2
    while not est_premier(n):
        n+=2
    return n

# On met dans une fonction pour aller plus vite
def chercher():
    n=999
    while 1:
        n=premier_suivant(n)
        str_n=str(n)
        for chiffre in "012":
            if str_n.count(chiffre)==3 : # On regarde si le nombre de 0, 1 ou 2 vaut 3. (Par flemme je ne considère pas le cas ou il y en a plus de 3 pour regarder tous les triplets possibles)
                compteur = 1
                for k in range(int(chiffre)+1,10):
                    if est_premier(int(str_n.replace(chiffre,str(k)))): # On regarde si le nombre est premier quand on remplace le chiffre qui est en triple par k
                        compteur+=1
                if compteur>7 : 
                    return n

        
                        
print(chercher())
