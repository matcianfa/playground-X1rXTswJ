# Sommes de chemins : 2 directions
`Difficulté : Moyen (10%)`
`Origine : Projet Euler n°81`

Dans la matrice 5 par 5 ci-dessous, le chemin de somme minimale du coin en haut à gauche au coin en bas à droite, en ne se déplaçant que vers la droite ou le bas est indiqué en rouge et est égal à 2427.

$`\begin{pmatrix}
\color{red}{131} & 673 & 234 & 103 & 18\\
\color{red}{201} & \color{red}{96} & \color{red}{342} & 965 & 150\\
630 & 803 & \color{red}{746} & \color{red}{422} & 111\\
537 & 699 & 497 & \color{red}{121} & 956\\
805 & 732 & 524 & \color{red}{37} & \color{red}{331}
\end{pmatrix}`$

Trouver le chemin de somme minimale dans la matrice 80 par 80 donnée ci dessous du coin en haut à gauche au coin en bas à droite, en ne se déplaçant que vers la droite ou le bas.

On affichera le résultat avec `print`.

@[Sommes de chemins : 2 directions]({"stubs": ["Defis/Euler_81.py"], "command": "python3 Defis/Euler_81_Test.py"})

---

# Sommes de chemins : 3 directions
`Difficulté : Moyen (20%)`
`Origine : Projet Euler n°82`

Dans la matrice 5 par 5 ci-dessous, le chemin de somme minimale de la colonne de gauche à la colonne de droite, en ne se déplaçant que vers la droite, le haut ou le bas est indiqué en rouge et est égal à 994.

$`\begin{pmatrix}
131 & 673 & \color{red}{234} & \color{red}{103} & \color{red}{18}\\
\color{red}{201} & \color{red}{96} & \color{red}{342} & 965 & 150\\
630 & 803 & 746 & 422 & 111\\
537 & 699 & 497 & 121 & 956\\
805 & 732 & 524 & 37 & 331
\end{pmatrix}`$

Trouver le chemin de somme minimale dans la matrice 80 par 80 donnée ci dessous de la colonne de gauche à la colonne de droite, en ne se déplaçant que vers la droite, le haut ou le bas.

On affichera le résultat avec `print`.

@[Sommes de chemins : 3 directions]({"stubs": ["Defis/Euler_82.py"], "command": "python3 Defis/Euler_82_Test.py"})

---

# Sommes de chemins : 4 directions
`Difficulté : Moyen (25%)`
`Origine : Projet Euler n°83`

Dans la matrice 5 par 5 ci-dessous, le chemin de somme minimale du coin en haut à gauche au coin en bas à droite, en se déplaçant vers la droite, la gauche, le haut ou le bas est indiqué en rouge et est égal à 2297.

$`\begin{pmatrix}
\color{red}{131} & 673 & \color{red}{234} & \color{red}{103} & \color{red}{18}\\
\color{red}{201} & \color{red}{96} & \color{red}{342} & 965 & \color{red}{150}\\
630 & 803 & 746 & \color{red}{422} & \color{red}{111}\\
537 & 699 & 497 & \color{red}{121} & 956\\
805 & 732 & 524 & \color{red}{37} & \color{red}{331}
\end{pmatrix}`$

Trouver le chemin de somme minimale dans la matrice 80 par 80 donnée ci dessous du coin en haut à gauche au coin en bas à droite, en se déplaçant vers la droite, la gauche, le haut ou le bas.

On affichera le résultat avec `print`.

@[Sommes de chemins : 4 directions]({"stubs": ["Defis/Euler_83.py"], "command": "python3 Defis/Euler_83_Test.py"})

---

# Chances au monopoly
`Difficulté : Moyen (35%)`
`Origine : Projet Euler n°84`

Dans le jeu de Monopoly, le plateau standard ressemble à ceci (C'est une version anglaise) :

![plateau](https://drive.google.com/open?id=1rxERHneYM1weOBQYIjRd0xZxLMOE6iXv)

Un joueur commence sur la case GO et ajoute le score fait avec 2 dés à 6 faces pour déterminer de combien de case il avance dans le sens des aiguilles d'une montre. Sans aucune autre règle, on peut s'attendre à visiter toutes les cases avec la même probabilité : 2.5%. Cependant, comber sur la case G2J (Aller en prison), CC (carte communauté) et CH (carte chance) change cette distribution.

De plus, en plus de la case G2J et des cartes CC ou CH qui envoient en prison, si le joueur obtient 3 doubles d'affilée, il est envoyé en prison au lieu d'avancer.

Il y a 16 cartes Chance et Communauté. Pour ce qui nous intéresse, c'est à dire le mouvement, certaines cartes n'auront aucune influence et le joueur restera donc sur la case CC ou CH.

    Community Chest (2/16 cards):  
        Advance to GO  
        Go to JAIL  
    Chance (10/16 cards):  
        Advance to GO  
        Go to JAIL  
        Go to C1  
        Go to E3  
        Go to H2  
        Go to R1  
        Go to next R (railway company)  
        Go to next R  
        Go to next U (utility company)  
        Go back 3 squares.  
        
Le coeur de ce problème est de trouver la probabilité de finir sur un case. Plus précisément : pour la case G2J, il est clair que la probabilité de finir sur cette case est nulle puisqu'elle nous envoie en prison. De même, la case CH a une probabilité beaucoup plus faible que les autres car 10 cartes sur 16 nous envoie sur une autre case et c'est la case sur laquelle le joueur fini son tour qui compte. On ne fera pas de distinction entre Aller en prison et visiter la prison car on supposera que la personne paie pour sortir systematiquement.

En commençant sur la case GO et en numérotant les cases de 00 à 39, on peut concaténer les 2 chiffres du nombre pour produire une chaine qui correspon aux cases.
On peut montrer que les 3 cases les plus populaires sont  JAIL (6.24%) (case 10), E3 (3.18%) (Case 24) et GO (3.09%) = (Case 00). Donc ces trois cases les plus populaires peuvent être listée sous forme d'une chaine de caractère de 6 chiffres : 102400.

Si, au lieu d'utiliser deux dés de 6 faces, on utilise deux dés de 4 faces, trouver la chaine de caractère de 6 chiffres correspondant aux 3 cases les plus populaires.

On affichera le résultat avec `print`.

@[Chances au monopoly]({"stubs": ["Defis/Euler_84.py"], "command": "python3 Defis/Euler_84_Test.py"})

---
