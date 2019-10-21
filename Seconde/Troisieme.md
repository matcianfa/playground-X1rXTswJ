# Classe de Seconde - Début d'année

Cette page est un peu particulière, elle regroupe des exercices demandant une programmation en python utilisant des notions de seconde en python mais un niveau troisième maximum en mathématique. 


## Exercice n° 1: Prix total
`Difficulté : Très facile`

Léa va régulièrement acheter toujours les mêmes bonbons : des fraises à 0.04 euros l'unité et des réglisses à 0.07 euros l'unité.  
Créer un programme qui donne le prix total payé par Léa en fonction du nombre ***a*** de fraises et ***b*** de réglisses achetés.

> Entrée : Le nombre ***a*** de fraises et ***b*** de réglisses achetés.

> Sorties : le prix payé par Léa.

@[Ticket de caisse]({"stubs": ["Variables_et_fonctions/Bonbons.py"], "command": "python3 Variables_et_fonctions/Bonbons_Test.py"})

---

## Exercice n° 2: Fréquence cardiaque maximale
`Difficulté : Très facile`

La fréquence cardiaque maximale (FCM) est le rythme que le cœur humain d'une personne donnée atteint lors des plus fortes sollicitations. On pourra trouver de plus amples informations [ici](https://fr.wikipedia.org/wiki/Fr%C3%A9quence_cardiaque_maximale) .

On peut y lire que la formule qui semble la plus proche de la réalité est donnée par $`FCM = 191,5-0,007*age^2`$.

Créer un programme qui prend en entrée l'age et renvoie la valeur de la FCM.

@[FCM]({"stubs": ["Seconde/Debut/fcm.py"], "command": "python3 Seconde/Debut/fcm_Test.py"})

---

# Exercice n° 3: Périmètre et aire d'un polygone régulier
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

## Exercice n° 4: Coefficient directeur d'une droite (AB)
`Difficulté : Très facile`  

Créer une fonction qui prend en entrée les valeurs xA, yA, xB et yB et renvoie en sortie le coefficient directeur de la droite (AB) avec A et B de coordonnées respectives (xA,yA) et (xB,yB).

> Exemple : `ma_fonction(1,2,3,8)` doit renvoyer `3` car le coefficient directeur de la droite (AB) où A(1,2) et B(3,8) vaut $`\dfrac{8-2}{3-1} = 3`$.

> Remarque : On ne s'occupera pas du cas où la droite pourrait être verticale.

@[Calcul du coefficient directeur]({"stubs": ["Seconde/Debut/coeff_dir.py"], "command": "python3 Seconde/Debut/coeff_dir_Test.py"})

---

## Exercice n° 5: Afficher si un nombre est pair
`Difficulté : Très facile`  
`Notion utilisée : Condition`

Faire un programme qui affiche si un nombre est pair ou impair.

::: Aide
Pour vérifier si un entier ***n*** est divisible par un entier ***k***, il suffit de vérifier si son reste par la division euclidienne par ***k*** est nul ou pas autrement dit si `n%k==0`.
:::

> Entrée : Un nombre entier ***n***

