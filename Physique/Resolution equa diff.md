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
