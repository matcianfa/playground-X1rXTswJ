# Classe de Seconde - Début d'année

Cette page est un peu particulière, elle regroupe des exercices demandant une programmation en python utilisant des notions de seconde en python mais un niveau troisième maximum en mathématique. 


## Exercice n° : Prix total
`Difficulté : Très facile`

Léa va régulièrement acheter toujours les mêmes bonbons : des fraises à 0.04 euros l'unité et des réglisses à 0.07 euros l'unité.  
Créer un programme qui donne le prix total payé par Léa en fonction du nombre ***a*** de fraises et ***b*** de réglisses achetés.

> Entrée : Le nombre ***a*** de fraises et ***b*** de réglisses achetés.

> Sorties : le prix payé par Léa.

@[Ticket de caisse]({"stubs": ["Variables_et_fonctions/Bonbons.py"], "command": "python3 Variables_et_fonctions/Bonbons_Test.py"})

---

# Exercice n° : Périmètre et aire d'un polygone régulier
`Difficulté : Facile`

Le but de cet exercice est de créer un programme qui, pour un nombre ***n***, donne le périmètre et l'aire du polygone régulier convexe à ***n*** côtés inscrit dans un cercle de rayon 1.
On peut aller voir sur cette page pour plus de détails : [Wikipédia](https://fr.wikipedia.org/wiki/Polygone_r%C3%A9gulier#Polygones_r%C3%A9guliers_convexes)

Entre autre, on a les propriétés suivantes :
1. la longueur d'un côté  du polygone est : $`coté=2\sin\left(\frac{\pi}{n}\right)`$
2. l'aire est donnée par la formule : $`aire = \dfrac{périmètre \times \cos\left(\frac{\pi}{n}\right)}2`$

+ De plus, les résultats devront être arrondis à 2 chiffres après la virgule. Pour cela, on utilisera la fonction `round( nombre , nombre_de_chiffres_après_la_virgule)`.
+ Enfin, les résultats ***x*** et ***y*** devront être affiché d'affilée, simplement séparés d'un espace. Pour cela, on utilisera simplement la syntaxe `print(x,y)`

> Entrée : Le nombre ***n*** de cotés du polygone.

> Sortie : Les valeurs du périmètre et de l'aire du polygone régulier convexe à ***n*** cotés, séparées par un espace.

@[Périmètre et aire d'un polygone régulier]({"stubs": ["Variables_et_fonctions/Perimetre_et_aire_polygone_regulier.py"], "command": "python3 Variables_et_fonctions/Perimetre_et_aire_polygone_regulier_Test.py"})

---

## Exercice n° : Coefficient directeur d'une droite (AB)
`Difficulté : Très facile`  

Créer une fonction qui prend en entrée les valeurs xA, yA, xB et yB et renvoie en sortie le coefficient directeur de la droite (AB) avec A et B de coordonnées respectives (xA,yA) et (xB,yB).

> Exemple : `ma_fonction(1,2,3,8)` doit renvoyer `3` car le coefficient directeur de la droite (AB) où A(1,2) et B(3,8) vaut $`\dfrac{8-2}{3-1} = 3`$.

> Remarque : On ne s'occupera pas du cas où la droite pourrait être verticale.

@[Calcul du coefficient directeur]({"stubs": ["Seconde/Debut/coeff_dir.py"], "command": "python3 Seconde/Debut/coeff_dir_Test.py"})

---


