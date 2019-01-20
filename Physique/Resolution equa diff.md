# Résolution numérique d'équations différentielles ordinaires

Le but de cette page est présenter quelques applications possibles en cours de physique de la résolution numérique d'équations differentielles ordinaires en python. Pour cela, nous allons utiliser la fonction odeint du module scipy

# Equations différentielles d'ordre 1 

Commençons simplement par une équation de la forme $`y'=a.y`$ comme on peut croiser en étudiant la radioactivité par exemple.

@[Résolution d'une équation différentielle d'ordre 1]({"stubs": ["Physique/radioactivite.py"], "command": "python3 Physique/radioactivite_Test.py"})

Détaillons le code :
- On définit le temps sur lequel on veut intégrer notre équation différentielle sous forme de liste en utilise `np.linspace(t_initial,t_final,nombre_de_t)`. Plus `nombre_de_t` sera grand, plus la résolution sera précise.
- Pour résoudre l'équation différentielle, il faut expliquer à `odeint` que vaut la dérivée en fonction de `y`et du temps (qui ici n'intervient pas directement mais les coefficients pourraient dépendre du temps par exemple). On explique donc cela sous forme de fonction appelée ici `equation`.
- On résout l'équation différentielle avec `odeint( fonction, valeurs_initiales, temps)`. On met comme fonction celle définie dans le point précédent. Les valeurs initiales doivent être donnée sous forme de liste.
- Enfin on affiche le résultat avec matplotlib

# Equations différentielles d'ordre 2

Ca va se compliquer un peu : la fonction `odeint` se sait résoudre que des équations d'ordre 1 mais peut en résoudre plusieurs d'un coup. Autrement dit, on peut résoudre $`Y'=A.Y`$ où $`Y`$ est un vecteur et $`A`$ une matrice.  
Ainsi, si on veut résoudre l'équation différentielle $`y" = a.y`$, on va poser $`Y=\left(\begin{array}{c} y \\ y' \end{array}\right)`$  et notre équation d'ordre 2 se ramène à résoudre $`Y'=\left(\begin{array}{c} y' \\ a.y \end{array}\right)`$.  
Ce qui nous donnerait comme code :

@[Résolution d'une équation différentielle d'ordre 2]({"stubs": ["Physique/ordre2.py"], "command": "python3 Physique/ordre2_Test.py"})

Détaillons les changements par rapport à l'ordre 1 :
- Cette fois-ci, dans la fonction `equation`, Y désigne un vecteur qu'on explicite par la commande (y,dy)=Y pour pouvoir les utiliser par la suite les valeurs y et dy.  
On explicite ce qu'elle renvoit c'est à dire $`Y'`$ comme expliqué juste avant.
- `odeint` attend comme pour l'ordre 1 une fonction qui caractérise l'équation différentielle, des valeurs initiales et la liste des temps mais cette fois-ci renvoit la liste des couples (y,dy) pour chaque temps. Or en général on veut les valeurs de y d'un coté et les valeurs de dy de l'autre. Pour cela, on rajoute `.T` (qui fait simplement une transposition) à la fin de la ligne.

# Applications

Une fois bien maitrisé l'ordre deux, la seule réelle restriction dans les applications est notre imagination. Voyons quelques exemples.

## Mouvement d'une planète

Voici par exemple le mouvement d'une planète autour d'un soleil si on ne considère que la force de gravitation provenant du soleil. On place l'origine du repère sur le soleil. Le programme qui suit n'a rien de réaliste dans le sens où toutes les constances valent 1 mais il suffit de l'adapter en fonction de ce que l'on veut étudier, le but ici étant de voir comment utiliser la fonction `odeint`

@[Mouvement d'une planète]({"stubs": ["Physique/planete.py"], "command": "python3 Physique/planete_Test.py"})

Remarque : Ici, pour résoudre, on décompose selon les axes x et y et on résout en réalité en même temps les équations en x et en y qu'on ramène à de l'ordre 1. On se ramène donc à une équation différentielle d'ordre 1 mais d'un vecteur de dimension 4.

---

## Etude du mouvement d'un projectile

Etudions le mouvement d'un projectile en considérant d'un coté le mouvement sans frottement et de l'autre avec frottement pour pouvoir les comparer.

@[Mouvement d'un projectile]({"stubs": ["Physique/projectile.py"], "command": "python3 Physique/projectile_Test.py"})
