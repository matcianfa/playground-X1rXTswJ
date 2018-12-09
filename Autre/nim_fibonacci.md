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

    1. Pour tout entier n et m<n-1 : $`F_n< 2F_{n-1}`$ et $`2F_m<F_n`$ 
    2. **Théorème de Zeckendorff** :  
       Tout entier naturel non nul peut s'écrire de manière unique comme la somme de nombres de Fibonacci non consécutifs.  
       On notera dans la suite $`N=F_{n_1}+...+F_{n_p}`$ la décomposition du théorème de Zeckendorff.
    3. Si $`N`$ n'est pas un nombre de Fibonacci (autrement dit, il y a au moins deux éléments dans la décomposition de Zeckendorff), alors $`N-F_{n_1}> 2F_{n_1}`$.
    4. Si il y a au moins 3 nombres de Fibonacci dans la décomposition de Zeckendorff, alors pour tout n compris entre 1 et  $2F_{n_1}`$`, $`N-F_{n_1}-n`$ n'est pas un nombre de Fibonacci.
    5. S'il y a exactement deux nombres dans la décomposition de Fibonacci alors pour tout n compris entre 1 et $2F_{n_1}`$`, on a $`N-F_{n_1}-n`$ qui est soit un nombre qui n'est pas un nombre de Fibonacci, soit un nombre qui est inférieur à $`2n`$.



