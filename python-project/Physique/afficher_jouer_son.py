import numpy as np
from matplotlib import pyplot as plt
import soundfile as sf
from fonction_afficher_jouer_son import afficher_jouer_son # Fonction perso pour afficher et jouer le son sur ce site

# Je charge mon fichier ce qui me donne des données (sous forme de vecteur numpy ) et la fréquence d'enregistrement
données_son,frequence = sf.read("pianoA.wav")

# J'affiche mon son et je le joue en même temps
afficher_jouer_son(données_son,frequence)

# Je regarde un peu les caractéristiques de mon son :
print("Taille de l'echantillon : ", données_son.shape) # Double si stéréo
print("Fréquence : {} Hz".format(frequence))
print("Données du son : ",données_son)
