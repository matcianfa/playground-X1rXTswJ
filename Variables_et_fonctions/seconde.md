# Exercices de niveau Seconde ou moins

Voici des exercices sur le chapitre Variables et fonctions mathématiques qui nécessitent un niveau de Seconde au maximum en mathématique.

# Paires de chaussettes
`Difficulté : Très Facile`  
`Origine :` [`Hackerrank`](https://www.hackerrank.com/challenges/maximum-draws/problem)

Baptiste cherche des chaussettes pour aller à une soirée. Son tiroir est plein de chaussettes, chaque paire est de couleur différente. Pour choisir une chaussette, il met sa main dans le tiroir et ne voit la couleur de la chaussette qu'une fois qu'il l'a sortie du tiroir.

Dans le pire des cas, combien doit-il prendre de chaussettes dans son tiroir pour être sûr d'avoir une paire de la même couleur ?

> Entrée : Le nombre ***n*** de chaussettes dans le tiroir.

> Sortir : Le nombre de chaussettes que Baptiste doit sortir dans le pire des cas du tiroir être sûr d'avoir une paire de la même couleur.

@[Chacun cherche ses chaussettes sèches]({"stubs": ["Variables_et_fonctions/Chaussettes.py"], "command": "python3 Variables_et_fonctions/Chaussettes_Test.py"})

---

# Symétrie centrale
`Difficulté : Très facile`  
`Notions : Symétrie centrale, Vecteurs`  
`Origine :` [`Hackerrank`](https://www.hackerrank.com/challenges/find-point/problem)

A partir de deux points P et Q, on peut créer un troisième point R symétrique de P par rapport à Q comme sur la figure ci-dessous :
![figure symetrie](https://s3.amazonaws.com/hr-challenge-images/128/1476207535-debed1b871-find-point-1122.png)

Le but de cet exercice est de créer un programme qui prend en entrée les coordonnées de P et Q et affiche les coordonnées de R.

> Entrée : Les coordonnées ***x_p***, ***y_p***, ***x_q*** et ***y_q*** de P et Q.

> Sortie : Les coordonnées du symétrique R de P par rapport à Q. On affichera les résultats d'affilée, simplement séparés d'un espace. Pour cela, on utilisera simplement la syntaxe `print(x,y)`

@[Symétrie centrale]({"stubs": ["Variables_et_fonctions/Symetrie_centrale.py"], "command": "python3 Variables_et_fonctions/Symetrie_centrale_Test.py"})

---

# Nombre de bises au nouvel an
`Difficulté : Facile`

Des amis passent le soir du reveillon du nouvel an ensemble. A minuit, chacun embrasse (en faisant deux bises) tous les autres invités.

Combien y a-t-il eu de bises échangées pas les invités pour ce nouvel an ?

> Entrée : Le nombre ***n*** d'invités.

> Sortie : Le nombre de bises échangées pour ce nouvel an.

@[Nombre de bises]({"stubs": ["Variables_et_fonctions/Bises.py"], "command": "python3 Variables_et_fonctions/Bises_Test.py"})

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

# Bases armées
`Difficulté : Facile à moyenne`  
`Notion : Division euclidienne`  
`Origine :` [`Hackerrank`](https://www.hackerrank.com/challenges/game-with-cells/problem)

Luke est dans ses pensées pendant un cours de maths. Sur un papier quadrillé de ***n*** lignes et ***m*** colonnes, il imagine que chaque case est une base armée. Il veut envoyer des fournitures à ses bases à des points stratégiques, en marquant chaque point en rouge. Si une base contient au moins un colis de fourniture dedans ou sur un de ses bords, on qu'onsidère qu'il y a accès. Par exemple : 
![Fournitures](https://s3.amazonaws.com/hr-challenge-images/0/1479944215-79f12638a7-example-army-game.png)

Etant donnés ***n*** et ***m***, quel est le nombre minimum de colis que Luke doit envoyer pour fournir toutes ses bases ?

@[Bases armées]({"stubs": ["Variables_et_fonctions/Bases_armees.py"], "command": "python3 Variables_et_fonctions/Bases_armees_Test.py"})

