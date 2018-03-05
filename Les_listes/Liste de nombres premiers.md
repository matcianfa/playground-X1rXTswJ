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

@[Liste des nombres premiers]({"stubs": ["Les_listes/liste_nombres_premiers1.py", "Les_listes/Est_entier.py], "command": "python3 Les_listes/liste_nombres_premiers1_Test.py"})

