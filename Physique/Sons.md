# Le son en python

Le but de cette page est de présenter succintement ce qu'est un son (réel ainsi qu'au sens informatique) au format Wav et comment le traiter avec python.

## Ouvrir un son, le voir et l'entendre

Nous allons commencer par observer un son (ici ce sera un LA joué au piano) enregistré au format WAVE. C'est un format brut dans lequel les données enregistrées sont simplement stockées (il n'y a aucun traitement). Il n'y a ainsi aucune perte a priori mais l'inconvénient est que cela prend beaucoup de place en mémoire.  
Remarque : Pour des raisons pratiques, l'affichage et le fait de jouer le son sont gérés par une fonction `afficher_jouer_son` car sur ce site l'accès à l'affichage et aux haut parleurs demande quelques pirouettes. Cela serait beaucoup plus simple à faire en direct sur son propre ordinateur. Pour les curieux vous pouvez voir les détails de la fonction en changeant d'onglet.
@[Ouvrir un son]({"stubs": ["Physique/afficher_jouer_son.py","Physique/fonction_afficher_jouer_son.py"], "command": "python3 Physique/afficher_jouer_son_Test.py"})

On peut observer sur le graphique 2 courbes de couleurs différentes car c'est un son stéréo. Cela se retrouve dans la taille des données : c'est un tableau de dimension 67936 x 2.  
Un son c'est donc une liste de données qui correspondent à la "valeur" du son à un instant précis. Si la frequence est de 44100 Hz cela signifie que 44100 données représente une seconde du son. Autrement dit, pour lire un son, on lit une donnée et toutes les 1/44100 secondes on passe à la donnée suivante.

## Créer son propre son

Pour créer un son c'est extrêmement simple : Si la frequence est de 44100 Hz, il suffit de créer une liste de valeur correspondant à ce qui sera joué toutes les 1/44100 secondes.  
Par exemple, si on veut jouer un son pur comme un LA de diapason (qui a une frequence de 440 Hz), il suffit de créer une liste de points correspondant à une fonction cosinus qui a une fréquence de 440 Hz (ce qui correspond à la fonction $`cos(2\pi*440x)`$). Voici le résultats ci-dessous.

@[Créer un son]({"stubs": ["Physique/creer_un_son.py","Physique/fonction_afficher_jouer_son.py"], "command": "python3 Physique/creer_un_son_Test.py"})

Quelques remarques : 
- Si on veut voir un peu mieux la fonction il faut réduire la durée à par exemple 0.01 car en 1 sec, elle oscille 440 fois donc naturellement sur le graphique, on ne voit pas les oscillations.
- S'il n'y a pas de modification à l'execution alors que vous avez modifié le code, n'hésitez pas à relancer en appuyant sur RUN
- On peut s'amuser à modifier la fréquence du son en modifiant le 440 Hz. Attention à ne pas confondre les fréquences : La fréquence d'echantillonage nous donne une information sur le nombre de données utilisées pour créer le son (plus il y a de données, plus notre son est précis). La fréquence de la note elle par contre est simplement physique, c'est la fréquence de vibration pour obtenir cette note (avec une corde par exemple).

On peut facilement créer d'autres sons plus interessants. 
