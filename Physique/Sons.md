# Le son en python

Le but de cette page est de présenter succintement ce qu'est un son (réel ainsi qu'au sens informatique) au format Wav et comment le traiter avec python.

## Ouvrir un son, le voir et l'entendre.

Nous allons commencer par observer un son (ici ce sera un LA joué au piano) enregistré au format WAVE. C'est un format brut dans lequel les données enregistrées sont simplement stockées (il n'y a aucun traitement). Il n'y a ainsi aucune perte a priori mais l'inconvénient est que cela prend beaucoup de place en mémoire.  
Remarque : Pour des raisons pratiques, l'affichage et le fait de jouer le son sont gérés par une fonction `afficher_jouer_son` car sur ce site l'accès à l'affichage et aux haut parleurs demande quelques pirouettes. Cela serait beaucoup plus simple à faire en direct sur son propre ordinateur. Pour les curieux vous pouvez voir les détails de la fonction en changeant d'onglet.
@[Ouvrir un son]({"stubs": ["Physique/afficher_jouer_son.py","Physique/fonction_afficher_jouer_son"], "command": "python3 Physique/afficher_jouer_son_Test.py"})

On peut observer sur le graphique 2 courbes de couleurs différentes car c'est un son stéréo.
