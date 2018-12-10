# Jeu de Nim : Variante utilisant la décomposition en base 2 (dite variante de Marienbad)

@[Stratégie gagnante au jeu de nim]({"stubs": ["Autre/Nim0.py","Autre/Nim.py"], "command": "python3 Autre/Nim0.py"})

Cette page temporaire a pour but d'être utilisée pour le forum des mathématiques 2019 de Porto Vecchio.

## Présentation du jeu

Le jeu consiste à répartir des allumettes en plusieurs tas. Chaque joueur prend à son tour autant d'allumettes qu'il le souhaite mais dans un seul tas.  
Le gagnant est celui qui prend la dernière allumette. (On peut bien sûr faire une variante où le gagnant est celui qui ne prend pas la dernière allumette)

## Résultats mathématiques

### Ecriture binaire

Tout nombre entier peut s'écrire comme une somme de puissance de deux. Par exemple $`13= 2^3 + 2^2 + 2^0`$.  
Un manière de résumer cette décomposition est de mettre un 1 lorsque la puissance est présente et 0 sinon. Autrement dit pour 13, je peux résumer cette décomposition en puissance de 2 sous la forme 1101. C'est ce qu'on appelle l'écriture en binaire.  
Voici d'autres exemples : 7 s'écrit 111, 8 s'écrit 1000, 21 s'écrit 10101.

### Configurations paires

Revenons à notre jeu de Nim : Pour chaque tas, on va considérer l'écriture en binaire du nombre d'allumettes. Ainsi, si on a au début des tas avec respectivement 7, 2 et 6 allumettes, on obtiendra comme écritures binaires :
```
Tas n°0 :  1 1 1  
Tas n°1 :    1 0  
Tas n°2 :  1 1 0  
```

On va alors s'intéresser aux nombres de 1 par colonne et plus précisément si ce nombre est pair ou impair. Pour simplifier, on notera 0 si le nombre de 1 est pair et 1 sinon. Ce qui nous donnerait sur notre exemple :

```
Tas n°0 :  1 1 1  
Tas n°1 :    1 0  
Tas n°2 :  1 1 0  
----------------  
Parité  :  0 1 1  
```

S'il n'y a que des 0, c'est à dire si il y a un nombre pair de 1 sur toutes les colonnes, on dit que la configuration est paire. Sinon on dira qu'elle est impaire. La configuration précédente est donc impaire.  
La configuration suite est paire :  
```
Tas n°0 :  1 0 0  
Tas n°1 :    1 0  
Tas n°2 :  1 1 0  
----------------  
Parité  :  0 0 0   
```

### Propriétés

1. Si on modifie une ligne d'une configuration paire, on obtient une configuration impaire.
2. On peut toujours modifier une ligne d'une configuration impaire pour se ramener à une configuration paire.

Précisons cette dernière propriété en expliquant comment faire : 
+ On prend, en binaire, la ligne correspondant au plus grand nombre d'allumettes et la ligne correspondant à la parité
+ On redétermine la parité avec ces deux lignes c'st à dire que colonne par colonne, on regarde s'il y a un nombre pair ou impair de 1
+ On calcule à quel nombre entier correspond cette deuxième parité écrite en binaire. Le résultat obtenu est le nombre d'allumettes qu'il faut laisser dans le tas contenant le plus d'allumettes pour avoir une configuration paire.

Donnons un exemple : Supposons qu'il y ait trois tas de respectivement 8, 6 et 3 allumettes. On a alors la situation :

```
Tas n°0 :  1 0 0 0  
Tas n°1 :    1 1 0  
Tas n°2 :      1 1  
------------------  
Parité  :  1 1 0 1  
```

En ne regardant que la ligne correspondant au tas le plus gros et la parité, on obtient comme parité de ce deux lignes :

```
Tas n°0 :  1 0 0 0  
Parité  :  1 1 0 1  
------------------  
Total   :  0 1 0 1  
```
Le nombre qui s'écrit 0101 en binaire est $`2^2+2^0=5`$. Il faut donc laisser 5 allumettes dans le tas le plus gros (et donc en retirer 3) pour obtenir une situation paire. Vérifions le : 

```
Tas n°0 :  1 0 1  
Tas n°1 :  1 1 0  
Tas n°2 :    1 1  
----------------  
Parité  :  0 0 0  
```

## Stratégie gagnante

En remarquant que si notre adversaire est dans une configuration paire, il ne peut pas gagner car cela signifie qu'il y a au moins deux tas contenant des allumettes. Donc la stratégie consiste à laisser toujours notre adversaire dans une configuration paire. 
1. Si à notre tour, on est dans une configuration impaire, la propriété 2 nous assure qu'on peut mettre notre adversaire dans une configuration paire (comme expliqué ci-dessus) et la propriété 1 nous assure que notre adversaire nous mettra dans une configuration impaire. Donc de fil en aiguille, comme lui ne peut pas gagner (car il sera toujours dans une configuration paire), c'est forcément nous qui allons gagner.
2. Si à notre tour, on est dans une configuration paire : Soit notre adversaire connait la stratégie et on est sûr de perdre sinon, il suffit d'attendre qu'il fasse l'erreur de nous mettre dans une configuration impaire pour dérouler la stratégie du cas précédent.

## Programme pour aider à mettre en place la stratégie gagnante

Il suffit de rentrer sous forme de liste le nombre d'allumettes de chacun des tas pour obtenir les décompositions binaires, la parité ainsi que le nombre d'allumettes à retirer.

@[Stratégie gagnante au jeu de nim]({"stubs": ["Autre/Nim0.py","Autre/Nim.py"], "command": "python3 Autre/Nim0.py"})

## Prolongement possibles

D'autres jeux peuvent se ramener au jeu de Nim que l'ont vient de voir. Par exemple :
- [Sous forme de pions sur un damier](http://jeux-et-mathematiques.davalan.org/jeux/nim/northcott/index.html)
