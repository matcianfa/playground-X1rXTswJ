# Le tri stupide

Nouos avons déjà vu des méthodes de tris dans des exercices précédents. Nous allons ici nous intéresser à une méthode de tri extrêmement peu efficace qui consiste à mélanger notre liste au hasard tant qu'elle n'est pas bien triée. C'est comme si on jetait un paquet de carte en l'air jusqu'à ce qu'il soit bien trié... Ca peu prendre du temps...

Nous allons procéder par étape :
1. D'abord nous allons créer une fonction ***est_triée*** qui renvoie si la liste est bien triée.
2. Ensuite nous créerons le programme qui tri la liste (ou plutôt qui essaye de trier).

### Vérifier si une liste est triée

Créer un programme ***est_triée*** qui prend en entrée une ***liste*** puis qui renvoie `True` si elle est triée dans l'ordre croissant et `False` sinon.

> Entrée : Une ***liste*** .

> Sortie : Renvoie (avec `return`) `True` si ***liste*** est bien triée et  `False` sinon.

@[Créer une fonction est_triée]({"stubs": ["Vrac/est_triee.py"], "command": "python3 Vrac/est_triee_Test.py"})

---

### Tri de la liste

