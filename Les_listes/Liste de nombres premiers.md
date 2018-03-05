# Liste des nombres premiers
`Difficulté : Moyenne`

Je rappelle qu'un nombre premier est un nombre qui a exactement 2 diviseurs qui sont 1 et lui même. Ainsi 2, 3 ,5 ,7, 11 sont des nombres premiers mais 4, 6, 9 n'en sont pas.

Le but de cette fiche est de créer une liste des nombres premiers donné par différentes méthodes.

### Méthode intuitive

La méthode consiste tout simplement à considérer tous les nombres les uns après les autres. Si le nombre est premier on le met dans notre liste des nombres premiers sinon on passe au suivant.

Nous avons déjà créé une fonction qui permet de savoir si un nombre est premier dans un exercice précédent. Inutile de la recréer ici, une version est disponible sous le nom `est_premier` et vous pouvez l'utiliser directement dans votre programme. Elle renvoie `True` si le nombre est premier et `False` sinon de manière à pouvoir l'utiliser avec un `if`.
Ainsi `est_premier(11)` renvoie `True` alors que `est_premier(12)` renvoie `False`. Vous pouvez voir le code de cette fonction dans le second onglet de l'éditeur Python.

> Entrée : Deux entiers ***a*** et ***b***.

> Sortie : La liste des nombres premiers compris au sens large entre ***a*** et ***b***.

@[Liste des nombres premiers]({"stubs": ["Les_listes/liste_nombres_premiers1.py", "Les_listes/Est_premier.py"], "command": "python3 Les_listes/liste_nombres_premiers1_Test.py"})

---

### Méthode du crible d'Ératosthène

Cette méthode est le contraire de la méthode précédente. Si on veut tous les nombres premiers inférieur à un ***n*** donné, on crée une liste contenant tous les nombres entre 2 et ***n*** puis on commence par retirer de cette liste tous les nombres multiples de 2 (mais pas 2). Ensuite on prend le nombre suivant dans la liste donc 3 et on retire tous les multiples de 3 sauf 3 puis le suivant dans la liste donc 5 (car 4 étant un multiple de 2 il a été retiré) et ainsi de suite jusqu'à $`\sqrt(n)`$ (car les nombres plus grands non premiers ont déjà été écartés).

:::Aide
+ Attention au piège avec la racine carrée en Python. A cause des erreurs d'arrondis, il vaut mieux prendre un peu de marge s'arreter à $`\sqrt(n)+1`$.
:::

> Entrée : Un entier ***n***.

> Sortie : La liste des nombres premiers inférieurs à ***n***.


@[Liste des nombres premiers]({"stubs": ["Les_listes/liste_nombres_premiers2.py"], "command": "python3 Les_listes/liste_nombres_premiers2_Test.py"})

---

Chaque méthode à ses avantages et inconvénients. La seconde est beaucoup plus rapide mais nous oblige à partir de 0 à chaque fois. La première, elle, nous permet de cibler l'intervalle où on cherche nos nombres premiers par exemple dans le cas où on chercherait 10 nombres premiers de 10 chiffres.
