# Exercices de niveau Première

Voici des exercices sur les variables et les fonctions mathématiques qui nécessitent des notions du programme de Première.


# Calcul du produit scalaire
`Difficulté : Très facile`  
`Notion : Produit scalaire`

Le but de cet exercice est de créer un programme qui calcul de produit scalaire de deux vecteurs $`\vec u_1 (x1,y1)`$ et $`\vec u_2 (x2,y2)`$

>Entrée : Les coordonnées $`\vec u_1 (x_1,y_1)`$ et $`\vec u_2 (x_2,y_2)`$ des deux vecteurs

>Sortie : Le produit scalaire $`\vec u_1 .\vec u_2 =x_1.x_2+y_1.y_2`$.

@[Calcul du produit scalaire]({"stubs": ["Variables_et_fonctions/Calcul_du_produit_scalaire.py"], "command": "python3 Variables_et_fonctions/Calcul_du_produit_scalaire_Test.py"})

---

# Somme de termes d'une suite
`Difficulté informatique : Très facile`  
`Difficulté mathématique : Facile`  
`Notion : Suites`  
`Origine :` [`Hackerrank`](https://www.hackerrank.com/challenges/summing-the-n-series/problem)

On pose $`T_n = n^2 - (n-1)^2`$ ainsi que $`S_n = T_1+ T_2 + T_3+... + T_n`$.

Etant donné ***n***, afficher la valeur de $`S_n`$.

> Entrée : La valeur de l'entier naturel non nul ***n***.

> Sortie : La valeur de $`S_n`$.

@[Somme de termes d'une suite]({"stubs": ["Variables_et_fonctions/Somme_telescopique.py"], "command": "python3 Variables_et_fonctions/Somme_telescopique_Test.py"})

---

# Passage des coordonnées polaires à cartésiennes
`Difficulté : Facile`  
`Notion : Angles en radians`

Pour étudier le mouvement d'un objet (une planète par exemple), il est parfois plus pratique de repérer cet objet par ses coordonnées polaires.
On pourra trouver une présentation de ce système de coordonnées  ainsi que des indications pour la suite sur cette page [Wikipédia](https://fr.wikipedia.org/wiki/Coordonn%C3%A9es_polaires)

Le but de cet exercice est de créer un programme qui traduit les coordonnées polaires en coordonnées cartésiennes.

+ Pour cela, voici les formules de passage des coordonnées polaires $`(r,\theta)`$ aux coordonnées cartésiennes $`(x,y)`$ :

$`\left\{\begin{array}{l} x= r.cos (\theta) \\ y= r.sin (\theta)\end{array}\right.`$


+ Je rappelle que le cosinus et sinus en Python sont en radians. Pour les tests, les angles seront donnés en degrés ce qui signifie  qu'il faudra les transformer en radians.

+ De plus, les résultats devront être arrondis à 3 chiffres après la virgule. Pour cela, on utilisera la fonction `round( nombre , nombre_de_chiffres_après_la_virgule)`.
+ Enfin, les résultats ***x*** et ***y*** devront être affiché d'affilée, simplement séparés d'un espace. Pour cela, on utilisera simplement la syntaxe `print(x,y)`

>Entrée : Les valeurs de $`r`$ et $`\theta`$ (en degrés).

>Sortie : Les coordonnées cartésiennes ***x*** et ***y*** correspondants aux coordonnées polaires données en entrée.

@[Passage des coordonnées polaires à cartésiennes]({"stubs": ["Variables_et_fonctions/Passage_polaires_cartesiennes.py"], "command": "python3 Variables_et_fonctions/Passage_polaires_cartesiennes_Test.py"})

---

# Calcul de distances à vol d'oiseau
`Difficulté : Facile`  
`Notion : Angles en radians`

Lorsqu'on regarde une carte de la Terre et que l'on souhaite aller d'un point à un autre, le plus court chemin n'est pas forcément la ligne droite sur la carte. De manière naturelle, cette plus courte distance est la distance à vol d'oiseau (ce plus court chemin s'appelle aussi l'orthodromie). Pour plus d'explication, vous pouvez aller voir [Wikipédia](https://fr.wikipedia.org/wiki/Orthodromie)

Le but de cet exercice est de calculer la distance à vol d'oiseau entre deux endroits A et B dont on connait la latitude et longitude (que l'on obtient facilement [ici](https://www.coordonnees-gps.fr/) par exemple). 

Pour cela, on utilisera la formule suivante, valable pour des petites distances par rapport au rayon de la terre : 
1. $`x=(longitude_B-longitude_A).cos\left(\frac{latitude_A+latitude_B}{2}\right)`$
2. $`y=latitude_B-latitude_A`$
3. $` distance = rayon.\sqrt{x^2+y^2}`$


+ On prendra pour le rayon de la Terre la valeur 6 371 km
+ On fera bien attention au fait que les latitudes et longitudes dans ces formules doivent être en radians alors que celles qu'on a en entrée seront en degrés. On n'oubliera donc pas de passer des degrés aux radians.
+ De plus, les résultats devront être arrondis au mètre près. Pour cela, on utilisera la fonction `round( nombre , nombre_de_chiffres_après_la_virgule)`.

> Entrée : Les latitudes et longitudes des deux points en degrés.

> Sortie : La distance à vol d'oiseau entre ces deux points, arrondie au mètre près.

@[Calcul de distances à vol d'oiseau]({"stubs": ["Variables_et_fonctions/Calcul_distance_vol_oiseau.py"], "command": "python3 Variables_et_fonctions/Calcul_distance_vol_oiseau_Test.py"})


### Pour aller plus loin :

Vous pouvez tester votre programme avec vos propres valeurs. Pour cela, il suffit de récupérer les latitudes et longitudes des lieux sur ce site : [www.coordonnees-gps.fr](https://www.coordonnees-gps.fr/).

Puis tout en bas de votre programme et sans indentation il suffit de taper `mon_programme(latitude_A, longitude_A,latitude_B,longitude_B)`en remplaçant latitude_A, longitude_A, latitude_B et longitude_B par vos valeurs.


