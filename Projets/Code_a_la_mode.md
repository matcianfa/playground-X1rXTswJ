# Combat d'IA : Code à la mode

Remarque pratique : N'hésitez pas à mettre en mode plein ecran (bouton au dessus du code à droite) et réduire le zoom pour mieux voir.

[Voici le lien pour accéder directement au jeu.](https://www.codingame.com/multiplayer/bot-programming/code-a-la-mode)

Vous pourrez trouver une introduction générale sur les combats d'IA sur le site Codingame sur une des pages précédentes.

## Présentation

Ce combat d'IA est très intéressant dans le cadre d'un projet avec les élèves car il demande assez peu de connaissances théoriques pour y participer pleinement. Le plus difficile est la bonne gestion des entrées pour les rendre utilisables facilement. Le coeur de l'IA est un enchainement de conditions qui peuvent être facilement gérés par les élèves.  
Un objectif raisonnable peut être de viser un bon classement dans la ligue Bronze voire, pour les meilleurs, passer en ligue Argent.

Jusqu'à la ligue Bronze, il suffira de s'adapter aux différents ajouts qui apparaitront à chaque changement de ligue. Donc le but pour arriver à la ligue Bronze est simplement de faire un code propre pour répondre aux attentes. Pour progresser ensuite, il faudra chercher à optimiser un peu plus.

## Kit de démarrage 

Vous pouvez trouver sur votre droite un kit de démarrage pour ce combat d'IA. Il suffit de le copier coller à la place du code de base sur le site Codingame. Ce kit est largement inspiré par celui fourni pour ce challenge, la principale différence est qu'il est traduit.

Donnons quelques explications sur le code.

### Les fonctions utiles 

La fonction `log` ne sert à rien pour le jeu mais c'est de loin la plus utile de toute car elle permet de chercher ses erreurs. En effet, elle permet d'afficher des variables comme un message d'erreur (donc en rouge) sans que cela soit pris comme une réponse et sans arrêter le jeu (comme si on affichait un commentaire).

### Les constantes

Une bonne habitude à prendre : Traduire les données de l'énoncé en constantes faciles à retenir. Impossible de ne pas se mélanger les pinceaux entre toutes les lettres qui correspondent aux noms des tables et aux différents objets du jeu. Le plus simple est de créer des constantes parlantes. On fera de même avec les fonctions de manière à se que donner l'ordre d'aller à la fenêtre ressemble à `aller(donner_case(FENETRE))` plutôt qu'à `print("MOVE",abscisse("W"), ordonnée("W"))`. Dans le premier cas, même quelqu'un qui n'a jamais lu votre code comprendra ce que ça fait alors que dans le second c'est moins évident...

### Les classes

J'ai gardé le choix fait par les créateurs du jeu de fournir un kit avec des classes. C'est une bonne chose à mon avis. Une autre option aurait été de gérer avec des dictionnaires. Il vaut mieux perdre un peu de temps à s'habituer à des outils un peu moins vus au lycée mais qui permettent de rendre un code beaucoup beaucoup plus clair plutôt que bidouiller avec des listes et vite se noyer dans des codes très peu lisibles. Je profite de la presentation des classes pour rappeler un peu le fonctionnement

+ Pour la classe Joueur, elle permet de conserver ses coordonnées et l'objet qu'il porte. La fonction `__init__` explique ce qui doit être fait lorsqu'on crée un nouvel élément de cette classe. `self` représente l'élément de cette classe (comme on ne connait pas encore le nom du joueur, on met `self` et python remplacera quand il le connaitra).  
Pour créer un joueur nommé alice il suffit de taper `alice=Joueur()`. Si on veut accéder à l'objet qu'elle porte, il suffit d'écrire `alice.objet` et si on veut modifier sa valeur de x, il suffit de taper `alice.x = 3`.  
Cela permet de rendre les choses beaucoup plus lisibles.

+ Pour la classe Case, le fonctionnement est le même à un détail près, la fonction `__init__` a des arguments en plus de `self` qu'il faudra préciser lorsqu'on crée une Case : `case0= Case(1,2,"Four")` créera une case telle que 
`case0.x` vaut 1, `case0.nom` vaut "Four", `case0.objet` vaut None (car par c'est la valeur choisie par défaut ici).  
La fonction `__repr__` permet simplement de choisir ce que l'on veut afficher lorsqu'on fait `print(case0)`. Ici on a choisit d'afficher "Case : Four (1,2)".

+ La classe Jeu est beaucoup plus conséquente en taille. Elle permet de 


@[Inutile d'appuyer sur Run]({"stubs":["Projets/Code_a_la_mode.py"], "command": "python3 Projets/Code_a_la_mode_Test.py", "layout": "aside"})
