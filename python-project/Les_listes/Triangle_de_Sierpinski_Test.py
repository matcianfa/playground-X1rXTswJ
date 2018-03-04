#Ne pas oublier de changer le module à importer
from Triangle_de_Sierpinski import mon_programme,dimension
import sys
import io
from PIL import Image, ImageDraw



# Image size (pixels)
WIDTH = dimension
HEIGHT = dimension
palette = []

im = Image.new('RGB', (WIDTH, HEIGHT), (255, 255, 255))
draw = ImageDraw.Draw(im)

#message d'aide si besoin
help=""



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    #send_msg("Tests validés","Bravo !")
    print("TECHIO> open -s /project/target/ index.html")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

        
        
        


def test():
    try:
      for n in range(1,dimension+1):
          sauvegarde_stdout=sys.stdout
          sys.stdout=io.StringIO()
          mon_programme(n)
          liste = list(sys.stdout.getvalue()[:-1])
          sys.stdout=sauvegarde_stdout
          for j,element in enumerate(liste):
            if element%2!=0: 
                draw.point([j, n-1], (0,0,0))
      im.save('output.png', 'PNG')
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
