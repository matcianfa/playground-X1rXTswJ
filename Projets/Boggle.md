# Exemple d'IA sur le jeu Boggle

Voici un exemple complet utilisant les modules présentés dans le projet IA et jeux sur mobiles de la page précédente.

## Présentation du jeu

Le jeu consiste en une grille 4x4 de lettres. Le but est de former le plus de mots possibles  en parcourant la grille de proche en proche en se déplaçant dans les 8 directions possibles. On peut trouver ce jeu sur mobile ou facebook sous plusieurs formes (Boggle entre amis, Word Blitz).

Voici un lien vers une vidéo montrant l'algorithme en action : [Vidéo](https://youtu.be/QmHLsj6jn7s)  
On pourra remarquer que la reconnaissance des 16 caractères prend dans les 15 secondes ce qui est relativement lent et il arrive souvent qu'elle inverse les P et les D ou les I et les l. Donc il y a des améliorations à faire de ce coté là.

On pourra trouver les fichiers directement ici : [GitHub](https://github.com/matcianfa/archives/tree/master/Word%20Blitz)

Remarque pour pouvoir l'utiliser : il faudra recompiler les dictionnaires car ils étaient trop lourds (50 Mo). Pour cela il suffit de lancer Generer_automate.py une fois (ce qui créera un fichier en binaire nommé automate qui fait environ 56 Mo).  
Une fois que c'est fait il faut lancer le script main.py pour charger en mémoire toutes les fonctions puis pour lancer l'IA lorsque le jeu Boogle démarre, il faut taper lancer(80) pour que l'IA fasse le maximum de mots pendant 80 secondes.




