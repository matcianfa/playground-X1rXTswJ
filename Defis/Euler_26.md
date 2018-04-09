# Cycles récurrents
`Difficulté : Facile`
`Origine : Projet Euler n°26`

Une fraction unitaire possède comme numérateur 1. La représentation décimale des fractions unitaires avec les dénominateurs de 2 à 10 sont :

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

où 0.1(6) signifie 0.166666..., et possède un 1-cycle de chiffres récurrents. On peut montrer que 1/7 possède un 6-cycle de chiffres récurrents.

Trouvez la valeur de d<1000 pour laquelle 1/d possède le cycle de chiffres récurrents le plus long dans sa partie décimale.

On affichera le résultat avec `print`.

@[Cycles récurrents]({"stubs": ["Defis/Euler_26.py"], "command": "python3 Defis/Euler_26_Test.py"})

---

# Nombres premiers quadratiques
`Difficulté : Facile`
`Origine : Projet Euler n°27`

Euler a découvert la formule quadratique remarquable $`n^2 + n+41`$ qui, lorsqu'on prend pour n des valeurs entières de 0 à 39, donne 40 nombres premiers. Cependant, pour n=40, 40²+40+41=40(40+1)+41=41² n'est pas un nombre premier.

Par la suite, on a découvert l'incroyable formule $`n^2-79n+1601`$ qui donne 80 nombres premiers pour les tous les n entre 0 et 79. Le produit des coefficients, -79 et 1601, est -126479.


En considérant des formes quadratiques $`n^2+an+b`$ où |a|<1000 et |b|≤1000, trouver le produit des coefficients a et b qui donnent le nombre maximum de nombres premiers pour des valeurs successives de n qui commencent par n=0.

On affichera le résultat avec `print`.

@[Nombres premiers quadratiques]({"stubs": ["Defis/Euler_27.py"], "command": "python3 Defis/Euler_27_Test.py"})

---

# Nombres sur les diagonales d'une spirale
`Difficulté : Facile`
`Origine : Projet Euler n°28`

En commençant avec le nombre 1 et en tournant dans vers la droite dans le sens des aiguilles d'une montre, on peut former une spirale 5 par 5 comme ceci :

**21** 22 23 24 **25**  
20   **07**   08   **09** 10  
19   06   **01**   02 11  
18   **05**   04   **03** 12  
**17** 16 15 14 **13**  

On peut vérifier que la somme des nombres sur les diagonales est 101.

Quelle est la somme des nombres sur les diagonales d'une spirale 1001 par 1001 construite de la même façon ?

On affichera le résultat avec `print`.

@[Nombres sur les diagonales d'une spirale]({"stubs": ["Defis/Euler_28.py"], "command": "python3 Defis/Euler_28_Test.py"})

---

# Puissances distinctes
`Difficulté : Facile`
`Origine : Projet Euler n°29`

Considérons tous les combinaisons entière $`a^b`$ pour 2 ≤ a ≤ 5 et 2 ≤ b ≤ 5 :

    22=4, 23=8, 24=16, 25=32  
    32=9, 33=27, 34=81, 35=243  
    42=16, 43=64, 44=256, 45=1024  
    52=25, 53=125, 54=625, 55=3125  

Si on les place dans l'ordre croissant, en retirant les répétitions, on obtient la suite des 15 nombres distincts :

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

Combien de nombres distincts obtient-on dans la suite générée par les $`a^b`$ pour 2 ≤ a ≤ 100 et 2 ≤ b ≤ 100 ?

On affichera le résultat avec `print`.

@[Puissances distinctes]({"stubs": ["Defis/Euler_29.py"], "command": "python3 Defis/Euler_29_Test.py"})

---

# Puissances cinquième de chiffres
`Difficulté : Facile`
`Origine : Projet Euler n°30`

Etonnamment, il y a seulement 3 nombres qui peuvent être écrits comme la somme des puissances quatrièmes de leurs chiffres : 

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

Comme $`1 = 1^4`$ n'est pas une somme, il n'est pas inclus.

La somme de ces nombres est 1634 + 8208 + 9474 = 19316.

Trouvez la somme de tous les nombres qui peuvent être écrits comme la somme des puissances cinquièmes de leurs chiffres.

On affichera le résultat avec `print`.

@[Puissances cinquième de chiffres]({"stubs": ["Defis/Euler_30.py"], "command": "python3 Defis/Euler_30_Test.py"})
