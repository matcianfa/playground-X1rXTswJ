# Classe de Première - Suites numériques

## Exercice n° : Calcul des termes d'une suite définie par $`u_n=f(n)`$
`Difficulté : Très facile`

On considère la suite $`(u_n)`$ définie pour tout entier naturel $`n`$ par $`u_n=\dfrac{3n-9}{2n+1}`$.

Créer une fonction qui prend en entrée un entier naturel $`n`$ et renvoie en sortie la valeur de $`u_n`$.

> Entrée : Un entier naturel $`n`$.

> Sortie : Le programme doit afficher la valeur de $`u_n`$ définie ci-dessus.

@[Calcul des termes d'une suite]({"stubs": ["Premiere/Suites/Calcul_terme1.py"], "command": "python3 Premiere/Suites/Calcul_terme1_Test.py"})

---

## Exercice n° : Calcul des termes d'une suite définie par récurrence I
`Difficulté : Facile`

Pour calculer à l'aide d'un programme les termes d'une suite définie par récurrence, l'idée est tout simplement de calculer au fur et à mesure les valeurs de la suite en les sauvegardant dans une seule variable ***u*** qui commence à $`u_0`$.

Dans la fenêtre ci-dessous, on a déjà commencé à écrire un programme pour calculer la valeur de $`u_n`$ définie par $`u_0=5`$ et $`u_{n+1}=2u_n-3`$. Remplacez les @ par ce qu'il faut pour que le programme fonctionne.

> Entrée : Un entier ***n***.

> Sortie : Le programme doit afficher la valeur de $`u_n`$ définie ci-dessus.

@[Calcul des termes d'une suite]({"stubs": ["Les_boucles/Calcul_terme_suite0.py"], "command": "python3 Les_boucles/Calcul_terme_suite0_Test.py"})

---

## Exercice n° : Calcul des termes d'une suite définie par récurrence II
`Difficulté : Facile`

Dans cet exercice, on considère une suite u définie par $`u_{n+1}=3-4u_n`$ et de premier terme $`u_0`$.
Le but de cet exercice est de créer un programme qui prend en entrée les valeurs de ***n*** et $`u_0`$ et affiche la valeur de $`u_n`$.

> Entrée : Un entier ***n*** et $`u_0`$.

> Sortie : La valeur de $`u_n`$.

@[Calcul des termes d'une suite]({"stubs": ["Les_boucles/Calcul_terme_suite0_5.py"], "command": "python3 Les_boucles/Calcul_terme_suite0_5_Test.py"})

---

## Exercice n° : Calcul des termes d'une suite définie par récurrence III
`Difficulté : Facile`

Dans cet exercice, on considère une suite u définie par $`u_{n+1}=u_n+n+1`$ et de premier terme $`u_0`$.
Le but de cet exercice est de créer un programme qui prend en entrée les valeurs de ***n*** et $`u_0`$ et affiche la valeur de $`u_n`$.

> Entrée : Un entier ***n*** et $`u_0`$.

> Sortie : La valeur de $`u_n`$.

@[Calcul des termes d'une suite]({"stubs": ["Les_boucles/Calcul_terme_suite1.py"], "command": "python3 Les_boucles/Calcul_terme_suite1_Test.py"})

---

## Exercice n° : Calcul des termes d'une suite définie par récurrence IV
`Difficulté : Facile`

Le but de cet exercice est de calculer les termes de la suite définie par $`u_{n+1}=a.u_n+b`$ et de premier terme $`u_0`$.

> Entrée : Les valeurs de ***a***, ***b***, $`u_0`$ et ***n***.

> Sortie : La valeur de $`u_n`$.

@[Calcul des termes d'une suite]({"stubs": ["Les_boucles/Calcul_terme_suite2.py"], "command": "python3 Les_boucles/Calcul_terme_suite2_Test.py"})

---

## Exercice n° : Calcul des termes d'une suite définie par récurrence V
`Difficulté : Facile`  
`Notion utilisée : Les listes`

Le but de cet exercice est de calculer tous les termes de la suite définie par $`u_{n+1}=u_n^2-5`$ et de premier terme $`u_0=0`$ jusqu'à un certain rang.

> Entrée : Le valeur de ***N*** jusqu'à laquelle on souhaite calculer.

> Sortie : La liste des valeurs de $`(u_n)`$ pour n allant de 0 jusqu'à ***N*** (compris).

@[Calcul des termes d'une suite]({"stubs": ["Premiere/Suites/Calcul_terme2.py"], "command": "python3 Premiere/Suites/Calcul_terme2_Test.py"})

---

## Exercice n° : Calcul de sommes
`Difficulté : Facile`

Le but de cet exercice est de faire une fonction qui calcule la valeur de la somme $`1^p+2^p+3^p+\dots+n^p`$ pour des valeurs de ***n*** et ***p*** données.

> Entrée : Un entier naturel ***n*** et un entier ***p*** (qui peut être négatif).

> Sortie : La valeur de la somme $`1^p+2^p+3^p+\dots+n^p`$.

:::Aide
Pour calculer une somme, il suffit de créer une variable S qui commence à 0 puis, dans une boucle, on rajoute à chaque étape un des termes.
:::

@[Calcul de sommes]({"stubs": ["Les_boucles/Calcul_de_sommes.py"], "command": "python3 Les_boucles/Calcul_de_sommes_Test.py"})

---

## Exercice n° : Calcul de la somme des termes d'une suite géométrique
`Difficulté : Facile`  

Le but de cet exercice est de faire une fonction qui calcule la valeur de la somme $`u_i+u_{i+1}+\dots+u_{j-1}+u_j`$ pour des valeurs entières de ***i*** et ***j*** données dans le cas où $`(u_n)`$ est une suite arithmétique de premier terme $`u_0`$ et de raison $`r`$.

> Entrée : Les valeurs de $`u_0`$ et $`r`$ suivis des deux entiers naturels ***i*** et ***j*** avec ***p***<***q***.

> Sortie : La valeur de la somme $`u_i+u_{i+1}+\dots+u_{j-1}+u_j`$ où $`(u_n)`$ est une suite arithmétique.


@[Calcul de la somme des termes d'une suite arithmétique]({"stubs": ["Premiere/Suites/Calcul_somme_arithmetique.py"], "command": "python3 Premiere/Suites/Calcul_somme_arithmetique_Test.py"})

---


## Exercice n° : Recherche de seuil I
`Difficulté : Facile`

On considère la suite définie par $`u_{n+1}=0.5.u_n`$ et de premier terme $`u_0`$. Plus la valeur de ***n*** augmente, plus les valeurs de $`u_n`$ se rapprochent de 0.

Le but de cet exercice est de faire un programme qui permet de déterminer pour un réel positif ***e*** donné, quel est le plus petit entier ***n*** tel que la valeur de $`u_n`$ soit inférieure à ***e***.

> Exemple : si ***e=0,2*** et $`u_0=1`$. Comme $`u_1=0.5`$, $`u_2=0.25`$ et $`u_3=0,125`$, on voit que le plus petit entier tel que $`u_n<e`$ est ***n=3***.

> Entrée : Un réel positif $`u_0`$ et un réel strictement positif ***e***

> Sortie : Le plus petit entier tel que $`u_n<e`$

@[Recherche de seuil 1]({"stubs": ["Les_boucles/Recherche_de_seuil.py"], "command": "python3 Les_boucles/Recherche_de_seuil_Test.py"})

---

## Exercice n° : Recherche de seuil II
`Difficulté : Facile`

On considère désormais la suite définie par $`u_{n+1}=2.u_n`$ et de premier terme $`u_0`$.
Cette suite augmente indéfiniment lorsque ***n*** augmente.

On se demande à partir de quel rang cette suite pourra dépasser une valeur ***e*** donnée en entrée.
Ecrire un programme qui donnera la plus petite valeur de ***n*** telle que $`u_n>e`$.

> Entrée : Deux réels $`u_0`$ et ***e***.

> Sortie : Le plus petit entier ***n*** tel que $`u_n>e`$. S'il n'en existe pas, afficher "IMPOSSIBLE".

@[Recherche de seuil 1]({"stubs": ["Les_boucles/Recherche_de_seuil2.py"], "command": "python3 Les_boucles/Recherche_de_seuil2_Test.py"})

---

## Exercice n° : Recherche de seuil III (Escargot de Gardner)

Nous allons nous intéresser à la progression de l'escargot  de Gardner. Je vous renvoie vers cette vidéo pour une présentation : [Youtube](https://www.youtube.com/watch?v=L1vDkUziBpw).

En résumé, ce qui va nous intéresser ici est que la ***n***-ieme heure, le pourcentage de progression de l'escargot sur l’élastique augmente de $`\frac 1 n `$.
Autrement dit, le pourcentage de progression  la ***n***-ieme heure est $`1+\frac 1 2+\frac 1 3+\dots+\frac 1 n`$.
On se demande naturellement au bout de combien de temps ce pourcentage de progression dépassera une valeur donnée ***e***.

Écrire un programme qui prend en entrée une valeur ***e*** et affiche en sortie la plus petite valeur de ***n*** pour laquelle le pourcentage de progression dépasse ***e***.

> Entrée : Un nombre strictement positif ***e*** pas trop grand (regarder la vidéo pour comprendre pourquoi).

> Sortie : La plus petite valeur de ***n*** tel que $`1+\frac 1 2+\frac 1 3+\dots+\frac 1 n >e`$.

@[Escargot de Gardner]({"stubs": ["Les_boucles/Gardner.py"], "command": "python3 Les_boucles/Gardner_Test.py"})

---
