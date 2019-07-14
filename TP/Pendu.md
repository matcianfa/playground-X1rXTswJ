# Le jeu du pendu
`Prérequis principaux : conditions, boucles et chaines de caractères`  
`Difficulté : Facile`

Le but de ce TP est de créer des fonctions auxiliaires pour pouvoir créer, au final, un jeu du pendu.

Une remarque qui pourra peut-être être utile lors des tests : le dictionnaire utilisé est celui des mots courants entre 7 et 11 lettres. Voici le [lien](https://github.com/matcianfa/playground-X1rXTswJ/blob/master/python-project/TP/dictionnaire7-10.txt)

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

# Le pendu (version avec triche)
`Difficulté : Difficile à très difficile`  
`Prérequis : Les listes`


Qui n'a pas déjà pensé à changer de mot au fur et à mesure que la personne propose des lettres ? C'est ce que nous allons programmer maintenant. 

Cette partie est beaucoup plus difficile que la précédente et plusieurs réponses plus ou moins efficaces peuvent être trouvées. En effet, selon la stratégie choisie, la personne qui jouera peut peut-être trouver une stratégie pour gagner quand même. Il peut donc être intéressant de former deux groupes et chaque groupe devra à la fois créer une façon de faire perdre le joueur en choisissant bien les mots au fur et à mesure et aussi trouver une stratégie pour gagner quand il joue au jeu créé par l'autre groupe. Une sorte de duel de pendus pour savoir qui triche le mieux.

## Donner un mot

Commençons par la fin : Supposons que la personne ait perdu, il faut lui donner un mot possible qu'elle aurait dû trouvé en tenant compte des lettres qu'elle a proposé.

Créer une fonction `donner_solution(lettres,mot_partiel,dictionnaire)` qui prend en entrée la liste des `lettres` proposées pendant le jeu, le `mot_partiel` qui correspond à l'état final du jeu (par exemple " _ A I _ _ _ " (sans les espaces)) ainsi que le `dictionnaire` des mots possibles sous forme de liste de mots. En sortie, la fonction doit renvoyer un (et un seul) mot du `dictionnaire` écrit en remplaçant les tirets bas _ qui sont dans `mot_partiel` par des lettres non encore utilisées (c'est à dire qui ne sont pas dans `lettres`).  
On renverra le mot vide "" s'il n'y a pas de réponses possibles.

> Exemple : Si `lettres=["U","A","I","X","Z","C","Y","V","K"]`, `mot_partiel="_AI___"` et le dictionnaire serait la liste des mots français. Alors on pourrait renvoyer "MAISON" ou "FAITES" mais pas "LAITUE" (car "U" a été proposé) ni "FAISAN" (car le "A" a été proposé et n'apparaissait qu'une fois en seconde position dans `mot_partiel`) ni "FAITS" (car il n'y a pas le bon nombre de lettres)

> Remarque : On teste juste que le mot proposé par la fonction vérifie les regles du jeu, pas si la stratégie est bonne ou pas.

@[Donner un mot]({"stubs": ["TP/donner_solution.py"], "command": "python3 TP/donner_solution_Test.py"})

---

## Ajouter une lettre

Passons maintenant au coeur du problème : Que faire quand une lettre est proposée par le joueur ? Il ne suffit clairement pas de dire qu'il a faux car s'il propose toutes les voyelles, il faudra bien en placer quelques unes. A vous de trouver une bonne stratégie pour pouvoir trouver les meilleures positions pour faire durer le plus longtemps possible le jeu.

Vous devez donc créer une nouvelle fonction `ajouter_lettre(lettre,lettres_proposees,mot_partiel,dictionnaire)` qui prend en entrée la nouvelle `lettre` que propose le joueur, la liste des `lettres_proposees` déjà utilisées pendant le jeu, le `mot_partiel` qui correspond à l'état final du jeu (par exemple " _ A I _ _ _ " (sans les espaces)) ainsi que le `dictionnaire` des mots possibles sous forme de liste de mots. En sortie on attend le nouveau `mot_partiel` à afficher.

> Remarque : On teste juste que le mot proposé par la fonction vérifie les regles du jeu, pas si la stratégie est bonne ou pas.

@[Ajouter une lettre]({"stubs": ["TP/ajouter_lettre_2.py"], "command": "python3 TP/ajouter_lettre_2_Test.py"})

---

## Le jeu (version avec triche)

On peut à présent passer au jeu : Copier coller les deux fonctions précédentes pour tester votre jeu.

@[Le jeu du pendu]({"stubs": ["TP/pendu_triche.py","TP/pendu_triche_Test.py"], "command": "python3 TP/pendu_triche_Test.py", "terminal": true})



