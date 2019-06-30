# Projet : IA de jeux

## Présentation

Le but de cette page est de présenter un squelette de projet réalisable avec les élèves et les outils qui peuvent être utile pour le réaliser.

L'idée est de proposer aux élèves de programmer une IA permettant de jouer à des jeux existants déjà sur ordinateur ou même telephone ou tablette.  
Pour que l'élève ait juste à programmer l'IA du jeu, il va falloir lui fournir toutes les données utiles et pour cela, nous allons voir quelques modules pythons intéressants.

Le plan d'attaque est à peu près celui la :
- récupération des données graphiques et traduction en données utilisables (mots, scores etc.)
- IA (la partie que l'élève aura à gérer)
- sorties clavier et souris

Après, libre à vous pour les élèves les plus avancés de les laisser faire plus que l'IA ou de laisser différents groupes gérer sa partie.

D'un point de vue pratique, il est indispensable de donner aux élèves ce qu'ils auront comme entrées (par exemple une matrice de lettre) et ce qu'ils doivent donner en sortie de manière très précise (par exemple une liste de commandes avec un format précis).
En effet, pour bien structurer le projet, chacune des trois parties étant indépendantes, elles devront être écrites dans des fichiers distincts et le programme sera lancé dans un quatrième qui importera les 3 autres et les mettra en relation.

## Le jeu

Tout d'abord quelques mots sur le jeu. L'idée est d'utiliser un jeu déjà existant et non pas de le reprogrammer. La motivation venant du fait qu'il pourra ensuite comparer son IA à d'autres joueurs. Pour cela, plusieurs possibilités : 
- Si le jeu existe en version ordinateur (jeux facebook par exemple), alors aucun soucis, il suffira de le lancer
- Si le jeu est un jeu mobile, on pourra utiliser un emulateur qui vous permettra d'émuler un mobile sur votre ordinateur. Par exemple pour Android, on pourra par exemple utiliser [Memu Play](https://www.memuplay.com/fr/). 

L'avantage des jeux mobiles ou facebook c'est qu'ils sont en général assez simples à utiliser (la souris suffit) et les utilisateurs s'imaginent peu qu'on puisse faire jouer un programme à notre place.




