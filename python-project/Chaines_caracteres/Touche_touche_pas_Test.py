#Ne pas oublier de changer le module à importer
module="Chaines_caracteres/Touche_touche_pas"

import sys
import io
from ma_bao import *
tester("from Touche_touche_pas import mon_programme",globals())




#liste des couples input/output
input_output=[\
("MAISON","TOUCHE"),\
("PORTE","TOUCHE"),\
("LIT","TOUCHE PAS"),\
("CHAISE","TOUCHE PAS"),\
("BEBE","TOUCHE"),\
("ROND","TOUCHE PAS"),\
("MAMAN","TOUCHE"),\
("HOPITAL","TOUCHE"),\
("PHARE","TOUCHE PAS"),\
("COMPTE","TOUCHE PAS"),\
("SIROP","TOUCHE PAS"),\
("POMPE","TOUCHE"),\
("CHAMP","TOUCHE PAS"),\
("CHAMPIGNON","TOUCHE"),\
("CHAMPS","TOUCHE PAS"),\
("AMPOULE","TOUCHE"),\
("AMPHORE","TOUCHE PAS"),\
("PHENOMENE","TOUCHE"),\
("SYMPTOME","TOUCHE"),\
("SOMPTUEUX","TOUCHE")\
]


#message d'aide si besoin
help="Il n'y a que 3 lettres qui font toucher mais il y a des pièges... beaucoup de pièges..."



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    afficher_correction(module)
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for inp,outp in input_output:
        sauvegarde_stdout=sys.stdout
        sys.stdout=io.StringIO()
        mon_programme(inp)
        count1 = sys.stdout.getvalue()[:-1]
        sys.stdout=sauvegarde_stdout
        assert str(count1) == str(outp), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
