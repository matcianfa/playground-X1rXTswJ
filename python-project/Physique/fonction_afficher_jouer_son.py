import soundfile as sf
from matplotlib import pyplot as plt
import numpy as np

def afficher_jouer_son(son,frequence,fichier = "Physique/son.wav"):
  # On l'affiche
  son = np.asarray(son)
  taille = son.shape[0]
  temps = np.arange(0,taille)/frequence
  plt.plot(temps,son)
  plt.show()
  # On l'enregistre pour qu'il se joue automatiquement dans la page html 
  # (pirouette due au fait de passer par ce site)
  # Sur son pc il suffirait de faire 

  #import sounddevice as sd
  #sd.play(son,frequence)
  
  sf.write(fichier,son,frequence)
