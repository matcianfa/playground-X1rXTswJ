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

> Entrée : Les valeur de ***a***, ***b***, $`u_0`$ et ***n***.

> Sortie : La valeur de $`u_n`$.

@[Calcul des termes d'une suite]({"stubs": ["Les_boucles/Calcul_terme_suite2.py"], "command": "python3 Les_boucles/Calcul_terme_suite2_Test.py"})

---

