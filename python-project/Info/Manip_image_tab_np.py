from PIL import Image, ImageDraw
import numpy as np

# On charge l'image et on la transforme en tableau contenant les couleurs
image_entrée = Image.open("Info/exemple.png")
image = np.asarray(image_entrée)

# On affiche le tableau numpy de représentant l'image
print(image)

# On sauvegarde l'image pour pouvoir les afficher
Image.fromarray(image).save("output.png")
