# Création de la liste des nombres abondants inférieurs à 28123. On utilise une fonction pour gagner en rapidité
def créer_liste_abondants():
    liste=[]
    for n in range(12,28112):#On retire 12 car le second nombre à ajouter vaut au moins 12
        somme=0
        d=1
        while d*d<=n: #Pour accélérer, on s'arrete de chercher à racine de n et on ajoute directement d et n//d à chaque diviseur d trouvé
            if n%d==0:
                somme+=d
                if d!=1 and d*d!=n:
                    somme+= n//d
            d+=1
        if n<somme:
            liste.append(n)
    return liste

liste_abondants=créer_liste_abondants()

# On teste toutes les sommes de deux nombres abondants et on retire à la liste des nombres entre 1 et 28123
nombres_restants=set(range(1,28124)) #Je passe par les ensembles pour gagner du temps et pouvoir utiliser .discard
for a in liste_abondants:
    for b in liste_abondants:
        if b>a or a+b > 28123: break # Pour des raisons de symétrie, on ne cherche que pour les b<=a et c'est inutile de chercher au dessus de 28123.
        nombres_restants.discard(a+b)
print(sum(nombres_restants))
