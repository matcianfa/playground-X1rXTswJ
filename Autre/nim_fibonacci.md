@[Obtenir la décomposition de Zeckendorf]({"stubs": ["Autre/Zeckendorf0.py","Autre/Zeckendorf.py"], "command": "python3 Autre/Zeckendorf0.py"})

# Jeu de nim : Variante utilisant la suite de Fibonacci

Cette page temporaire a pour but d'être utilisée pour le forum des mathématiques 2019 de Porto Vecchio. Elle est largement inspirée de [cette page](https://blogdemaths.wordpress.com/2012/06/03/devenez-le-maitre-dune-variante-du-jeu-de-nim/).

## Présentation du jeu

Le jeu consiste à étaler N allumettes sur une table. Deux joueurs à tour de rôle doivent en ramasser suivant les règles suivantes :
- Le premier joueur peut prendre autant d'allumettes qu'il le souhaite sauf toutes.
- Un joueur peut prendre à son tour un nombre entre un et le double des allumettes qu'a pris son adversaire au tour précédent.
- Le gagnant est celui qui ramasse la dernière allumette.

## Résultats mathématiques

Commençons par rappeler la définition de la suite de Fibonacci. C'est la suite définie par $`F_0=1`$, $`F_1=2`$ et $`F_{n+2}=F_{n+1}+F_n`$.  
Voici les premieres valeurs : 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,...

Voici des propriétés qui vont nous être utiles pour mettre en place notre stratégie gagnante :

###### Propriétés :
1. Pour tout entier n et m<n-1 : $`F_n< 2F_{n-1}`$ et $`2F_m<F_n`$ 
2. **Théorème de Zeckendorf** :  
   Tout entier naturel non nul peut s'écrire de manière unique comme la somme de nombres de Fibonacci non consécutifs.  
   On notera dans la suite $`N=F_{n_1}+...+F_{n_p}`$ la décomposition dans l'ordre croissant du théorème de Zeckendorf.
3. Si $`N`$ n'est pas un nombre de Fibonacci (autrement dit, il y a au moins deux éléments dans la décomposition de Zeckendorf), alors $`N-F_{n_1}> 2F_{n_1}`$.
4. Si il y a au moins 3 nombres de Fibonacci dans la décomposition de Zeckendorf, alors pour tout n compris entre 1 et  $2F_{n_1}`$`, $`N-F_{n_1}-n`$ n'est pas un nombre de Fibonacci.
5. S'il y a exactement deux nombres dans la décomposition de Fibonacci alors pour tout n compris entre 1 et $`2F_{n_1}`$, on a $`N-F_{n_1}-n`$ qui est soit un nombre qui n'est pas un nombre de Fibonacci, soit un nombre qui est inférieur à $`2n`$.

## Stratégie gagnante

Elle consiste à décomposer le nombre $`N`$ d'allumettes en somme de nombres de Fibonacci non consécutifs comme dans le théorème de Zeckendorf. On a deux cas :
1. $`N`$ n'est pas un nombre de Fibonacci. Alors il suffit de prendre un nombre d'allumettes égal au plus petit nombre de Fibonacci de la décomposition de Zeckendorf.   
   D'après la propriété 3, ce qui reste est plus grand que le double de ce qu'on a pris donc l'autre joueur ne peut pas gagner lors de son prochain tour.  
   D'après la propriété 4 et 5, à notre prochain tour on tombera soit sur un nombre qui n'est pas de Fibonacci et donc on pourra recommencer cette stratégie avec le nombre d'allumettes restantes, soit on tombe sur un nombre inférieur au double de ce qu'a pris notre adversaire et donc on peut gagner.
2. Si $`N`$ est un nombre de Fibonacci, il faut prier pour que notre adversaire ne connaisse pas cette stratégie car quoi qu'on prenne, il pourra l'utiliser pour gagner. S'il ne la connait pas, il suffit d'attendre qu'il fasse l'erreur de nous laisser un nombre d'allumettes qui n'est pas de Fibonacci et utiliser la stratégie 1.
3. Si $`N`$ n'est pas un nombre de Fibonacci mais qu'on ne peut pas prendre le nombre de Fibonacci le plus petit qui apparait dans la décomposition (ce qui peut se produire si on joue en second), alors on est dans le cas 2, il faut attendre le bon moment pour mettre en place la stratégie 1.

## Programme pour aider à mettre en place la stratégie gagnante.

### Obtenir la décomposition de Zeckendorf d'un entier

Compléter la valeur de $`N`$ ci dessous pour que s'affiche la décomposition de Zeckendorf de ce nombre.  

@[Obtenir la décomposition de Zeckendorf]({"stubs": ["Autre/Zeckendorf0.py","Autre/Zeckendorf.py"], "command": "python3 Autre/Zeckendorf0.py"})

## Prolongement possible

Voici un lien vers un tour de magie utilisant la décomposition de Zeckendorf : [Tour de magie](http://jeux-et-mathematiques.davalan.org/jeux/cartes/add/index.html)
