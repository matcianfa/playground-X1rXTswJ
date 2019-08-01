from PIL import Image, ImageDraw  # Module de gestion des images
import numpy as np
from Julia import Julia, MU

# --------- Les constantes, modifiables
WIDTH,HEIGHT = 900,600
X_MIN,Y_MIN,X_MAX = -1,-1.1,2 # Valeurs min et max pour les parties reelles et imaginaires
Y_MAX=Y_MIN+HEIGHT*(X_MAX-X_MIN)/WIDTH #Pour avoir un repère normé


def creer_image(mu=MU):
    im = Image.new('HSV', (WIDTH, HEIGHT), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    X = np.linspace(X_MIN, X_MAX, WIDTH)
    Y = np.linspace(Y_MAX, Y_MIN, HEIGHT)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            n=Julia(mu,complex(X[x],Y[y]))
            draw.point((x, y), (n%255, 255, 255 if n < 200 else 0))
    im.convert('RGB').save('output.png', 'PNG')