> Sortie : "PAIR" ou "IMPAIR". (N'oubliez pas les guillemets)

@[Parité d'un nombre]({"stubs": ["Les_conditions/nombre_pair.py"], "command": "python3 Les_conditions/nombre_pair_Test.py"})

---

## Exercice n° 6: Radars routiers
`Difficulté : Très facile`  
`Notion utilisée : Condition`

Les radars routiers permettent de mesurer la vitesse d'un véhicule et le verbaliser s'il dépasse la limite autorisée. On pourra trouver [ici](https://fr.wikipedia.org/wiki/Radar_Doppler) leur fonctionnement. Comme pour toute mesure, il y a un des incertitudes. C'est pour cela que la loi prévoit que pour toute mesure faite par un radar fixe, on doit retirer 5km/h à la vitesse mesurée si elle est inférieure à 100 km/h et 5% si elle est supérieure à 100 km/h. Le résultat est la vitesse retenue pour le véhicule pour savoir si elle dépasse la limitation de vitesse.  
Ainsi, pour une vitesse mesurée de 60 km/h, on retiendra comme vitesse 55 km/h et pour une vitesse mesurée de 110 km/h, on retiendra une vitesse de 104,5 km/h.

Créer un programme qui prend en entrée la vitesse mesurée `v` et renvoie la vitesse retenue pour la verbalisation.

> Entrée : La vitesse ***v***

> Sortie : La vitesse retenue après retrait de la marge d'erreur prévue par la loi.

@[Radars routiers]({"stubs": ["Seconde/Debut/radars.py"], "command": "python3 Seconde/Debut/radars_Test.py"})

---

## Exercice n° 7: Numéro de sécurité sociale
`Difficulté : Facile`  
`Notion utilisée : Condition`

Le numéro de sécurité social est composé de 13 chiffres suivis d'une clé de 2 chiffres. On pourra lire pour plus de détail sur la signification des 13 premiers chiffres par exemple sur [Wikipédia](https://fr.wikipedia.org/wiki/Num%C3%A9ro_de_s%C3%A9curit%C3%A9_sociale_en_France)

Nous allons nous intéresser à la clé car elle permet de vérifier si il n'y a pas eu d'erreur en reportant le numéro sur un formulaire ou lors du transfert informatique par exemple. Voici comment est calculée la clé : 
1. On prend le nombre composé des 13 premiers chiffres du numéro de sécurité sociale et on calcule le reste de sa division euclidienne par 97.
2. On soustrait alors ce reste à 97. Le résultat est la clé. 

Exemple : si le numéro est 9700000000100 alors le reste de la division euclidienne par 97 est 3. La clé est alors 97-3=94. 

:::Rappel sur la division euclidienne
Pour obtenir le quotient de la division euclidienne de n par d, on tape `n//d`.

Pour obtenir le reste de la division euclidienne de n par d, on tape `n%d`.
:::

Le but est de créer un programme qui prend en entrée le ***numéro*** de sécurité sociale et la ***clé*** et qui affiche "VALIDE" si la ***clé*** correspond au ***numéro*** et "NON VALIDE" sinon.

> Entrée : Le ***numéro*** et la ***clé***

> Sortie : "VALIDE" si la ***clé*** correspond au ***numéro*** et "NON VALIDE" sinon. N'oubliez pas les guillemets.


@[Validité du numéro de sécurité sociale]({"stubs": ["Les_conditions/Numero_securite_sociale.py"], "command": "python3 Les_conditions/Numero_securite_sociale_Test.py"})

---

## Exercice n° 8: Conversion degré Celsius <-> degré Fahrenheit
`Difficulté : Facile`
`Notion utilisée : Condition`

Écrire un programme qui convertit les degrés Celsius en degré Fahrenheit et inversement.

Pour les formules, on regardera [Wikipédia](https://fr.wikipedia.org/wiki/Degr%C3%A9_Fahrenheit)

> Entrée : Une température ***t*** et un nombre ***n***. 
> + Si ***n*** vaut 0, ***t*** est en degré Celsius et il faut la convertir en degré Fahrenheit. 
> + Si ***n*** vaut 1, ***t*** est en degré Fahrenheit et il faut la convertir en degré Celsius.

> Sortie : La température convertie, arrondie à 3 chiffres après la virgule.

@[Conversion Celsius/Fahrenheit]({"stubs": ["Les_conditions/Conversion_Celsius_Fahrenheit.py"], "command": "python3 Les_conditions/Conversion_Celsius_Fahrenheit_Test.py"})

---

## Exercice n° 9: Dire si un triangle est rectangle I
`Difficulté : Très facile`  
`Notion utilisée :  Condition`

Faire un programme qui affiche si un triangle dont on donne les angles est rectangle ou pas.

> Entrée : Les trois angles ***a***, ***b*** et ***c*** en degrés.

> Sortie : "RECTANGLE" si le triangle est rectangle, "PAS RECTANGLE" sinon. N'oubliez pas les guillemets.

@[Triangle rectangle ? Cas 1]({"stubs": ["Les_conditions/Triangle_rectangle_0.py"], "command": "python3 Les_conditions/Triangle_rectangle_0_Test.py"})

---

## Exercice n° 10: Dire si un triangle est rectangle II
`Difficulté : Très facile`  
`Notion utilisée :  Condition`

Faire un programme qui affiche si un triangle dont on donne les longueurs est rectangle ou pas.

> Entrée : Les trois longueurs ***a***, ***b*** et ***c*** du triangle.

> Sortie : "RECTANGLE" si le triangle est rectangle, "PAS RECTANGLE" sinon. N'oubliez pas les guillemets.

@[Triangle rectangle ? Cas 2]({"stubs": ["Les_conditions/Triangle_rectangle_1.py"], "command": "python3 Les_conditions/Triangle_rectangle_1_Test.py"})

---

## Exercice n° 11: Triangles constructibles
`Difficulté : Facile à moyen`  
`Notion utilisée :  Condition`

Si on choisit 3 nombres, il n'est pas toujours possible de construire un triangle ayant pour longueur ces nombres.
Par exemple, il est impossible de construire un triangle de côtés de longueurs 1, 1 et 5. 

Un triangle est constructible si pour chaque coté, sa longueur est inférieur à la somme des longueurs deux autres cotés.

Le but de cet exercice est de créer un programme qui nous dit si le triangle est constructible ou pas à partir des longueurs qui nous sont données.

> Entrée : Trois longueurs ***a***, ***b*** et ***c***.

> Sortie : Affiche "CONSTRUCTIBLE" si on peut construire un triangle ayant des cotés de ces trois longueurs ou bien "PAS CONSTRUCTIBLE" sinon. N'oubliez pas les guillemets.  
> Pour les plus rapides, vous pouvez afficher "PLAT" si le triangle qu'on peut construire est plat. 

@[Triangles constructibles ?]({"stubs": ["Les_conditions/Triangles_constructibles.py"], "command": "python3 Les_conditions/Triangles_constructibles_Test.py"})

---

## Exercice n°12 : Donner la nature d'un triangle
`Difficulté : Difficile`  
`Notion utilisée :  Condition`

Le but de cet exercice est de faire un programme qui donne la nature d'un triangle c'est à dire s'il est rectangle, isocèle, équilatéral ou rectangle isocèle à partir des longueurs données. Dans les autres cas, on dira qu'il est quelconque.

Pour les plus rapides, pour passer les derniers tests, il faut de plus vérifier si le triangle est un triangle d'or. On pourra trouver des informations sur [Wikipédia](https://fr.wikipedia.org/wiki/Triangle_d%27or_(g%C3%A9om%C3%A9trie))

::: Indications  
Voici plusieurs points qui peuvent faire que votre programme ne marche pas:
+ Reflechissez bien à l'ordre de vos conditions. Par exemple en pseudo code :
```
    Si le triangle est isocèle
        afficher("ISOCELE")
    Sinon si le triangle est équilateral
        afficher("EQUILATERAL")
```
Ce code affichera "ISOCELE" pour un triangle equilatéral car la condition isocèle sera vérifiée avant et donc le programme n'ira pas jusqu'à la condition équilatérale.
+ Pensez à bien vérifier pour les 3 sommets une condition du type "être rectangle" ou "isocèle".
+ Attention aux problèmes d'arrondis avec Python. Je rappelle qu'en Python, $`\sqrt{2}^2=2.0000000000000004 `$ ! Donc pour vérifier des égalités comme celle de Pythagore, il vaut mieux vérifier si `c**2-a**2-b**2` une fois arrondi (à 10 chiffres après la virgule par exemple) vaut 0 plutôt que directement.
:::

> Entrée : Les trois longueurs ***a***, ***b*** et ***c*** du triangle.

> Sortie : Les propriétés du triangle parmi : "RECTANGLE", "RECTANGLE ISOCELE", "ISOCELE", "EQUILATERAL", "QUELCONQUE" (et pour les plus rapide : "TRIANGLE D'OR"). N'oubliez pas les guillemets.

@[Nature d'un triangle]({"stubs": ["Les_conditions/Nature_d_un_triangle.py"], "command": "python3 Les_conditions/Nature_d_un_triangle_Test.py"})

---

## Exercice n°13 : Constante de Champernowne
`Difficulté : Moyen`  
`Notions utilisées :  Condition, boucle`

On appelle constante de Champernowne le nombre 0.123456789101112131415161718192021... c'est à dire le nombre où on écrit tous les nombres à la suite les uns des autres. 

Écrire un programme qui prend ***n*** en entrée et affiche la constante de Champernowne jusqu'au nombre ***n*** inclus.

Par exemple si ***n***=3, il faut afficher 0.123.

:::Aide
On pourra utiliser l'astuce suivante : si on écrit `print("texte", end="")`, le programme n'ira pas à la ligne à chaque nouvel affichage et on pourra ainsi afficher tous les nombres d'affilée.
:::

> Entrée : Un entier ***n***

> Sortie : la constante de Champernowne jusqu'au rang ***n***.

@[Constante de Champernowne]({"stubs": ["Les_boucles/Champernowne.py"], "command": "python3 Les_boucles/Champernowne_Test.py"})

---

## Exercice n°14 : Nombres parfaits
`Difficulté : Moyen`  
`Notions utilisées :  Condition, boucle`

Un nombre est dit parfait si il est égal à la somme de ses diviseurs stricts (c'est à dire des diviseurs strictement plus petit que lui même).

Par exemple : 
- Les diviseurs de 6 sont 1, 2, 3 et 6. La somme de ses diviseurs stricts est donc 1+2+3=6. Le nombre 6 est donc un nombre parfait.
- Les diviseurs de 8 sont 1, 2, 4, 8. La somme de ses diviseurs stricts est donc 1+2+4=7. Le nombre 8 n'est donc pas parfait.

Écrire un programme qui affiche si le nombre est parfait ou pas. 

::: Aide 
On utilisera le fait que d est un diviseur de n si et seulement si n%d==0.
:::

> Entrée : un nombre entier ***n***.

> Sortie : "PARFAIT" si le nombre est parfait ou "PAS PARFAIT" sinon.

@[Nombre Parfait ?]({"stubs": ["Les_boucles/Nombres_parfaits.py"], "command": "python3 Les_boucles/Nombres_parfaits_Test.py"})

---

## Exercice n°15 : Sommes de deux dés
`Difficulté : Facile`  
`Notions utilisées :  Condition, boucle`
On s’intéresse au lancer de deux dés et plus précisément à la somme des résultats des deux dés. 

Écrire un programme qui, pour un ***k*** donné, affiche le nombre de façons d'obtenir ***k*** en faisant la somme des résultats des deux dés. Par exemple si ***k***=5, il y a 4 façons d'obtenir 5 : 1+4, 2+3, 3+2, 4+1.

> Entrée : Un entier ***k***.

> Sortie : Le nombre de façons d'obtenir ***k*** en ajoutant les résultats du lancer de deux dés.

@[Sommes de deux dés]({"stubs": ["Les_boucles/Somme_deux_dés.py"], "command": "python3 Les_boucles/Somme_deux_dés_Test.py"})

---

## Exercice n°16 : Sommes de trois dés
`Difficulté : Facile`  
`Notions utilisées :  Condition, boucle`

On s’intéresse à présent au lancer de trois dés et plus précisément à la somme des résultats de ces trois dés. 

Écrire un programme qui, pour un ***k*** donné, affiche le nombre de façons d'obtenir ***k*** en faisant la somme des résultats des trois dés. Par exemple si ***k***=4, il y a 3 façons d'obtenir 4 : 1+1+2, 1+2+1, 2+1+1

> Entrée : Un entier ***k***.

> Sortie : Le nombre de façons d'obtenir ***k*** en ajoutant les résultats du lancer de trois dés.

@[Sommes de trois dés]({"stubs": ["Les_boucles/Somme_trois_dés.py"], "command": "python3 Les_boucles/Somme_trois_dés_Test.py"})

---

## Exercice n°17 : Vérifier si un nombre est premier I
`Difficulté : Moyenne`  
`Notions utilisées : Condition, boucle`

Je rappelle qu'un nombre premier est un nombre qui a exactement 2 diviseurs qui sont 1 et lui même. Ainsi 2, 3 ,5 ,7, 11 sont des nombres premiers mais 4, 6, 9 n'en sont pas.

Le but de cet exercice est de créer un algorithme qui nous dit si un nombre est premier ou pas.

Etant donnée la définition, pour savoir si un nombre ***n*** est premier ou pas, on va tout simplement tester s'il est divisible par un des nombres compris entre 2 et ***n-1***. Dès qu'on trouve un diviseur, on affiche "PAS PREMIER" sinon on affiche "PREMIER".

::: Aide
+ Je rappelle que pour savoir si un nombre ***d*** divise ***n***, il suffit de regarder si ***n%d==0***
+ Dès qu'on a trouvé un diviseur, on peut s'arrêter. On pourra utiliser break si on utilise un boucle `for`
+ N'oubliez pas que `return` arrête l'execution de la fonction.
:::

> Entrée : Un nombre ***n***

> Sortie : "PREMIER" ou "PAS PREMIER"

@[Nombre premier ?]({"stubs": ["Les_boucles/Nombre_premier1.py"], "command": "python3 Les_boucles/Nombre_premier1_Test.py"})

---

## Exercice n°18 : Vérifier si un nombre est premier II
`Difficulté : Moyenne`  
`Notions utilisées : Condition, boucle`

La version précédente a quelques défauts facilement améliorables. 

Le premier est que le programme vérifie si le nombre est divisible par tous les nombres pairs or s'il n'est pas divisible par 2, ça ne sert à rien de vérifier pour les autres.

De plus, si ***n***=117 par exemple, c'est évident qu'il ne peut pas être divisible par 116, ni même 115 ou 114... car ces nombres sont trop grands. Par un petit raisonnement, on peut montrer qu'il ne sert à rien de chercher des diviseurs plus grands que $`\sqrt n`$

Recopiez votre programme précédent ci-dessous et améliorez le en vous aidant des deux remarques précédentes.
Avant de le modifier, lancer Run pour voir qu'il est trop lent pour passer les tests.

:::Aide
+ Traitez le cas de 2 à part puis utilisez la possibilité de `range` d'aller de 2 en 2.
+ Python calcule très mal les racines carrées surtout pour les grands nombres donc dans la pratique, pour éviter les erreurs d'arrondi, il vaut mieux tester jusqu'à $`\sqrt(n) +1`$.
:::

> Entrée : Un nombre ***n***

> Sortie : "PREMIER" ou "PAS PREMIER"

@[Nombre premier ?]({"stubs": ["Les_boucles/Nombre_premier2.py"], "command": "python3 Les_boucles/Nombre_premier2_Test.py"})

---

## Exercice n°19 : Décomposition des entiers sous la forme $`impair.2^k`$
`Difficulté : Moyenne`  
`Notion utilisée : Boucle`

Tout nombre entier ***n*** peut s'écrire $`n=m . 2^k`$ où ***m*** est un nombre impair. Pour ce faire, il suffit de diviser ***n*** par 2 autant que possible. Le résultat final est alors ***m*** et le nombre de fois où on a divisé par 2 nous donne ***k****. 

Créer un programme qui donne la valeur de ***m*** et ***k*** pour un nombre entier ***n*** donné.

> Entrée : Un entier ***n***.

> Sortie : Les valeurs de ***m*** et ***k*** séparés par un espace.

@[Décomposition d'un nombre]({"stubs": ["Les_boucles/Décomposition_d_un_nombre.py"], "command": "python3 Les_boucles/Décomposition_d_un_nombre_Test.py"})

---

## Exercice n°20 : Triplets pythagoriciens
`Difficulté : Moyenne`  
`Notions utilisées : Condition, boucle`

On appelle un triplet pythagoricien trois nombres entiers ***a***, ***b*** et ***c*** vérifiant l'égalité de Pythagore : $`a^2+b^2=c^2`$.

Écrire un programme qui prend en entrée le nombre ***c*** et qui donne le nombre de couples (***a***,***b***) vérifiant l'égalité de Pythagore.

Par exemple, si ***c=1***, il y a deux couples qui conviennent : (1,0) et (0,1).

> Entrée : Un entier ***c***.

> Sortie: Le nombre de couples d'entiers (***a***,***b***) vérifiant l'égalité de Pythagore $`a^2+b^2=c^2`$.

@[Triplets pythagoriciens]({"stubs": ["Les_boucles/triplets_pythagoriciens.py"], "command": "python3 Les_boucles/triplets_pythagoriciens_Test.py"})

---

