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

