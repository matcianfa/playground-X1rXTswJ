# Combat d'IA : Spider attack

Remarque pratique : N'hésitez pas à mettre en mode plein ecran (bouton au dessus du code à droite) et réduire le zoom pour mieux voir.

[Voici le lien pour accéder directement au jeu](https://www.codingame.com/multiplayer/bot-programming/spring-challenge-2022)

## Présentation

Ce combat d'IA va demander un peu plus de connaissance en programmation qu'un challenge comme Code à la mode. Mais une fois passées les premières difficultés (comme par exemple compréhension du kit de démarrage ou comment programmer la recherche d'un plus petit élément dans une liste), c'est surtout la recherche d'une bonne stratégie qui va prévaloir sur le niveau en programmation.
Un objectif raisonnable peut être de viser un bon classement dans la ligue Bronze voire, pour les meilleurs, passer en ligue Argent.

Jusqu'à la ligue Bronze, il va falloir s'adapter aux différents ajouts qui apparaitront à chaque changement de ligue. Donc le but pour arriver à la ligue Bronze est simplement de faire un code propre pour répondre aux attentes. Pour progresser ensuite, il faudra chercher à optimiser un peu plus.

## Kit de démarrage

Vous pouvez trouver sur votre droite un kit de démarrage pour ce combat d'IA. Il suffit de le copier coller à la place du code de base sur le site Codingame. Ce kit est largement inspiré par celui fourni pour ce challenge, la principale différence est qu'il est traduit. Bien sûr ce kit de démarrage n'est ni un obligation ni la perfection. On peut très bien s'en passer et même si on l'utilise, il faudra de toute façon s'en éloigner pour réussir à monter haut dans le classement. Il n'a pas d'autre but que d'aider à démarrer ceux qui en auraient besoin.

Donnons quelques explications sur le code.

### Les fonctions auxiliaires

La fonction log ne sert à rien pour le jeu mais c'est de loin la plus utile de toutes car elle permet de chercher ses erreurs. En effet, elle permet d'afficher des variables comme un message d'erreur (donc en rouge) sans que cela soit pris comme une réponse et sans arrêter le jeu (comme si on affichait un commentaire).

Si vous avez besoin de créer des fonctions, je vous conseille de les rajouter dans cette partie du code car on se perd très vite dans un code mais structuré.

### Les constantes et variables

Une bonne habitude à prendre : Traduire les données de l'énoncé en constantes faciles à retenir. Par exemple ici, il y a plusieurs types d'agents qui vont intervenir : vos heros, les heros adverses et les araignées. Pour les différencier, il y aura une variable `type` qui de base vaut 0, 1 ou 2. On peut choisir de conserver dans notre code ces valeurs (ce qui donnerait par exemple `if _type == 0:` dans notre code) ou bien, comme proposé dans le kit, de nommer ces différents types pour que, quand on lit `if _type == TYPE_MONSTRE:` on comprenne de suite qu'on est en train de vérifier si notre agent est un monstre. 

Ensuite vient la création de ce que l'on va appeler un Agent qui sera le terme générique pour un élément du jeu (héros ou araignées). En effet ils ont beaucoup d'éléments en commun donc autant les considérer de manière identique pour stocker leurs informations et on les triera simplement dans  des listes différentes dans lesquels on mettra les heros de chaque joueur et les araignées séparément. 

Nous avons essayé ici de réduire au minimum la programmation orientée objet sans pour autant l'éviter car elle rend ici le code beaucoup plus simple d'utilisation. En effet un agent (donc un heros ou une araignée) a plusieurs caractéristiques qui sont détaillées dans la présentation du jeu (à traduction près) : 'id', 'type', 'x', 'y', 'duree_bouclier', 'sous_controle', 'vie', 'vx', 'vy', 'proche_base', 'menace_pour'.  
Pour récupérer les données d'un agent nommé `a`, il suffira d'écrire `a.x` pour connaitre son abscisse par exemple ou `a.vie` pour connaitre sa vie ou encore `a.menace_pour` pour savoir quelle base est menacée par cet agent.
