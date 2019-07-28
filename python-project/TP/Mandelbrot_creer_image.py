from PIL import Image, ImageDraw  # Module de gestion des images

# --------- Les constantes, modifiables
WIDTH,HEIGHT = 900,600
X_MIN,Y_MIN,X_MAX = -2,-2,4 # Valeurs min et max pour les parties reelles et imaginaires
Y_MAX=Y_MIN+HEIGHT*(X_MAX-X_MIN)/WIDTH #Pour avoir un repère normé

# La fonction pour créer l'image de la courbe de Mandelbrot
def creer_image():
    # Crée une image vierge
    im = Image.new('HSV', (WIDTH, HEIGHT), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    
    # Créer autant de X et Y que de pixels dans l'image
    X = np.linspace(X_MIN, X_MAX, WIDTH)
    Y = np.linspace(Y_MIN, Y_MAX, HEIGHT)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            n = Mandelbrot(complex(X[x],Y[y]))
            # Colorie le point de coordonnée (x,y) avec une couleur indiquée en HSV (ce qui permet de n'avoir à modifier que le premier coefficient (et le dernier pour obtenir le noir))
            draw.point((x, y), (n%255, 255, 255 if n < 200 else 0))
            
    # Converti l'image en RGB pour ensuite la sauvegarder en .png
    im.convert('RGB').save('output.png', 'PNG')
