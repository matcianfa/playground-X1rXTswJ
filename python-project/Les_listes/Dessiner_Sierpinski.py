from PIL import Image, ImageDraw
from Triangle_de_Sierpinski import dimension

# Image size (pixels)
WIDTH = dimension
HEIGHT = dimension
palette = []

im = Image.new('RGB', (WIDTH, HEIGHT), (255, 255, 255))
draw = ImageDraw.Draw(im)

def dessiner(liste):
  i=len(liste)-1
  for j,element in enumerate(liste):
    if element%2!=0: 
      draw.point([x, y], (0,0,0))
      
im.save('output.png', 'PNG')
