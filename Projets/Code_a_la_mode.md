# Combat d'IA : Code à la mode

Remarque pratique : N'hésitez pas à mettre en mode plein ecran (bouton au dessus du code à droite) et réduire le zoom pour mieux voir.

[Voici le lien pour accéder directement au jeu.](https://www.codingame.com/multiplayer/bot-programming/code-a-la-mode)

Vous pourrez trouver une introduction générale en vidéo sur les combats d'IA sur le site Codingame ainsi qu'une présentation de ce kit de démarrage en [cliquant sur ce lien](https://youtube.com/playlist?list=PLSvpVr2aLOBc9AJ1P-Oy98bT1ay-ENUet). 


## Présentation

Ce combat d'IA est très intéressant dans le cadre d'un projet avec les élèves car il demande assez peu de connaissances théoriques pour y participer pleinement. Le plus difficile est la bonne gestion des entrées pour les rendre utilisables facilement. Le coeur de l'IA est un enchainement de conditions qui peuvent être facilement gérés par les élèves.  
Un objectif raisonnable peut être de viser un bon classement dans la ligue Bronze voire, pour les meilleurs, passer en ligue Or.

Jusqu'à la ligue Bronze, il suffira de s'adapter aux différents ajouts qui apparaitront à chaque changement de ligue. Donc le but pour arriver à la ligue Bronze est simplement de faire un code propre pour répondre aux attentes. Pour progresser ensuite, il faudra chercher à optimiser un peu plus.

## Kit de démarrage 

Vous pouvez trouver sur votre droite un kit de démarrage pour ce combat d'IA (Il y a une version avec ou sans POO). Il suffit de le copier coller à la place du code de base sur le site Codingame. Ce kit est largement inspiré par celui fourni pour ce challenge, la principale différence est qu'il est traduit. Bien sûr ce kit de démarrage n'est ni un obligation ni la perfection. On peut très bien s'en passer et même si on l'utilise, il faudra de toute façon s'en éloigner pour réussir à monter haut dans le classement. Il n'a pas d'autre but que d'aider à démarrer ceux qui en auraient besoin.

Donnons quelques explications sur le code.

### La fonction auxiliaire

La fonction `log` ne sert à rien pour le jeu mais c'est de loin la plus utile de toute car elle permet de chercher ses erreurs. En effet, elle permet d'afficher des variables comme un message d'erreur (donc en rouge) sans que cela soit pris comme une réponse et sans arrêter le jeu (comme si on affichait un commentaire).

### Les constantes et variables

Une bonne habitude à prendre : Traduire les données de l'énoncé en constantes faciles à retenir. Impossible de ne pas se mélanger les pinceaux entre toutes les lettres qui correspondent aux noms des tables et aux différents objets du jeu. Le plus simple est de créer des constantes parlantes. On fera de même avec les fonctions de manière à se que donner l'ordre d'utiliser le four ressemble à `utiliser(donner_case(FOUR))` plutôt qu'à `print("MOVE",abscisse("O"), ordonnée("O"))`. Dans le premier cas, même quelqu'un qui n'a jamais lu votre code comprendra ce que ça fait alors que dans le second c'est moins évident...

Après les constantes, se trouvent l'initialisation des principales variables utilisées. Cela permet de regrouper au même endroit les noms que l'on va utiliser pour les retrouver plus rapidement en cas de trou de mémoire. 

Une remarque sur les variables liées aux cases : L'idée est de faire comme si on numérotait les cases de 0 à 76 et de mettre dans différentes listes les propriétés liées aux cases. Par exemple tous les noms des cases sont dans la liste `cases_nom` et pour récupérer celui de la cases numéro 3 par exemple, il suffira d'écrire `cases_nom[3]`. `cases_x` et `cases_y` regroupent respectivement la première et la seconde coordonnées. On remarquera que l'ordonnée en informatique est dirigée très souvent vers le bas contrairement aux ordonnées mathématiques.

### Les fonctions pour le jeu

On donne quelques fonctions utiles pour créer une intelligence artificielle plus facilement. Par exemple si on veut aller chercher de la vaisselle, on devra d'abord déterminer à quelle numero de case correspond le lave-vaisselle (en utilisant la fonction `donner_case_par_nom(LAVE_VAISSELLE)`) puis à l'utiliser ce qui donnera au final : `utiliser(donner_case_par_nom(LAVE_VAISSELLE))`.

### Récupération des entrées

Maintenant qu'on a nos constantes, variables et fonctions, il faut gérer toutes les informations liées au jeu qui nous sont envoyées (avec la fonction `input()`) et remplir nos variables. C'est le rôle de toutes les lignes entre 100 et 170 environ. Normalement, vous n'aurez pas à y toucher avant la ligue bois 1 dans laquelle il faudra gérer ce qu'il y a dans le four.

### La logique du jeu : l'IA

Enfin, maintenant qu'on a toutes les données utiles, on peut s'attaquer au jeu. C'est ici que commence le travail. Le code a déjà été prérempli pour collecter d'abord une assiette et ensuite une glace et quand c'est fait, il attend. A vous de le compléter pour qu'il fasse ce qu'il faut pour réussir les commandes des clients.  

C'est ici qu'on peut apprécier l'utilisation de noms parlant pour les constantes, variables et fonctions. En effet, en lisant simplement le code, on comprend bien ce qu'il fait. On peut ainsi se concentrer sur la logique du jeu et pas sur le dechiffrage d'une ligne de code à la signification obscure. 


Bon jeu !


@[Inutile d'appuyer sur Run]({"stubs":["Projets/Code_a_la_mode.py","Projets/Code_a_la_mode_avec_classes.py"], "command": "python3 Projets/Code_a_la_mode_Test.py", "layout": "aside"})
