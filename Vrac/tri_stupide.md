# Le tri stupide
`Difficulté : Moyenne`

Nouos avons déjà vu des méthodes de tris dans des exercices précédents. Nous allons ici nous intéresser à une méthode de tri extrêmement peu efficace qui consiste à mélanger notre liste au hasard tant qu'elle n'est pas bien triée. C'est comme si on jetait un paquet de carte en l'air jusqu'à ce qu'il soit bien trié... Ca peu prendre du temps...

Nous allons procéder par étape :
1. D'abord nous allons créer une fonction ***est_triée*** qui renvoie si la liste est bien triée.
2. Ensuite nous allons créer une fonction ***mélanger*** qui mélangera les éléments de la liste.
3. Enfin nous créerons le programme qui tri la liste (ou plutôt qui essaye de trier).

### Vérifier si une liste est triée

Créer un programme ***est_triée*** qui prend en entrée une ***liste*** puis qui renvoie `True` si elle est triée dans l'ordre croissant et `False` sinon.

> Entrée : Une ***liste*** .

> Sortie : Renvoie (avec `return`) `True` si ***liste*** est bien triée et  `False` sinon.

@[Créer une fonction est_triée]({"stubs": ["Vrac/est_triee.py"], "command": "python3 Vrac/est_triee_Test.py"})

---

### Mélange d'une liste

Pour mélanger une ***liste*** de longueur ***n***, nous allons procéder de la manère suivante :
1. On part du dernier élément de la liste (donc celui d'indice ***n***-1). 
2. On choisit un nombre k au hasard entre 0 et ***n***-1 et on échange ***liste***[k] et ***liste***[n-1].
3. On recommence mais cette fois ci en considérant l'avant-dernier  et un nombre ***k*** choisi entre 0 et ***n*** - 2 puis ensuite on recommence avec l'avant avant dernier etc. jusqu'à l'élément d'indice 1.

Ce mélange s'appelle mélange de Fisher-Yates. On peut trouver des précisions sur [Wikipédia](https://fr.wikipedia.org/wiki/M%C3%A9lange_de_Fisher-Yates)

Créer un programme ***mélanger*** qui prend en entrée une ***liste*** et renvoie une liste mélangée par cette méthode.

::: Aide
+ Pour choisir un nombre aléatoirement entre 0 et n, on peut utiliser la fonction `randint(0,n)`.
+ Pour échanger des valeurs a et b, il suffit d'écrire `a,b=b,a`.
:::

> Entrée : Une ***liste***.

> Sortie : Renvoyer (avec `return`) la ***liste*** mélangée.

@[Créer une fonction mélanger]({"stubs": ["Vrac/melanger.py"], "command": "python3 Vrac/melanger_Test.py"})

---

### Le tri stupide

Maintenant qu'on a nos deux sous-fonctions, on peut créer un programme qui tri notre liste en procédant de la manière suivante :
1. Tant que la liste n'est pas triée, on mélange la liste.
2. Quand on trouve la liste triée, on la renvoie (avec `return`)

Copiez collez vos deux programmes précédents puis créez le programme qui renvoie la liste triée par une méthode de tri stupide.

> Entrée : une ***liste***.

> Sortie : Une liste triée dans les temps (si on a de la chance).


@[Créer une fonction qui trie]({"stubs": ["Vrac/tri_stupide.py"], "command": "python3 Vrac/tri_stupide_Test.py"})
