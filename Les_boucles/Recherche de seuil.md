## Recherche de seuil

### Premier exercice

On considère la suite définie par $`u_{n+1}=0.5.u_n`$ et de premier terme $`u_0`$. Plus la valeur de ***n*** augmente, plus les valeurs de $`u_n`$ se rapprochent de 0.

Le but de cet exercice est de faire un programme qui permet de déterminer pour un réel positif ***e*** donné, quel est le plus petit entier ***n*** tel que la valeur de $`u_n`$ soit inférieure à ***e***.

Par exemple : si ***e=0,2*** et $`u_0`=1$. Comme $`u_1=0.5`$, $`u_2=0.25`$ et $`u_3=0,125`$, on voit que le plus petit entier tel que $`u_n<e`$ est ***n=3***.

> Entrée : Un réel positif $`u_0`$ et un réel strictement positif ***e***

> Sortie : Le plus petit entier tel que $`u_n<e`$

@[Recherche de seuil 1]({"stubs": ["Les_boucles/Recherche_de_seuil.py"], "command": "python3 Les_boucles/Recherche_de_seuil_Test.py"})

---

### Second exercice

On considère désormais la suite définie par $`u_{n+1}=2.u_n et de premier terme $`u_0`$.
Cette suite augmente indéfiniment lorsque ***n*** augmente.

On se demande à partir de quel rang cette suite pourra dépasser une valeur ***e*** donnée en entrée.
Ecrire un programme qui donnera la plus petite valeur de ***n*** telle que $`u_n>e`$.

> Entrée : Deux réels $`u_0`$ et ***e***.

> Sortie : Le plus petit entier ***n*** tel que $`u_n>e`$. S'il n'en existe pas, afficher "IMPOSSIBLE".

@[Recherche de seuil 1]({"stubs": ["Les_boucles/Recherche_de_seuil2.py"], "command": "python3 Les_boucles/Recherche_de_seuil2_Test.py"})
