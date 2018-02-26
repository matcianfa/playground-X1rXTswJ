## Triangles constructibles

Si on choisit 3 nombres, il n'est pas toujours possible de construire un triangle ayant pour longueur ces nombres.
Par exemple, il est impossible de construire un triangle de côtés de longueurs 1, 1 et 5. 

Un triangle est constructible si pour chaque coté, sa longueur est inférieur à la somme des longueurs deux autres cotés.

Le but de cet exercice est de créer un programme qui nous dit si le triangle est constructible ou pas à partir des longueurs qui nous sont données.

> Entrée : Trois longueurs ***a***, ***b*** et ***c***.

> Sortie : Affiche "CONSTRUCTIBLE" si on peut construire un triangle ayant des cotés de ces trois longueurs ou bien "PAS CONSTRUCTIBLE" sinon.
> Pour les plus rapides, vous pouvez afficher "PLAT" si le triangle qu'on peut construire est plat.

@[Triangles constructibles ?]({"stubs": ["Les_conditions/Triangles_constructibles.py"], "command": "python3 Les_conditions/Triangles_constructibles_Test.py"})
