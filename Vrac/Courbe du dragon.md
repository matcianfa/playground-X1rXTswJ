# La courbe du dragon
`Difficulté : Moyenne à difficile`

On a déjà parlé de la courbe des pliages d'un papier dans un exercice. Pour rappel : 

Si l'on prend une bande de papier que l'on plie en deux, toujours dans le même sens (à gauche par exemple), la forme résultante présente une suite de changements de direction que l'on peut coder par G pour gauche et D pour droite. 
On obtient alors la suite : 
1. G 
2. G G D 
3. G G D G G D D
4. G G D G G D D G G G D D G D D 
5. ... 

Cette suite de lettre s'appelle la suite des pliages d'un papier et si on la représente, on obtient la courbe du dragon. Vous pouvez regarder sur [Wikipédia](https://fr.wikipedia.org/wiki/Suite_de_pliage_de_papier) pour plus d'informations et de [belles images](https://fr.wikipedia.org/wiki/Courbe_du_dragon). 

Le but de cet exercice est de représenter cette courbe.

### Première étape : La suite des pliages d'un papier.

On a déjà vu des manières de construire cette suite mais qui ne sont pas très efficaces si on veut la suite pour un nombre de pliage grand (car il fallait calculer à chaque fois les pliages en partant du début).

Pour obtenir le ***k***-ième terme de cette suite (attention : on commence à k=1 ici, autrement dit le 3ieme terme est D.), voici ce qu'il faut faire :
+ Mettre ***k*** sous la forme $`k=m2^p`$ où ***m*** est un nombre impair. On a déjà fait un exercice la dessus, s'y reporter si besoin.
+ Si `m%4==1` alors le ***k***-ième terme est un 'G' sinon c'est un 'D'.

Créer une programme ***pliage*** qui prend un entier ***k*** en entrée et affiche le ***k***-ième terme de la suite des pliages d'un papier (en commençant par un 'G' si ***k***=1).

> Entrée : Un entier non nul ***k***.
  
> Sortie : La ***k***-ème lettre de la suite des pliages d'un papier donc un "G" ou un "D" renvoyée avec `return`.
  
@[k-ième lettre de la suite des pliages d'un papier]({"stubs": ["Vrac/courbe_dragon.py"], "command": "python3 Vrac/courbe_dragon_Test.py"})
  
---
  

