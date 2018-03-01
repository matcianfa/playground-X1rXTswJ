## Suite des pliages d'un papier
`Difficulté : Moyenne`

Si l'on prend une bande de papier que l'on plie en deux, toujours dans le même sens (à gauche par exemple), la forme résultante présente une suite de changements de direction que l'on peut coder par G pour gauche et D pour droite. 
On obtient alors la suite : 
1. G 
2. G G D 
3. G G D G G D D
4. G G D G G D D G G G D D G D D 
5. ... 

Cette suite de lettre s'appelle la suite des pliages d'un papier et si on la représente, on obtient la courbe du dragon. Vous pouvez regarder sur [Wikipédia](https://fr.wikipedia.org/wiki/Suite_de_pliage_de_papier) pour plus d'informations et de [belles images](https://fr.wikipedia.org/wiki/Courbe_du_dragon). 

### Première méthode

Une façon de construire cette suite est de commencer par un G et pour passer d'une ligne de la suite à la suivante, on fait toujours la même chose : 
- On rajoute un G à la fin. 
- On prend les lettres 2 par 2 et 
  + si on a GG on le remplace par GGDG 
  + si on a DG on le remplace par GDDG 
  + si on a GD on le remplace par GGDD 
  + si on a DD on le remplace par GDDD 
- On obtient ainsi un mot 2 fois plus long auquel on retire le dernier G.
C'est notre nouvelle ligne de la suite de pliage de papier. 

Faire un programme qui prend en entrée un nombre ***n*** et affiche la ***n***-ième ligne de la suite des pliages d'un papier.

> Entrée : Un entier ***n***.

> Sortie : Une suite de G et de D (sans espace entre) qui représentent la succession de pliures lorsqu'on plie ***n*** fois un papier.

@[Suite des pliages d'un papier]({"stubs": ["Chaines_caracteres/Pliage_papier.py"], "command": "python3 Chaines_caracteres/Pliage_papier_Test.py"})

---

### Seconde méthode

Une autre façon de construire cette suite est de commencer par un G et pour passer d'une ligne de la suite à la suivante, on fait toujours la même chose : 
- On recopie la ligne précédente. 
- On ajoute un G à la fin 
- On rajoute ensuite la ligne précédente où l'on change tous les G en D et inversement et en plus on renverse l'ordre des lettres (les premières en dernier et inversement) 

Faire un programme qui prend en entrée un nombre ***n*** et affiche la ***n***-ième ligne de la suite de pliage de papier.


> Entrée : Un entier ***n***.

> Sortie : Une suite de G et de D (sans espace entre) qui représentent la succession de pliures lorsqu'on plie ***n*** fois un papier.

@[Suite des pliages d'un papier 2]({"stubs": ["Chaines_caracteres/Pliage_papier2.py"], "command": "python3 Chaines_caracteres/Pliage_papier2_Test.py"})
