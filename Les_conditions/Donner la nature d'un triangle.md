## Donner la nature d'un triangle

Le but de cet exercice est de faire un programme qui donne la nature d'un triangle c'est à dire s'il est rectangle, isocèle, équilatéral ou rectangle isocèle à partir des longueurs données. Dans les autres cas, on dira qu'il est quelconque.

Pour les plus rapides, pour passer les derniers tests, il faut de plus vérifier si le triangle est un triangle d'or. On pourra trouver des informations sur [Wikipédia](https://fr.wikipedia.org/wiki/Triangle_d%27or_(g%C3%A9om%C3%A9trie))

::: Indications  
Voici plusieurs points qui peuvent faire que votre programme ne marche pas:
+ Reflechissez bien à l'ordre de vos conditions. Par exemple en pseudo code :
    Si le triangle est isocèle
        afficher("ISOCELE")
    Sinon si le triangle est equilateral
        afficher("EQUILATERAL")
Ce code affichera "ISOCELE" pour un triangle equilatéral car la condition isocèle sera vérifier avant et donc le programme n'ira pas jusqu'a la condition equilatérale.
+ Pensez à bien vérifier pour les 3 sommets une condition du type être rectangle ou isocèle.
+ Attention aux problèmes d'arrondis avec Python. Je rappelle qu'en Python, $`\sqrt(2)^2=2.0000000000000004 `$ ! Donc pour vérifier des égalités comme celle de Pythagore, il vaut mieux vérifier si `c**2-a**2-b**2` une fois arrondi (à 10 chiffres après la virgule par exemple) vaut 0 plutôt que directement.
:::

> Entrée : Les trois longueurs ***a***, ***b*** et ***c*** du triangle.

> Sortie : Les propriétés du triangle parmi : "RECTANGLE", "RECTANGLE ISOCELE", "ISOCELE", "EQUILATERAL", "QUELCONQUE" (et pour les plus rapide : "TRIANGLE D'OR".

@[Nature d'un triangle]({"stubs": ["Les_conditions/Nature_d_un_triangle.py"], "command": "python3 Les_conditions/Nature_d_un_triangle_Test.py"})
