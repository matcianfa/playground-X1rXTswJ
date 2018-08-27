# Exercices de niveau seconde ou moins

Voici des exercices sur le chapitre Variables et fonctions mathématiques qui nécessitent un niveau de Seconde au maximum en mathématique.

# Symétrie centrale
`Difficulté : Très facile`
`Notion : Symétrie centrale, Vecteurs`

A partir de deux points P et Q, on peut créer un troisième point R symétrique de P par rapport à Q comme sur la figure ci-dessous :
![figure symetrie](https://s3.amazonaws.com/hr-challenge-images/128/1476207535-debed1b871-find-point-1122.png)

Le but de cet exercice est de créer un programme qui prend en entrée les coordonnées de P et Q et affiche les coordonnées de R.

> Entrée : Les coordonnées ***x_p***, ***y_p***, ***x_q*** et ***y_q*** de P et Q.

> Sortie : Les coordonnées du symétrique R de P par rapport à Q. On affichera les résultats d'affilée, simplement séparés d'un espace. Pour cela, on utilisera simplement la syntaxe `print(x,y)`

@[Symétrie centrale]({"stubs": ["Variables_et_fonctions/Symetrie_centrale.py"], "command": "python3 Variables_et_fonctions/Symetrie_centrale_Test.py"})

---

# Périmètre et aire d'un polygone régulier
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
