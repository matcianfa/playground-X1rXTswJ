# Autour de Kaprekar
`Difficulté : Difficile à très difficile`

Kaprekar est un mathématicien indien qui s'est beaucoup intéressé aux nombres. Nous allons nous pencher sur les nombres et un algorithme associé à son nom.

### Les nombres de Kaprekar

Un nombre de Kaprekar est un nombre dont l'écriture décimale du carré de ce nombre peut être séparée en deux nombres (pas forcément de même taille) dont la somme vaut le nombre initial.

Exemples :
+ 9 est un nombre de Kaprekar car 9²=81 et on peut séparer 81 en 8 et 1 dont la somme 8+1 = 9.
+ 45 est un nombre de Kaprekar car 45²=2025 et on peut séparer 2025 en 20+25=45.
+ 12 n'est pas un nombre de Kaprekar car 12²=144 et on ne peut pas couper ce nombre pour trouver 12 (1+44=45, 14+4=18).
+ 4 879 est un nombre de Kaprekar car 4879² = 23804641 et 238 + 04 641 = 4 879.

Créer un programme qui affiche (avec `print`) si un nombre ***n*** est de Kaprekar ou pas.

::: Aide
Il sera peut-être utile d'utiliser le `else` avec la boucle `for` qui permet d'executer des commandes seulement si la boucle `for` s'est terminée normalement (c'est à dire sans `break`)
:::

> Entrée : Un entier ***n***

> Sortie : "KAPREKAR" ou "PAS KAPREKAR".

@[Kaprekar ?]({"stubs": ["Vrac/Nombres_Kaprekar.py"], "command": "python3 Vrac/Nombres_Kaprekar_Test.py"})

---

### Algorithme de Kaprekar

Prenons un nombre ***n***. Considérons l'algorithme suivant :
1. En rangeant les chiffres de ***n*** du plus grand au plus petit, on obtient un nombre ***a*** 
2. En rangeant les chiffres de ***n*** du plus petit au plus grand, on obtient un nombre ***b***.
3. On forme alors le nombre K(n)= ***a*** - ***b*** .
4. On recommence l'algorithme avec K(n).

Kaprekar s'est rendu compte qu'en faisant ainsi avec un nombre de 3 chiffres (non tous identiques), on obtenait toujours le nombre 495. Dans le cas des nombres de 4 chiffres (non tous identiques), on obtient toujours 6174. Dans les autres cas, on obtient au bout d'un certain temps des boucles qui se répètent.

Exemples: 
+ Si on part de n=326,
 - alors a=632 et b = 236 donc a-b=396. 
 - On recommence avec 396 : a=963 et b= 369. a-b=594
 - On recommence avec 594 : a=954 et b= 459. a-b=495
 - On recommence avec 495 : a=954 et b= 459. a-b=495. On obtiendra donc toujours le même résultat.
+ Si on par de n=34,
 - alors a=43 et b=34 donc  a-b=9.
 - On recommence avec 9  : a=90 et b=09 donc a-b=81 (Comme on considère des nombres de 2 chiffres, 9=09)
 - On recommence avec 81 : a=81 et b=18 donc a-b=63
 - On recommence avec 63 : a=63 et b=36 donc a-b=27
 - On recommence avec 27 : a=72 et b=27 donc a-b=45
 - On recommence avec 45 : a=54 et b=45 donc a-b=9. On peut s'arrêter car on a déjà obtenu 9 donc les calculs seront les mêmes. On a donc une boucle.
 
Le but est de créer un programme qui prend en entrée ***n*** et qui affichera la liste des nombres qui seront affichés en boucle si on itère l'algorithme de Kaprekar.

Par exemple pour n=326, il faudra afficher [495] car c'est ce nombre qui apparaitra en boucle. Pour n=34, il faudra afficher [9,81,63,27,45].

> Entrée : Un nombre ***n***.

> Sortie : La liste des nombres qui sortiront en boucle quand on réitère l'algorithme de Kaprekar en partant de ***n*** affiché avec `print`.

@[Algorithme de Kaprekar]({"stubs": ["Vrac/Algo_Kaprekar.py"], "command": "python3 Vrac/Algo_Kaprekar_Test.py"})
