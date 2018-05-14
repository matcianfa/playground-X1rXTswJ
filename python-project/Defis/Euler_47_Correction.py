#  Ressortons de notre boite à outils la fonction qui permet de savoir si un nombre est premier
def est_premier(n):
    if n < 2 or n%2==0: return False
    for x in range(3, int(n**0.5) + 1,2):
        if n % x == 0:
            return False
    return True


# Créons une liste des nombres premiers qu'on complétera au fur et à mesure 
liste_premiers=[2]

# Créons une fonction qui dit si le nombre donnée en entrée a exactement 4 facteurs premiers distincts
def quatre_facteurs_premiers(n):
    nb_facteurs_premiers=0
    for p in liste_premiers:
        if p>n or nb_facteurs_premiers>4 : break
        if n%p==0 : 
            while n%p==0:
                n//=p
            nb_facteurs_premiers+=1
    return nb_facteurs_premiers==4
    


# Cherchons les 4 entiers consécutifs (On utilise une fonction pour aller plus vite)
def chercher():
    n=3
    bool_1=bool_2=bool_3=bool_4=False # Pour garder en mémoire les résultats (s'ils ont 4 diviseurs premiers) des n précédents
    while 1:
        if est_premier(n) : # On complete la liste des nombres premiers au fur et à mesure
            liste_premiers.append(n)
        bool_4 = quatre_facteurs_premiers(n)
        if bool_1 and bool_2 and bool_3 and bool_4 : # Si les 4 nombres consécutifs ont exactement 4 diviseurs 
            return n-3
        else : 
            bool_1,bool_2,bool_3=bool_2,bool_3,bool_4 # On décale
        n+=1

        
print(chercher())

