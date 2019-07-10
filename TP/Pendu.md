# Le jeu du pendu
`Prérequis principaux : conditions, boucles et chaines de caractères`  
`Difficulté : Facile`

Le but de ce TP est de créer des fonctions auxiliaires pour pouvoir créer, au final, un jeu du pendu.

## Fonction d'espacement

Tout d'abord, nous aurons besoin d'afficher correctement nos mots et pour cela, nous allons devoir espacer chaque lettre.

Créer ci-dessous une fonction `espacer(mot)` qui prend en entrée un chaine de caractère `mot` et qui renvoie en sortie les mêmes lettres espacées toutes d'un espace.

> Exemple : `espacer("PYTHON")` doit renvoyer "P Y T H O N".

@[Espacer]({"stubs": ["TP/espacer.py"], "command": "python3 TP/espacer_Test.py"})

---
## Ajouter une lettre

Passons maintenant au coeur du jeu. Durant la partie il y a d'un côté le `mot_choisi` au hasard dans le dictionnaire qui ne change pas et de l'autre le `mot_partiel` où certaines lettres non encore trouvées seront représentées par des tirets bas ***_***. Par exemple si le `mot_choisi` est "MAISON", au début le `mot_partiel` sera " _ _ _ _ _ _ " (Les espaces n'y sont normalement pas, c'est juste pour visualiser mieux). Si on choisit la lettre S, le `mot_partiel` deviendra " _ _ _ S _ _ ". Si on choisit le A, le `mot_partiel` deviendra " _ A _ S _ _ " etc.

Créer une fonction `ajouter_lettre(lettre,mot_partiel,mot_choisi)` qui prend en entrée une `lettre`, le `mot_partiel` partiellement trouvé et `mot_choisi` au départ et renvoie en sortie le `mot_partiel` complété en rajoutant la `lettre` partout où elle apparait dans le `mot_choisi` (donc si elle n'apparait pas, on renvoie `mot_partiel` inchangé).

@[Ajouter une lettre]({"stubs": ["TP/ajouter_lettre.py"], "command": "python3 TP/ajouter_lettre_Test.py"})

## Le jeu !

Passons maintenant aux choses sérieuses : le jeu ! 

Copier-coller les deux fonctions précédentes dans la fenêtre ci-dessous et lancer pour tester le jeu.

Remarques : 
- Vous pouvez voir dans le second onglet le code qui se lance pour le jeu.
- Pour mieux voir, vous pouvez agrandir la fenetre du terminal dans le coin en bas à droite
- Pour des raisons techniques dues au fonctionnement du site, il faut jouer rapidement sinon le script s'arrête.

@[Le jeu du pendu]({"stubs": ["TP/pendu.py","TP/pendu_Test.py"], "command": "python3 TP/pendu_Test.py", "terminal": true})
`
