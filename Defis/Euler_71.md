# Fractions ordonnées
`Difficulté : Facile (10%)`
`Origine : Projet Euler n°71`

Considérons la fraction n/d où n et d sont des entiers strictement positifs. Si n<d et PGCD(n,d)=1, on dit que la fraction est réduite et propre.

Si on liste la liste des fractions réduites et propres pour d ≤ 8 dans l'ordre croissant, on obtient :

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

On peut voir que 2/5 est la fraction immediatement à gauche de 3/7.

En listant toutes les fractions réduites et propres pour d ≤ 1 000 000 dans l'ordre croissant, trouver le numérateur de la fraction immediatement à gauche de 3/7.

On affichera le résultat avec `print`.

@[Fractions ordonnées]({"stubs": ["Defis/Euler_71.py"], "command": "python3 Defis/Euler_71_Test.py"})

---

# Décompte du nombre de fractions dans un intervalle
`Difficulté : Moyen (20%)`
`Origine : Projet Euler n°72`

Considérons la fraction n/d où n et d sont des entiers strictement positifs. Si n<d et PGCD(n,d)=1, on dit que la fraction est réduite et propre.

Si on liste la liste des fractions réduites et propres pour d ≤ 8 dans l'ordre croissant, on obtient :

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

On peut voir qu'il y a 21 fractions dans cette liste.

Combien d'éléments contiendra la liste des fractions réduites et propres pour d ≤ 1,000,000 ?

On affichera le résultat avec `print`.

@[Décompte du nombre de fractions dans un intervalle]({"stubs": ["Defis/Euler_72.py"], "command": "python3 Defis/Euler_72_Test.py"})

---

# Décompte du nombre de fractions dans un intervalle
`Difficulté : Moyen (15%)`
`Origine : Projet Euler n°73`

Considérons la fraction n/d où n et d sont des entiers strictement positifs. Si n<d et PGCD(n,d)=1, on dit que la fraction est réduite et propre.

Si on liste la liste des fractions réduites et propres pour d ≤ 8 dans l'ordre croissant, on obtient :

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

On peut voir qu'il y a 3 fractions entre 1/3 et 1/2.

Combien de fractions sont comprises entre 1/3 et 1/2 dans la liste des fractions réduites et propres pour d ≤ 12 000 ?

On affichera le résultat avec `print`.

@[Décompte du nombre de fractions dans un intervalle]({"stubs": ["Defis/Euler_73.py"], "command": "python3 Defis/Euler_73_Test.py"})

---

# Chaine de factorielle de chiffres
`Difficulté : Moyen (15%)`
`Origine : Projet Euler n°74`

Le nombre 145 est bien connu pour avoir la propriété que la somme des factorielles de ses chiffres est égale à 145 :

1! + 4! + 5! = 1 + 24 + 120 = 145

Il est cependant moins connu que 169 produit une chaine de nombre qui revient sur 169. Il s'avère qu'il y a seulement 3 telles boucles qui existent : 

169 → 363601 → 1454 → 169  
871 → 45361 → 871  
872 → 45362 → 872  

Il n'est pas difficile de montre que pour chaque nombre de départ sera bloqué dans une boucle. Par exemple :

69 → 363600 → 1454 → 169 → 363601 (→ 1454)  
78 → 45360 → 871 → 45361 (→ 871)  
540 → 145 (→ 145)  

En partant de 69, on crée une chaine de 5 termes distincts. La chaine la plus longue de nombres distincts avec un nombre de départ inférieur à un million est de 60 termes.

Combien de chaines de 60 termes exactement existe-t-il en commençant avec un nombre inférieur à un million ?

On affichera le résultat avec `print`.

@[Chaine de factorielle de chiffres]({"stubs": ["Defis/Euler_74.py"], "command": "python3 Defis/Euler_74_Test.py"})

---

# Périmètre singulier de triangles rectangles entiers
`Difficulté : Moyen (25%)`
`Origine : Projet Euler n°75`

Il s'avère que 12 cm est la plus petite longueur de corde telle qu'on peut former un triangle rectangle dont la longueur des cotés est un entier et d'une unique façon. Voici d'autres exemples : 

12 cm: (3,4,5)  
24 cm: (6,8,10)  
30 cm: (5,12,13)  
36 cm: (9,12,15)  
40 cm: (8,15,17)  
48 cm: (12,16,20)  

A l'opposé, certaines longueurs de cordes, comme 20 cm ne peuvent pas être utilisées pour former un triangle rectangle de cotés entiers. D'un autre coté, certaines longueurs ont plusieurs possibilités pour former un triangle rectangle de cotés entiers comme par exemple 120 cm avec laquelle on peut former 3 triangles différents :

120 cm: (30,40,50), (20,48,52), (24,45,51)

Etant donnée une longueur L de corde, pour combien de valeurs de L ≤ 1,500,000 peut-on former exactement un seul triangle rectangle de cotés entiers ? 

On affichera le résultat avec `print`.

@[Périmètre singulier de triangles rectangles entiers]({"stubs": ["Defis/Euler_75.py"], "command": "python3 Defis/Euler_75_Test.py"})

---
