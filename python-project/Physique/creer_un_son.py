from math import cos,sin,pi
from fonction_afficher_jouer_son import afficher_jouer_son # Fonction perso pour afficher et jouer le son sur ce site

# ------- Constantes
frequence_echantillon = 44100 # Hz
duree = 2 # secondes

# ------- Fonction correspondant au son

def ma_fonction(x) :
    return cos(2*pi*440*x)

# ------- création des données du son
données_son = [ma_fonction(k/frequence_echantillon) for k in range(int(duree*frequence_echantillon))]

# J'affiche mon son et je le joue en même temps
afficher_jouer_son(données_son,frequence_echantillon)

