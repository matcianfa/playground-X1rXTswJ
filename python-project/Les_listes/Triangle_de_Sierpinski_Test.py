#Ne pas oublier de changer le module à importer
from Triangle_de_Sierpinski import mon_programme,dimension
import sys
import io
import pixel


#liste des couples input/output
zoom=4


#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      pixel.initialiser(dimension//zoom,dimension//zoom,zoom)
      mon_programme(input_output)
      pixel.afficher()
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
