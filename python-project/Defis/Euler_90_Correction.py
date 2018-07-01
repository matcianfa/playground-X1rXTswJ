# Méthode bourrin : On regarde toutes les combinaisons possibles et on ne garde que celles qui fonctionnent

# Fonction qui liste les combinaisons de k elements dans un ensemble
from itertools import combinations

liste_combinaisons=[c for c in combinations(list(range(9))+[6],6)] #On remplace le 9 par un 6

carrés = [(0,1),(0,4),(0,6),(1,6),(2,5),(3,6),(4,6),(8,1)] # 49 et 64 sont représentés pareil avec les conditions de l'énoncé

# Fonction qui vérifie si une paire de dés est valide
# Pour cela on vérifie simplement si les deux chiffres de tous les carrés sont dans les faces  des dés
def est_valide(d1,d2):
    return all([(chiffre1 in d1 and chiffre2 in d2) or (chiffre1 in d2 and chiffre2 in d1) for chiffre1,chiffre2 in carrés])
    
somme=0
for (d1,d2) in combinations(liste_combinaisons,2):
    if est_valide(d1,d2):
        somme+=1
        
print(somme)
