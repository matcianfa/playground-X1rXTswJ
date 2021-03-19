import numpy as np
from matplotlib import pyplot as plt
import soundfile as sf
from fonctions_Fourier import * # Les fonctions qui permettent de calculer les coefficients de Fourier etc. (voir onglet)

# Je charge mon fichier ce qui me donne des données (sous forme de vecteur numpy ) et la fréquence d'enregistrement
données_son,frequence_echantillon = sf.read("pianoA.wav")
# On passe en mono (car le son est stéréo), 
# On réduit aussi un peu la longueur de notre son et on ne garde qu'un coefficient sur 4 car on ne peut calculer que 30 sec sur ce site
données_son = données_son[:50000:3,0]
taille_echantillon = données_son.shape[0]
frequence_echantillon //= 3

# On récupère les coefficients de Fouriers
a,b = coeff_Fourier(données_son)

# On cherche pour quelle valeur de k on va dépasser les fréquences audibles pour ne pas faire de calculs inutiles
frequence_max = 4000 # Hz
k_max = int(frequence_max*taille_echantillon/frequence_echantillon)

# On calcule les coefficients des harmoniques audibles
coeff_harmoniques = donner_coefficients_harmoniques(a[:k_max],b[:k_max])

# On affiche les harmoniques
plt.plot(np.arange(0,k_max)*frequence_echantillon/taille_echantillon,coeff_harmoniques)
plt.show()

# On retire les coefficients en dessous du seuil car il ne compte pas vraiment dans le son
seuil = 2
a_coupé = np.where(a<seuil,0,a)
b_coupé = np.where(b<seuil,0,b)
son_épuré = inv_Fourier(a_coupé,b_coupé,k_max)

# On enregistre notre son où on a retiré tous ces coefficients pour voir ce que cela donne
sf.write("Physique/son_epure.wav",son_épuré,frequence_echantillon)

# Pour info : on regarde combien de coefficients il reste 
print("Il reste {} coefficients non nuls au lieu de {} au départ".format(np.count_nonzero(a_coupé)+np.count_nonzero(b_coupé),taille_echantillon))
