from PIL import Image, ImageDraw
import numpy as np

# On charge l'image et on la transforme en tableau contenant les couleurs
image_entrée = Image.open("Info/Lenna.png")
image = np.asarray(image_entrée)

# On crée notre image de sortie sous forme de tableau numpy
image_sortie = ...

# On sauvegarde les images pour pouvoir les afficher
Image.fromarray(image).save("image_entree.png")
Image.fromarray(image_sortie).save("image_sortie.png")
