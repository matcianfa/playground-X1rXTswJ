# La suite de Van Eck

Cette page est inspirée de cette [vidéo](https://www.youtube.com/watch?v=etMJxB-igrc).  
Nous allons nous intéresser à la suite de Van Eck qui est une suite créée très recemment (en 2010) et étudiée (pour le plaisir) depuis. Ce qui est intéressant avec cette suite c'est que, comme elle est très récente, on la connait assez mal et très peu de choses ont été découvertes dessus. On a, au mieux, quelques conjectures en observant les termes de la suite ([Wikipedia](https://en.wikipedia.org/wiki/Van_Eck%27s_sequence)).  

Le but de cette page est de calculer les termes de la suite puis de les afficher pour faire quelques observations et conjectures. Libre à vous ensuite d'approfondir et pourquoi pas découvrir des choses que les chercheurs n'auraient pas encore vues...

## Définition de la suite

La suite $`(V_n)`$ commence par $`V_0=0`$. (On pourrait commencer par un autre nombre mais c'est classiquement le choix qui est fait).

Ensuite, supposons connus les premiers termes jusqu'à $`V_n`$. Deux possibilités : 
- Si c'est la première fois qu'apparait le nombre $`V_n`$ jusqu'à présent, alors $`V_{n+1}=0`$.
- Sinon, on compte de combien il faut reculer pour retomber sur la valeur $`V_n`$ dans les termes précédents de la suite.

Regardons la construction des premiers termes :
1. On commence par $`V_0=0`$. Comme 0 apparait pour la première fois, le nombre suivant $`V_1=0`$
2. $`V_1=0`$ et ce n'est pas la première fois qu'il apparait donc on compte de combien il faut reculer pour retomber sur 0.   
Ici comme $`V_0=0`$, on recule de 1 donc $`V_2=1`$
3. $`V_2=1`$ et 1 apparait pour la première fois donc $`V_3=0`$.
4. $`V_3=0`$ et 0 est déjà dans les premiers termes et qu'il faut reculer de 2 pour retomber dessus, $`V_4=2`$
5. $`V_5=0`$ et ainsi de suite

On obtient ainsi comme premiers termes :  
0, 0, 1, 0, 2, 0, 2, 2, 1, 6, 0, 5, 0, 2, 6, 5, 4, 0, 5, 3, 0, 3, 2, 9, 0, 4, 9, 3, 6, 14, 0, 6, 3, 5, 15, 0, 5, 3, 5, 2, 17, 0, 6, 11, 0, 3, 8, 0, 3, 3, 1, 42, 0, 5, 15, 20, 0, 4, 32, 0, 3, 11, 18, 0, 4, 7, 0, 3, 7, 3, 2, 31, 0, 6, 31, 3, 6, 3, 2, 8, 33, 0, 9, 56, 0, 3, 8, 7, 19, 0, 5, 37, 0, 3, 8, 8, 1...

Essayez de calculer seul les termes $`V_6`$ jusqu'à $`V_{10}`$ puis vérifiez avec la liste précédente pour être sûr d'avoir bien compris comment se construit cette suite.

---

## Calcul des termes de la suite (version naive)
`Difficulté : Moyenne`  
`Prérequis : Les listes`

En utilisant la définition précédente, créer une fonction `VanEck(n)` qui donne la liste des valeurs de la suite de Van Eck $`(V_n)`$ de $`V_0`$ jusqu'à $`V_n`$.

> Exemple : `VanEck(4)` doit renvoyer `[0, 0, 1, 0, 2]`.

@[Calcul des termes de la suite de Van Eck]({"stubs": ["TP/VanEck.py"], "command": "python3 TP/VanEck_Test.py"})

---

## Calcul des termes de la suite (version optimisée)
`Difficulté : Difficile`  
`Prérequis : Les listes`

La façon dont on calcule les termes de la suite en utilisant simplement la définition prend beaucoup de temps dès qu'on augmente un peu la valeur de n (plusieurs minutes pour seulement n=100000). Nous allons voir comment optimiser beaucoup nos calculs.

Pour cela nous allons utiliser deux listes : une première dans laquelle on va mettre nos termes au fur et à mesure (comme pour la version précédente) et une autre dans laquelle, à chaque nouvelle valeur de $`V_n`$ qu'on calcule, on va mettre l'indice correspondant. Ainsi il suffira de lire dans cette liste la dernière fois qu'on a croisé une valeur au lieu de chercher à chaque fois dans la liste des termes où était cette dernière valeur.

> Exemple : Supposons qu'on veuille calculer pour n=5.  
On commence par créer nos deux listes : 
- la liste des termes initialisée avec 0 : `liste_termes=[0]`
- la liste des indices qu'on crée déjà en entier (comme on calcule pour n=5, on va créer une liste de longueur 6). Pour l'initialiser, il faut mettre une valeur qu'on n'utilisera pas (par exemple -1 ou None) pour signifier qu'on n'a pas encore trouver cette valeur. Ainsi, au début on a donc une variable `liste_indices = [-1,-1,-1,-1,-1,-1]` (qu'on peut créer facilement en faisant `[-1]*6`). Pour bien préciser les choses : si on a `liste_indices[3]=5`, cela signifie que la dernière fois qu'on a obtenu un 3 comme valeur de notre suite, c'est lorsque l'indice était 5.  
Voyons maintenant comment doit fonctionner notre algorithme pour calculer les 6 premiers termes :
+ A l'étape 0 : On regarde le dernier terme de notre `liste_termes` : C'est 0. On regarde dans notre `liste_indices` la dernière fois qu'on a croisé 0 : on trouve -1 ce qui signifie jamais. Dans ce cas, d'après la façon dont on doit créer la suite, la valeur suivante de la suite $`(V_n)`$ est $`V_1=0`$. On rajoute donc 0 à notre `liste_termes` et comme du coup la dernière fois qu'on a croisé 0 est à l'indice 0 (on ne considère pas encore le nouveau 0 qu'on a rajouté) on le note dans notre `liste_indices`. 
Donc à cette étape on a `liste_termes = [0,0]` et `liste_indices=[0,-1,-1,-1,-1,-1]`.
+ A l'étape 1 : On recommence : la dernier terme est 0. Dans `liste_indices`, la dernière fois qu'on a croisé 0 est en 0. Comme on est à l'étape 1 (on considère $`V_1`$) la distance entre les deux est 1 - 0 = 1. Donc la valeur suivante de la suite est $`V_2=1`$ qu'on ajoute à `liste_termes`. On met à jour le fait que le dernier 0 croisé est à l'indice 1 ce qui donne comme état des variables : `liste_termes = [0,0,1]` et `liste_indices=[1,-1,-1,-1,-1,-1]`.  
Remarque importante : On ne met pas encore le fait qu'on a obtenu un 1 à l'indice 2 dans la `liste_indices` car cette liste nous permet de garder en mémoire ce qui se passe avant d'avoir obtenu ce 1.
+ A l'étape 2 : On rerecommence : le dernier terme est 1. On a jamais croisé de 1 donc on met un 0...  
On obtient comme variables à la fin de cette étape : `liste_termes = [0,0,1,0]` et `liste_indices=[1,2,-1,-1,-1,-1]`.  
+ On a ensuite : `liste_termes = [0,0,1,0,2]` et `liste_indices=[3,2,-1,-1,-1,-1]`.  
+ Et enfin : `liste_termes = [0,0,1,0,2,0]` et `liste_indices=[3,2,4,-1,-1,-1]`.  

Vérifiez bien que vous avec compris le raisonnement avant de vous lancer dans l'algorithme.

A présent, créez votre nouvelle fonction `VanEck(n)` en utilisant l'algorithme qui vient d'être décrit.

@[Calcul des termes de la suite de Van Eck]({"stubs": ["TP/VanEck2.py"], "command": "python3 TP/VanEck2_Test.py"})

---

## Affichage graphique des termes de la suite

Compléter le script ci-dessous pour qu'il affiche les termes de la suite. On utilise la fonction `plt.plot(X,Y)`, où X est la liste des abscisses des points que l'on souhaite tracer et Y la liste des ordonnées. On pourra se repporter à la partie du cours sur matplotlib.

Vous pouvez ensuite modifier comme vous le souhaiter ce script pour essayer de trouver des propriétés intéressantes. On peut par exemple observer que les "pics" ont l'air alignés selon un droite (Cela fait partie des conjectures sur cette suite).


@[affichage des termes de la suite de Van Eck]({"stubs": ["TP/VanEck_graphique.py"], "command": "python3 TP/VanEck_graphique_Test.py"})

---

## Pour aller plus loin 

Une des conjectures consiste à considérer le suite $`(u_n)`$ des maximums entre 0 et n des valeurs de $`\dfrac{V_k}{k}`$. La conjecture affirme que $`(u_n)`$ aurait pour limite 1. Vous pouvez essayer de tester cette conjecture à l'aide d'un programme...
