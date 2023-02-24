# Combat d'IA : Code4life

Remarque pratique : N'hésitez pas à mettre en mode plein ecran (bouton au dessus du code à droite) et réduire le zoom pour mieux voir.

[Voici le lien pour accéder directement au jeu](https://www.codingame.com/multiplayer/bot-programming/code4life)

## Présentation

Ce combat d'IA va demander un peu plus de connaissance en programmation qu'un challenge comme Code à la mode. Mais une fois passées les premières difficultés (comme par exemple compréhension du kit de démarrage ou comment programmer la gestion des molecules), c'est surtout la recherche d'une bonne stratégie qui va prévaloir sur le niveau en programmation.
Un objectif raisonnable peut être de viser un bon classement dans la ligue Bronze voire, pour les meilleurs, passer en ligue Argent.

Jusqu'à la ligue Bronze, il va falloir s'adapter aux différents ajouts qui apparaitront à chaque changement de ligue. Donc le but pour arriver à la ligue Bronze est simplement de faire un code propre pour répondre aux attentes. Pour progresser ensuite, il faudra chercher à optimiser un peu plus.

## Kit de démarrage

Vous pouvez trouver sur votre droite un kit de démarrage pour ce combat d'IA. Il suffit de le copier coller à la place du code de base sur le site Codingame. Bien sûr ce kit de démarrage n'est ni un obligation ni la perfection. On peut très bien s'en passer et même si on l'utilise, il faudra de toute façon s'en éloigner pour réussir à monter haut dans le classement. Il n'a pas d'autre but que d'aider à démarrer ceux qui en auraient besoin.

Donnons quelques explications sur le code.

### Les fonctions auxiliaires

La fonction log ne sert à rien pour le jeu mais c'est de loin la plus utile de toutes car elle permet de chercher ses erreurs. En effet, elle permet d'afficher des variables comme un message d'erreur (donc en rouge) sans que cela soit pris comme une réponse et sans arrêter le jeu (comme si on affichait un commentaire).

On donne ensuite une fonction qui détermine le nombre de molécules manquantes de chaque sorte ce qui va servir à savoir quelle molecule on doit prendre. Attention au fait que cette fonction est un point de départ et qu'il va falloir l'adapter au fur et à mesure. Par exemple, elle ne prend pas en compte l'expertise qui va arriver dans les ligues suivantes. 

Si vous avez besoin de créer des fonctions, je vous conseille de les rajouter dans cette partie du code car on se perd très vite dans un code mais structuré.

### Les constantes et variables

Une bonne habitude à prendre : Traduire les données de l'énoncé en constantes faciles à retenir. Par exemple ici, les fichiers peuvent être soit dans les mains des robots soit dans le cloud. Pour les différencier, chaque fichier aura une variable `porteur` qui de base vaut 0, 1 ou -1 selon l'endroit où il se trouve. On peut choisir de conserver dans notre code ces valeurs (ce qui donnerait par exemple `if fichier.porteur == 0 :` dans notre code) ou bien, comme proposé dans le kit, de nommer ces différents types pour que, quand on lit `if fichier.porteur == MOI :` on comprenne de suite qu'on est en train de vérifier si nous somme le porteur du fichier considéré. 

La variable ABCDE est simplement là pour permettre une traduction rapide de la valeur d'une molecule à son nom. En effet il est plus naturel de travailler avec des nombres de 0 à 4 mais quand on va devoir donner nos instructions, il faudra revenir au nom d'origine de la molecule (c'est à dire une lettre entre A et E). Pour cela, si on veut par exemple la molecule associée à 3 (c'est à dire le D puisque le A est associé à 0) il suffira d'écrire `ABCDE[3]`.

Ensuite vient la création de ce que l'on va appeler un Fichier et un Robot qui permettront de stocker les informations de chaque type.  
Nous avons essayé ici de réduire au minimum la programmation orientée objet sans pour autant l'éviter car elle rend ici le code beaucoup plus simple d'utilisation. En effet un Fichier (ou un robot) a plusieurs caractéristiques qui sont détaillées dans la présentation du jeu (à traduction près) : 'id', 'porteur', 'rang', 'vie', 'couts', 'gain_expertise'.  
Pour récupérer les données d'un fichier nommé `a`, il suffira d'écrire `a.id` pour connaitre son id  par exemple ou `a.vie` pour connaitre la vie qu'il va rapporter si on le rend ou encore `a.couts` pour avoir la liste des coûts pour chaque molécule (donc une liste de 5 nombres).

### La récupération des entrées

C'est le but de ce kit de démarrage : déjà gérer la récupération des informations car ce n'est pas très intuitif quand on débute sur Codingame. Il faut juste comprendre que cette partie là du code sert à récupérer l'état du jeu au fur et à mesure qu'il évolue : On récupère l'état du jeu, on joue en fonction ce qui change l'état du jeu etc.  
Il vaut mieux éviter de toucher cette partie du code, du moins au début.

### La logique du jeu 

C'est là qu'il va falloir intervenir. Pour chaque héros, il va falloir renvoyer (avec la fonction `print`) une action.  
Le code de base proposé dans ce kit est le suivant : 
- Si on est en déplacement, il suffit d'attendre 
- Si on n'a rien dans les mains et qu'on n'est pas à l'endroit où on va récupérer les fichiers, alors on y va. Attention au fait que cet endroit change à la ligue bois 1.

On gère ensuite nos cas selon l'endroit où on est :
- Si on est au module SAMPLES : Pour l'instant on ne fait rien car ce module apparait en ligue bois 1
- Si on est au module DIAGNOSIS (qui analyse les données) : Soit on n'a pas assez de fichiers dans les mains alors on prend un fichier, sinon on passe à l'étape suivante.
- Si on est au module MOLECULES : Alors on prend les molécules qu'il nous faut sinon on va au module suivant.
- Si on est au module LABORATORY : Le kit propose d'attendre mais on sent bien que c'est pas le plus utile à faire ici...


## Les différents éléments utilisables 

Voici les principales variables de ce kit contenant les informations du jeu dont vous pouvez avoir besoin :

- `liste_projets` : Contient la liste des projets qui permettront de gagner des points bonus dans les ligues suivantes (donc pas utile au début)
- `mon_robot` et `son_robot` : Contiennent les informations suivantes pour chaque joueur : 'position','temps_arrivee','score','molecules','expertise' que l'on peut récupérer en écrivant par exemple `mon_robot.score` si l'on souhaite récupérer la valeur de notre score ou `mon_robot.molecules` si l'on souhaite avoir la liste du nombre de molécules de chaque sorte que l'on possède.
- `mes_fichiers`, `ses_fichiers`,`fichiers_stockés` : L'ensemble des fichiers est réparti dans ces listes.

Pour rappel, ces trois dernières listes contiennent des objets de type Fichier. Pour récupérer une donnée particulière d'un Fichier, par exemple pour la vie, on utilisera la notation `fichier.vie` comme présentée plus haut.  
Par exemple si on veut voir s'afficher (avec la fonction log) l'ID de mes fichier suivie de son coût pour chaque molecule et de la vie qu'il va rapporter on pourrait écrire :
```python
for fichier in mes_fichiers:
    log(fichier.id, fichier.couts, fichier.vie)
```
On verrait alors s'afficher dans la partie "Sortie d'erreur" en rouge trois lignes de la forme "0 [1,2,0,0,1] 10" par exemple.

## Quelques conseils

- Commencez par des stratégies simple au  début. Le but est d'arriver en Bronze avec le moins d'efforts possibles car des règles vont se rajouter jusque là donc inutile de créer un code parfait qu'il faudra de toute façon changer.
- Essayez de comprendre la structure du code proposé en kit et de la respecter pour que votre code reste lisible et compréhensible sur le long terme. Par exemple, il vaut mieux prendre le temps d'écrire des fonctions à part plutôt que d'écrire directement tout dans la logique du jeu. Une idée aussi bonne soit-elle sera surement remplacée un peu plus tard par une autre et donc si votre code est trop brouillon, il deviendra vite inutilisable. Par exemple une fonction `choix_molecule` car comme le nombre de molécule est très limité, selon la stratégie choisie, ce choix va changer. On pourra ainsi facilement tester différentes stratégies en créant différentes fonctions tout en changeant au minimum notre code dans la partie logique du jeu tout en gardant un code lisible.

Amusez vous bien !

@[Inutile d'appuyer sur Run]({"stubs":["Projets/Code4life.py"], "command": "python3 Projets/Code_a_la_mode_Test.py", "layout": "aside"})
