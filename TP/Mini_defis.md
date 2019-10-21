# Mini Défis

Cette page regroupe des exercices qui demandent un peu plus de reflexion (mathématique) que les exercices des pages précédentes avant de se lancer dans la programmation. Ils nécessitent un niveau collège ou seconde maximum.

## Exercice n° : Paires de chaussettes
`Difficulté : Très Facile`  
`Origine :` [`Hackerrank`](https://www.hackerrank.com/challenges/maximum-draws/problem)

Baptiste cherche des chaussettes pour aller à une soirée. Son tiroir est plein de chaussettes, chaque paire est de couleur différente. Pour choisir une chaussette, il met sa main dans le tiroir et ne voit la couleur de la chaussette qu'une fois qu'il l'a sortie du tiroir.

Dans le pire des cas, combien doit-il prendre de chaussettes dans son tiroir pour être sûr d'avoir une paire de la même couleur ?

> Entrée : Le nombre ***n*** de chaussettes dans le tiroir.

> Sortir : Le nombre de chaussettes que Baptiste doit sortir dans le pire des cas du tiroir être sûr d'avoir une paire de la même couleur.

@[Chacun cherche ses chaussettes sèches]({"stubs": ["Variables_et_fonctions/Chaussettes.py"], "command": "python3 Variables_et_fonctions/Chaussettes_Test.py"})

---

## Exercice n° :  Nombre de bises au nouvel an
`Difficulté informatique : Très facile`  
`Difficulté mathématique : Facile`

Des amis passent le soir du reveillon du nouvel an ensemble. A minuit, chacun embrasse (en faisant deux bises) tous les autres invités.

Combien y a-t-il eu de bises échangées pas les invités pour ce nouvel an ?

> Entrée : Le nombre ***n*** d'invités.

> Sortie : Le nombre de bises échangées pour ce nouvel an.

::: Indications :
On pourra considérer le nombre de bises que doit faire chaque personne puis remarquer qu'en comptant ainsi, on a compté plusieurs fois les mêmes bises.
:::

@[Nombre de bises]({"stubs": ["Variables_et_fonctions/Bises.py"], "command": "python3 Variables_et_fonctions/Bises_Test.py"})

---

## Exercice n° : Bases armées
`Difficulté informatique : Très facile`  
`Difficulté mathématique : Moyenne`  
`Notion : Division euclidienne`  
`Origine :` [`Hackerrank`](https://www.hackerrank.com/challenges/game-with-cells/problem)

Luke est dans ses pensées pendant un cours de maths. Sur un papier quadrillé de ***n*** lignes et ***m*** colonnes, il imagine que chaque case est une base armée. Il veut envoyer des fournitures à ses bases à des points stratégiques, en marquant chaque point en rouge. Si une base contient au moins un colis de fourniture dedans ou sur un de ses bords, on qu'onsidère qu'il y a accès. Par exemple : 
![Fournitures](https://s3.amazonaws.com/hr-challenge-images/0/1479944215-79f12638a7-example-army-game.png)

Etant donnés ***n*** et ***m***, érire une fonction qui renvoit le nombre minimum de colis que Luke doit envoyer pour fournir toutes ses bases.

@[Bases armées]({"stubs": ["Variables_et_fonctions/Bases_armees.py"], "command": "python3 Variables_et_fonctions/Bases_armees_Test.py"})

---

## Exercice n° : Découpe de morceaux de papier
`Difficulté informatique: Très facile`  
`Difficulté mathématique : Moyenne`  
`Origine : ` [`Hackerrank`](https://www.hackerrank.com/challenges/p1-paper-cutting/problem)

Marie veut découper un morceau de papier de dimmension $`n\times m`$ en morceau de papier de dimension $`1\times 1`$ selon les règles suivantes :

+ Elle ne peut couper qu'un morceau de papier à la fois, c'est à dire qu'elle ne peut pas placer des papiers déjà découpés les uns sur les autres ou d'affilée. Elle ne peut pas non plus les plier avant de les découper.

+ Elle découpe en ligne droite horizonthalement ou bien verticalement uniquement.

Voici un exemple montrant les trois seules découpes possibles dans ce cas :
![Découpes](https://s3.amazonaws.com/hr-challenge-images/26273/1476740077-bd1ab26d74-example-cutting-squares.png)

Etant donnés n et m, trouver et renvoyer (avec `return`) le nombre minimum de découpe que Marie peut faire pour découper le papier en carré unité.

> Entrée : Les dimensions entières ***n*** et ***m*** du morceau de papier au départ.

> Sortie : Le nombre minimum de découpe nécessaire pour n'obtenir plus que des petits carrés de dimensions $`1\times 1`$

:::  Indication :
On pourra remarquer que chaque coup de ciseau rajoute un au nombre de morceaux de papier qu'on a ...
:::

@[Découpe de morceaux de papier]({"stubs": ["Variables_et_fonctions/Decoupe_papier.py"], "command": "python3 Variables_et_fonctions/Decoupe_papier_Test.py"})

---
## Exercice n° : Symétrie centrale
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

## Exercice n° : Carreaux mouvants
`Difficulté informatique : Facile`  
`Difficulté mathématique : Moyenne`  
`Notions : Vecteurs, vitesse`  
`Origine :` [`Hackerrank`](https://www.hackerrank.com/challenges/sherlock-and-moving-tiles/problem)

On considère deux carreaux carrés de côté L, initialement tous les deux placés de manière à avoir leur coin inférieur gauche sur l'origine du repère et leurs cotés parallèles aux axes.

A t=0, les deux carreaux commencent à bouger sur la ligne y=x (pour x et y positifs) avec une vitesse $`V_1`$ et $`V_2`$.

Pour une valeur q donnée, afficher la valeur du temps t pour lequel l'aire de l'intersection des deux carreaux est égale à q.
![figure](https://s3.amazonaws.com/hr-challenge-images/5519/1422784979-db005a0a44-drawing-3.svg)

> Entrée : Les valeurs de L, V1, V2 et q.

> Sortie : La valeur de t cherchée.

@[Carreaux mouvants]({"stubs": ["Variables_et_fonctions/Carreaux_mouvants.py"], "command": "python3 Variables_et_fonctions/Carreaux_mouvants_Test.py"})

---

## Exercice n° : Triangle de hauteur minimum
`Difficulté : Facile`  
`Notion : Aire d'un triangle`  
`Origine :`[`Hackerrank`](https://www.hackerrank.com/challenges/lowest-triangle/problem)

Etant donnés deux entiers ***a*** et ***b***, écrire un programme qui donne la plus petite valeur de ***h*** telle que le triangle de base ***b*** et de  hauteur ***h*** ait une aire plus grande que ***a***.
![Triangle](https://s3.amazonaws.com/hr-assets/0/1496306792-f2c37eea44-triangle.jpg)

> Entrée : Des entiers ***a*** et ***b*** correspondant respectivement à la valeur de l'aire à dépasser et la longueur de la base du triangle.

> Sortie : La plus petite valeur de ***h*** cherchée, affichée avec `print`.

@[Triangle de hauteur minimum]({"stubs": ["Les_boucles/Triangle_h_min.py"], "command": "python3 Les_boucles/Triangle_h_min_Test.py"})

---

## Exercice n° : Passage des coordonnées cartésiennes à polaires
`Difficulté : Moyen à difficile`  
`Notion utilisée : Condition`

Le but de cet exercice est de créer un programme qui reçoit les coordonnées cartésiennes et les transforme en coordonnées polaires.  On pourra trouver plus d'informations sur les coordonnées polaires par exemple ici : [Wikipédia](https://fr.wikipedia.org/wiki/Coordonn%C3%A9es_polaires)

Entre autre, voici une des façons d'obtenir les valeurs de $`r`$ et $`\theta`$ :
+ $`r=\sqrt{x^2+y^2}`$
+ $`\theta=\left\{\begin{array}{ll} arctan\left(\frac{y}{x}\right) & \textrm{si } x>0 \\ arctan\left(\frac{y}{x}\right) + \pi & \textrm{si } x<0\ et \ y\geq 0 \\ arctan\left(\frac{y}{x}\right) - \pi & \textrm{si } x<0\ et \ y<0 \\ \dfrac \pi 2 & \textrm{si } x=0\ et\ y>0 \\ -\dfrac \pi 2 & \textrm{si } x=0\ et\ y<0 \end{array}\right.`$

> Entrée : Les coordonnées cartésiennes ***x*** et ***y***.

> Sortie : Les coordonnées polaires correspondantes ***r*** et $`\theta`$ arrondies à 3 chiffres après la virgule.

@[Passage des coordonnées cartésiennes à polaires]({"stubs": ["Les_conditions/passage_cartesiennes_polaires.py"], "command": "python3 Les_conditions/passage_cartesiennes_polaires_Test.py"})

---

