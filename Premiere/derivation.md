# Première : Analyse : Dérivation, études de fonctions, exponentielle et fonctions trigonométriques

## Exercice n° : Taux d'accroissement
`Difficulté : Facile`  

Ecrire une fonction qui prend en entrée une fonction $`f`$ et des réels $`a`$ et $`h`$ et donne en sortie le taux de variation (ou d'accroissement) de la fonction $`f`$ entre le point d'abscisse $`a+h`$ et $`a`$.

@[Taux d'accroissement]({"stubs": ["Premiere/Derivation/taux_accroissement.py"], "command": "python3 Premiere/Derivation/taux_accroissement_Test.py"})

---

## Exercice n° : Ecrire la liste des coefficients directeurs des sécantes pour un pas donné
`Difficulté : Moyenne`  
`Prérequis : Les listes`  
`Programme officiel`

On considère $`\mathcal{C}`$ la courbe représentative d'une fonction $`f`$ dans un repère, $`A`$ un point d'abscisse $`a`$ de $`\mathcal{C}`$ et $`B`$ celui d'abscisse $`a+h`$. 

![Sécantes](secantes.jpg)

Compléter la fonction ci-dessous pour qu'elle permette de calculer la liste des coefficients directeurs des sécantes (ou cordes) (AB) pour h variant de 1 à 0 avec un pas de 0,01. 

@[la liste des coefficients directeurs des sécantes pour un pas donné]({"stubs": ["Premiere/Derivation/liste_coeff.py"], "command": "python3 Premiere/Derivation/liste_coeff_Test.py"})

---

## Exercice n° : Donner la mesure principale d'un angle 
`Difficulté : Moyenne`

Créer une fonction qui prend en entrée un angle en radian et donne en sortie la mesure principale ( dans $`]-\pi; \pi]`$) de cet angle.

@[Mesure principale d'un angle]({"stubs": ["Premiere/Derivation/mesure_principale.py"], "command": "python3 Premiere/Derivation/mesure_principale_Test.py"})

---

## Exercice n° : Donner la mesure principale d'un angle (version améliorée I)
`Difficulté : Moyenne`

La version précédente donne une valeur approchée de la mesure principale. C'est pratique pour vérifier si le calcul qu'on a fait est juste mais ne nous donne pas la réponse comme on souhaiterait l'écrire sur notre feuille (c'est à dire de la forme $`\dfrac{3\pi}{5}`$ au lieu de 1.8849555921538759 par exemple).

Pour améliorer un peu cela, il suffit de travailler avec le nombre qui multiplie $`\pi`$ au lieu de travailler avec l'angle en entier. Une façon de voir les choses est de considérer $`\pi`$ comme une unité.

> Exemple : si on cherche la mesure principale de $`\dfrac{13\pi}{4}`$, on considère le nombre $`\dfrac{13}{4}`$, on lui retire autant de 2 que nécessaire pour être en -1 et 1. On trouve ici $`dfrac{1}{4}`$.

Donc si on part d'un angle quelconque, il faut d'abord le diviser par $`\pi`$ puis retirer ou ajouter autant de 2 que necessaire au résultat pour être entre -1 et 1. On aura juste à afficher $`\pi`$ derrière pour avoir la mesure principale.

Créer une fonction qui prend en entrée un angle et donne en sortie la mesure principale sous la forme $`nombre\pi`$

> Exemple : Si l'angle donné en entrée est $`\dfrac{7\pi}2`$ (c'est à dire 10.995574287564276) alors en sorti, il devra afficher "-0.5pi"

@[Mesure principale d'un angle]({"stubs": ["Premiere/Derivation/mesure_principale2.py"], "command": "python3 Premiere/Derivation/mesure_principale2_Test.py"})

---

## Exercice n° : Donner la mesure principale d'un angle (version améliorée II)
`Difficulté : Difficile`

Reprenons la version précédente et tentons de l'améliorer encore un peu. On obtient dans la version précédente des résultats sous la forme "0.3333333333333333pi" mais on aimerait bien avoir plutôt "(1/3)pi". C'est ce que nous allons essayer de faire.

Pour cela, nous allons utiliser le module `fractions` et plus précisément la fonction `Fraction` de ce module qui va permettre de traduire un nombre décimal en fraction. Malheureusement si on tape directement `str(Fraction(0.333333333333))` on n'obtient pas "1/3". Pour cela il faudra taper `str(Fraction(0.333333333333).limit_denominator())`.

En utilisant `str(Fraction(nombre).limit_denominator())` du module `fractions`, créer une fonction qui donne la mesure principale d'un angle sous la forme "(fraction)pi".

> Exemple :  Si l'angle donné en entrée est $`\dfrac{7\pi}2`$ (c'est à dire 10.995574287564276) alors en sorti, il devra afficher "(-1/2)pi"

@[Mesure principale d'un angle]({"stubs": ["Premiere/Derivation/mesure_principale3.py"], "command": "python3 Premiere/Derivation/mesure_principale3_Test.py"})

---

## Exercice n° : Passage des coordonnées polaires à cartésiennes
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

## Exercice n° : Calcul de distances à vol d'oiseau
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


# Pour aller plus loin 

Voici quelques approfondissements possibles :
- [Recherche de solutions par dichotomie](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/la-recherche-par-dichotomie)
- [La méthode d'Euler](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/la-methode-deuler)
- [La méthode de Newton](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/la-methode-de-newton)
- [La méthode d'Archimède](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/methode-darchimede)
