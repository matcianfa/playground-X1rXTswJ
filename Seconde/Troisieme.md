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

## Exercice n° : Afficher si un nombre est pair
`Difficulté : Très facile`  
`Notion utilisée : Condition`

Faire un programme qui affiche si un nombre est pair ou impair.

::: Aide
Pour vérifier si un entier ***n*** est divisible par un entier ***k***, il suffit de vérifier si son reste par la division euclidienne par ***k*** est nul ou pas autrement dit si `n%k==0`.
:::

> Entrée : Un nombre entier ***n***

> Sortie : "PAIR" ou "IMPAIR". (N'oubliez pas les guillemets)

@[Parité d'un nombre]({"stubs": ["Les_conditions/nombre_pair.py"], "command": "python3 Les_conditions/nombre_pair_Test.py"})

---

## Exercice n° : Numéro de sécurité sociale
`Difficulté : Facile`  
`Notion utilisée : Condition`

Le numéro de sécurité social est composé de 13 chiffres suivis d'une clé de 2 chiffres. On pourra lire pour plus de détail sur la signification des 13 premiers chiffres par exemple sur [Wikipédia](https://fr.wikipedia.org/wiki/Num%C3%A9ro_de_s%C3%A9curit%C3%A9_sociale_en_France)

Nous allons nous intéresser à la clé car elle permet de vérifier si il n'y a pas eu d'erreur en reportant le numéro sur un formulaire ou lors du transfert informatique par exemple. Voici comment est calculée la clé : 
1. On prend le nombre composé des 13 premiers chiffres du numéro de sécurité sociale et on calcule le reste de sa division euclidienne par 97.
2. On soustrait alors ce reste à 97. Le résultat est la clé. 

Exemple : si le numéro est 9700000000100 alors le reste de la division euclidienne par 97 est 3. La clé est alors 97-3=94. 

:::Rappel sur la division euclidienne
Pour obtenir le quotient de la division euclidienne de n par d, on tape `n//d`.

Pour obtenir le reste de la division euclidienne de n par d, on tape `n%d`.
:::

Le but est de créer un programme qui prend en entrée le ***numéro*** de sécurité sociale et la ***clé*** et qui affiche "VALIDE" si la ***clé*** correspond au ***numéro*** et "NON VALIDE" sinon.

> Entrée : Le ***numéro*** et la ***clé***

> Sortie : "VALIDE" si la ***clé*** correspond au ***numéro*** et "NON VALIDE" sinon. N'oubliez pas les guillemets.


@[Validité du numéro de sécurité sociale]({"stubs": ["Les_conditions/Numero_securite_sociale.py"], "command": "python3 Les_conditions/Numero_securite_sociale_Test.py"})

---

## Exercice n° : Conversion degré Celsius <-> degré Fahrenheit
`Difficulté : Facile`
`Notion utilisée : Condition`

Écrire un programme qui convertit les degrés Celsius en degré Fahrenheit et inversement.

Pour les formules, on regardera [Wikipédia](https://fr.wikipedia.org/wiki/Degr%C3%A9_Fahrenheit)

> Entrée : Une température ***t*** et un nombre ***n***. 
> + Si ***n*** vaut 0, ***t*** est en degré Celsius et il faut la convertir en degré Fahrenheit. 
> + Si ***n*** vaut 1, ***t*** est en degré Fahrenheit et il faut la convertir en degré Celsius.

> Sortie : La température convertie, arrondie à 3 chiffres après la virgule.

@[Conversion Celsius/Fahrenheit]({"stubs": ["Les_conditions/Conversion_Celsius_Fahrenheit.py"], "command": "python3 Les_conditions/Conversion_Celsius_Fahrenheit_Test.py"})

---

## Exercice n° : Dire si un triangle est rectangle I
`Difficulté : Très facile`  
`Notion utilisée :  Condition`

Faire un programme qui affiche si un triangle dont on donne les angles est rectangle ou pas.

> Entrée : Les trois angles ***a***, ***b*** et ***c*** en degrés.

> Sortie : "RECTANGLE" si le triangle est rectangle, "PAS RECTANGLE" sinon. N'oubliez pas les guillemets.

@[Triangle rectangle ? Cas 1]({"stubs": ["Les_conditions/Triangle_rectangle_0.py"], "command": "python3 Les_conditions/Triangle_rectangle_0_Test.py"})

---

## Exercice n° : Dire si un triangle est rectangle II
`Difficulté : Très facile`  
`Notion utilisée :  Condition`

Faire un programme qui affiche si un triangle dont on donne les longueurs est rectangle ou pas.

> Entrée : Les trois longueurs ***a***, ***b*** et ***c*** du triangle.

> Sortie : "RECTANGLE" si le triangle est rectangle, "PAS RECTANGLE" sinon. N'oubliez pas les guillemets.

@[Triangle rectangle ? Cas 2]({"stubs": ["Les_conditions/Triangle_rectangle_1.py"], "command": "python3 Les_conditions/Triangle_rectangle_1_Test.py"})

---

## Exercice n° : Triangles constructibles
`Difficulté : Facile à moyen`  
`Notion utilisée :  Condition`

Si on choisit 3 nombres, il n'est pas toujours possible de construire un triangle ayant pour longueur ces nombres.
Par exemple, il est impossible de construire un triangle de côtés de longueurs 1, 1 et 5. 

Un triangle est constructible si pour chaque coté, sa longueur est inférieur à la somme des longueurs deux autres cotés.

Le but de cet exercice est de créer un programme qui nous dit si le triangle est constructible ou pas à partir des longueurs qui nous sont données.

> Entrée : Trois longueurs ***a***, ***b*** et ***c***.

> Sortie : Affiche "CONSTRUCTIBLE" si on peut construire un triangle ayant des cotés de ces trois longueurs ou bien "PAS CONSTRUCTIBLE" sinon. N'oubliez pas les guillemets.  
> Pour les plus rapides, vous pouvez afficher "PLAT" si le triangle qu'on peut construire est plat. 

@[Triangles constructibles ?]({"stubs": ["Les_conditions/Triangles_constructibles.py"], "command": "python3 Les_conditions/Triangles_constructibles_Test.py"})

---

## Donner la nature d'un triangle
`Difficulté : Difficile`  
`Notion utilisée :  Condition`

Le but de cet exercice est de faire un programme qui donne la nature d'un triangle c'est à dire s'il est rectangle, isocèle, équilatéral ou rectangle isocèle à partir des longueurs données. Dans les autres cas, on dira qu'il est quelconque.

Pour les plus rapides, pour passer les derniers tests, il faut de plus vérifier si le triangle est un triangle d'or. On pourra trouver des informations sur [Wikipédia](https://fr.wikipedia.org/wiki/Triangle_d%27or_(g%C3%A9om%C3%A9trie))

::: Indications  
Voici plusieurs points qui peuvent faire que votre programme ne marche pas:
+ Reflechissez bien à l'ordre de vos conditions. Par exemple en pseudo code :
```
    Si le triangle est isocèle
        afficher("ISOCELE")
    Sinon si le triangle est équilateral
        afficher("EQUILATERAL")
```
Ce code affichera "ISOCELE" pour un triangle equilatéral car la condition isocèle sera vérifiée avant et donc le programme n'ira pas jusqu'à la condition équilatérale.
+ Pensez à bien vérifier pour les 3 sommets une condition du type "être rectangle" ou "isocèle".
+ Attention aux problèmes d'arrondis avec Python. Je rappelle qu'en Python, $`\sqrt{2}^2=2.0000000000000004 `$ ! Donc pour vérifier des égalités comme celle de Pythagore, il vaut mieux vérifier si `c**2-a**2-b**2` une fois arrondi (à 10 chiffres après la virgule par exemple) vaut 0 plutôt que directement.
:::

> Entrée : Les trois longueurs ***a***, ***b*** et ***c*** du triangle.

> Sortie : Les propriétés du triangle parmi : "RECTANGLE", "RECTANGLE ISOCELE", "ISOCELE", "EQUILATERAL", "QUELCONQUE" (et pour les plus rapide : "TRIANGLE D'OR"). N'oubliez pas les guillemets.

@[Nature d'un triangle]({"stubs": ["Les_conditions/Nature_d_un_triangle.py"], "command": "python3 Les_conditions/Nature_d_un_triangle_Test.py"})

---

