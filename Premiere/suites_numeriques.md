# Classe de Première - Suites numériques

## Exercice n° 1 : Calcul des termes d'une suite définie par $`u_n=f(n)`$
`Difficulté : Très facile`  
`Programme officiel`

On considère la suite $`(u_n)`$ définie pour tout entier naturel $`n`$ par $`u_n=\dfrac{3n-9}{2n+1}`$.

Créer une fonction qui prend en entrée un entier naturel $`n`$ et renvoie en sortie la valeur de $`u_n`$.

> Entrée : Un entier naturel $`n`$.

> Sortie : Le programme doit afficher la valeur de $`u_n`$ définie ci-dessus.

@[Calcul des termes d'une suite]({"stubs": ["Premiere/Suites/Calcul_terme1.py"], "command": "python3 Premiere/Suites/Calcul_terme1_Test.py"})

---

## Exercice n° 2 : Calcul des termes d'une suite définie par récurrence I
`Difficulté : Facile`  
`Programme officiel`

Pour calculer à l'aide d'un programme les termes d'une suite définie par récurrence, l'idée est tout simplement de calculer au fur et à mesure les valeurs de la suite en les sauvegardant dans une seule variable ***u*** qui commence à $`u_0`$.

Dans la fenêtre ci-dessous, on a déjà commencé à écrire un programme pour calculer la valeur de $`u_n`$ définie par $`u_0=5`$ et $`u_{n+1}=2u_n-3`$. Remplacez les @ par ce qu'il faut pour que le programme fonctionne.

> Entrée : Un entier ***n***.

> Sortie : Le programme doit afficher la valeur de $`u_n`$ définie ci-dessus.

@[Calcul des termes d'une suite]({"stubs": ["Les_boucles/Calcul_terme_suite0.py"], "command": "python3 Les_boucles/Calcul_terme_suite0_Test.py"})

---

## Exercice n° 3 : Calcul des termes d'une suite définie par récurrence II
`Difficulté : Facile`  
`Programme officiel`

Dans cet exercice, on considère une suite u définie par $`u_{n+1}=3-4u_n`$ et de premier terme $`u_0`$.
Le but de cet exercice est de créer un programme qui prend en entrée les valeurs de ***n*** et $`u_0`$ et affiche la valeur de $`u_n`$.

> Entrée : Un entier ***n*** et $`u_0`$.

> Sortie : La valeur de $`u_n`$.

@[Calcul des termes d'une suite]({"stubs": ["Les_boucles/Calcul_terme_suite0_5.py"], "command": "python3 Les_boucles/Calcul_terme_suite0_5_Test.py"})

---

## Exercice n° 4 : Calcul des termes d'une suite définie par récurrence III
`Difficulté : Facile`  
`Programme officiel`

Dans cet exercice, on considère une suite u définie par $`u_{n+1}=u_n+n+1`$ et de premier terme $`u_0`$.
Le but de cet exercice est de créer un programme qui prend en entrée les valeurs de ***n*** et $`u_0`$ et affiche la valeur de $`u_n`$.

> Entrée : Un entier ***n*** et $`u_0`$.

> Sortie : La valeur de $`u_n`$.

@[Calcul des termes d'une suite]({"stubs": ["Les_boucles/Calcul_terme_suite1.py"], "command": "python3 Les_boucles/Calcul_terme_suite1_Test.py"})

---

## Exercice n° 5 : Calcul des termes d'une suite définie par récurrence IV
`Difficulté : Facile`  
`Programme officiel`

Le but de cet exercice est de calculer les termes de la suite définie par $`u_{n+1}=a.u_n+b`$ et de premier terme $`u_0`$.

> Entrée : Les valeurs de ***a***, ***b***, $`u_0`$ et ***n***.

> Sortie : La valeur de $`u_n`$.

@[Calcul des termes d'une suite]({"stubs": ["Les_boucles/Calcul_terme_suite2.py"], "command": "python3 Les_boucles/Calcul_terme_suite2_Test.py"})

---

## Exercice n° 6 : Calcul des termes d'une suite définie par récurrence V
`Difficulté : Facile`  
`Notion utilisée : Les listes`  
`Programme officiel`

Le but de cet exercice est de calculer tous les termes de la suite définie par $`u_{n+1}=u_n^2-5`$ et de premier terme $`u_0=0`$ jusqu'à un certain rang.

> Entrée : Le valeur de ***N*** jusqu'à laquelle on souhaite calculer.

> Sortie : La liste des valeurs de $`(u_n)`$ pour n allant de 0 jusqu'à ***N*** (compris).

@[Calcul des termes d'une suite]({"stubs": ["Premiere/Suites/Calcul_terme2.py"], "command": "python3 Premiere/Suites/Calcul_terme2_Test.py"})

---

## Exercice n° 7 : Calcul de sommes I
`Difficulté : Facile`  
`Programme officiel`

Pour un $`N`$ donné, on souhaite calculer la somme des termes $`u_0+u_{1}+\dots+u_{N-1}+u_N`$ de la suite $`(u_n)`$ définie par $`u_0 = 2`$ et $`u_{n+1}=2u_n-1`$. Pour cela, compléter et traduire en python l'algorithme suivant :

```
ma_fonction(N) :
    u ← ...
    S ← u
    Pour i allant de 1 à ...
        u ← ...
        S ← ...
    Renvoyer  ...
```

@[Calcul de sommes]({"stubs": ["Premiere/Suites/Calcul_de_sommes1.py"], "command": "python3 Premiere/Suites/Calcul_de_sommes1_Test.py"})

---

## Exercice n° 8 : Calcul de sommes II
`Difficulté : Facile`  
`Programme officiel`

Le but de cet exercice est de faire une fonction qui calcule la valeur de la somme $`1^p+2^p+3^p+\dots+n^p`$ pour des valeurs de ***n*** et ***p*** données.

> Entrée : Un entier naturel ***n*** et un entier ***p*** (qui peut être négatif).

> Sortie : La valeur de la somme $`1^p+2^p+3^p+\dots+n^p`$.

:::Aide
Pour calculer une somme, il suffit de créer une variable S qui commence à 0 puis, dans une boucle, on rajoute à chaque étape un des termes.
:::

@[Calcul de sommes]({"stubs": ["Les_boucles/Calcul_de_sommes.py"], "command": "python3 Les_boucles/Calcul_de_sommes_Test.py"})

---

## Exercice n° 9 : Calcul de la somme des termes d'une suite arihmétique
`Difficulté : Facile`  
`Programme officiel`  

Le but de cet exercice est de faire une fonction qui calcule la valeur de la somme $`u_i+u_{i+1}+\dots+u_{j-1}+u_j`$ pour des valeurs entières de ***i*** et ***j*** données dans le cas où $`(u_n)`$ est une suite arithmétique de premier terme $`u_0`$ et de raison $`r`$.

> Entrée : Les valeurs de $`u_0`$ et $`r`$ suivis des deux entiers naturels ***i*** et ***j*** avec ***i***<***j***.

> Sortie : La valeur de la somme $`u_i+u_{i+1}+\dots+u_{j-1}+u_j`$ où $`(u_n)`$ est une suite arithmétique.


@[Calcul de la somme des termes d'une suite arithmétique]({"stubs": ["Premiere/Suites/Calcul_somme_arithmetique.py"], "command": "python3 Premiere/Suites/Calcul_somme_arithmetique_Test.py"})

---

## Exercice n° 10 : Calcul de la somme des termes d'une suite géométrique
`Difficulté : Facile`  
`Programme officiel`  

Le but de cet exercice est de faire une fonction qui calcule la valeur de la somme $`u_i+u_{i+1}+\dots+u_{j-1}+u_j`$ pour des valeurs entières de ***i*** et ***j*** données dans le cas où $`(u_n)`$ est une suite géométrique de premier terme $`u_0`$ et de raison $`q`$.

> Entrée : Les valeurs de $`u_0`$ et $`q`$ ($`q\neq 1`$) suivis des deux entiers naturels ***i*** et ***j*** avec ***i***<***j***.

> Sortie : La valeur de la somme $`u_i+u_{i+1}+\dots+u_{j-1}+u_j`$ où $`(u_n)`$ est une suite géométrique.


@[Calcul de la somme des termes d'une suite géométrique]({"stubs": ["Premiere/Suites/Calcul_somme_geometrique.py"], "command": "python3 Premiere/Suites/Calcul_somme_geometrique_Test.py"})

---

## Exercice n°11 Somme de termes d'une suite 
`Difficulté  : Facile` 
`Origine :` [`Hackerrank`](https://www.hackerrank.com/challenges/summing-the-n-series/problem)

On pose $`T_n = n^2 - (n-1)^2`$ ainsi que $`S_n = T_1+ T_2 + T_3+... + T_n`$.

Etant donné ***n***, afficher la valeur de $`S_n`$.

> Entrée : La valeur de l'entier naturel non nul ***n***.

> Sortie : La valeur de $`S_n`$.

@[Somme de termes d'une suite]({"stubs": ["Variables_et_fonctions/Somme_telescopique.py"], "command": "python3 Variables_et_fonctions/Somme_telescopique_Test.py"})

---

## Exercice n° 12 : Recherche de seuil I
`Difficulté : Facile`  
`Programme officiel`

On considère la suite définie par $`u_{n+1}=0.5.u_n`$ et de premier terme $`u_0`$. Plus la valeur de ***n*** augmente, plus les valeurs de $`u_n`$ se rapprochent de 0.

Le but de cet exercice est de faire un programme qui permet de déterminer pour un réel positif ***e*** donné, quel est le plus petit entier ***n*** tel que la valeur de $`u_n`$ soit inférieure à ***e***.

> Exemple : si ***e=0,2*** et $`u_0=1`$. Comme $`u_1=0.5`$, $`u_2=0.25`$ et $`u_3=0,125`$, on voit que le plus petit entier tel que $`u_n<e`$ est ***n=3***.

> Entrée : Un réel positif $`u_0`$ et un réel strictement positif ***e***

> Sortie : Le plus petit entier tel que $`u_n<e`$

::: Indications
On pourra regarder le cours sur le boucles `while`
:::

@[Recherche de seuil 1]({"stubs": ["Les_boucles/Recherche_de_seuil.py"], "command": "python3 Les_boucles/Recherche_de_seuil_Test.py"})

---

## Exercice n° 13 : Recherche de seuil II
`Difficulté : Facile`  
`Programme officiel`

On considère désormais la suite définie par $`u_{n+1}=2.u_n`$ et de premier terme $`u_0`$.
Cette suite augmente indéfiniment lorsque ***n*** augmente.

On se demande à partir de quel rang cette suite pourra dépasser une valeur ***e*** donnée en entrée.
Ecrire un programme qui donnera la plus petite valeur de ***n*** telle que $`u_n\geq e`$.

> Entrée : Deux réels $`u_0`$ et ***e***.

> Sortie : Le plus petit entier ***n*** tel que $`u_n>e`$. S'il n'en existe pas, afficher "IMPOSSIBLE".

::: Indications
Il faut considérer 3 cas : 
- Si $`u_0\geq e`$ car la réponse est ...
- Si $`u_0\leq 0`$ car la réponse est ...
- Le reste des cas où il faut calculer la réponse.
:::

@[Recherche de seuil 1]({"stubs": ["Les_boucles/Recherche_de_seuil2.py"], "command": "python3 Les_boucles/Recherche_de_seuil2_Test.py"})

---

## Exercice n° 14 : Recherche de seuil III (Escargot de Gardner)
`Difficulté : Facile`

Nous allons nous intéresser à la progression de l'escargot  de Gardner. Je vous renvoie vers cette vidéo pour une présentation : [Youtube](https://www.youtube.com/watch?v=L1vDkUziBpw).

En résumé, ce qui va nous intéresser ici est que la ***n***-ieme heure, le pourcentage de progression de l'escargot sur l’élastique augmente de $`\frac 1 n `$.
Autrement dit, le pourcentage de progression  la ***n***-ieme heure est $`1+\frac 1 2+\frac 1 3+\dots+\frac 1 n`$.
On se demande naturellement au bout de combien de temps ce pourcentage de progression dépassera une valeur donnée ***e***.

Écrire un programme qui prend en entrée une valeur ***e*** et affiche en sortie la plus petite valeur de ***n*** pour laquelle le pourcentage de progression dépasse ***e***.

> Entrée : Un nombre strictement positif ***e*** pas trop grand (regarder la vidéo pour comprendre pourquoi).

> Sortie : La plus petite valeur de ***n*** tel que $`1+\frac 1 2+\frac 1 3+\dots+\frac 1 n >e`$.

@[Escargot de Gardner]({"stubs": ["Les_boucles/Gardner.py"], "command": "python3 Les_boucles/Gardner_Test.py"})

---

## Exercice n° 15 : Factorielle
`Difficulté : Facile`  
`Programme officiel`

En mathématiques, il est fréquent que l'on ait besoin de calculer $`1\times2\times3\times4\times\dots\times n`$. On note le résultat ***n!*** et on le nomme factorielle de n.

Ainsi, on a 
+ $`3!=1\times2\times3= 6`$, 
+ $`4!=24`$, 
+ $`5!=120`$, 
+ $`1!=1`$. 
+ Par convention, $`0!=1`$.

Le but de cet exercice est tout simplement d'afficher la factorielle du nombre ***n*** donné en entrée.

> Entrée : Un entier naturel ***n*** .

> Sortie : Afficher ***n!*** .

@[Factorielle]({"stubs": ["Les_boucles/Factorielle.py"], "command": "python3 Les_boucles/Factorielle_Test.py"})

 ---
 
 ## Exercice n° 16 : Afficher les termes d'une suite
 `Difficulté : moyenne`
 `Prérequis : Listes et matplotlib`
 
 Compléter le script suivant pour qu'il affiche les 10 premiers termes de la suite $`(u_n)`$ définie par $`u_0=10`$ et $`u_{n+1}=\dfrac 1 2 u_n + 2`$. 
 
Pour cela, on utilisera la fonction `plt.scatter(X,Y)` où X représente la liste des abscisses des points que l'on souhaite tracer et Y la liste des ordonnées. On pourra voir le [cours](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/cours---representation-graphique-avec-matplotlib) sur le module matplotlib pour plus d'information.

@[Tracé des termes d'une suite]({"stubs": ["Premiere/Suites/Trace_suite.py"], "command": "python3 Premiere/Suites/Trace_suite_Test.py"})
 
 ---

## Compléments :

Pour ne pas surcharger cette page, voici quelques approfondissements possibles disponibles sur d'autres pages :
- [Programmer des suites de manière récursive](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/suites-recurrentes)
- [La suite de Syracuse](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/suite-de-syracuse)
- [La suite de Van Eck](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/suite-de-van-eck)
- [Systèmes proies-prédateurs (Volterra)](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/systeme-proie-predateur)

