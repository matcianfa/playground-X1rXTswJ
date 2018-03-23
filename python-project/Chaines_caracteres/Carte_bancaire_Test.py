#Ne pas oublier de changer le module à importer
module="Les_boucles/Carte_bancaire"

import sys
import io
from ma_bao import *
tester("from Carte_bancaire import mon_programme",globals())




#liste des couples input/output
input_output=[\
("1234567891234565","NON VALIDE"),\
("4970101234567899","NON VALIDE"),\
("1234567891234563","VALIDE"),\
("4970101234567893","VALIDE"),\
("1001001001001002","VALIDE"),\
("1234567898","NON VALIDE"),\
("101010101010101012","NON VALIDE"),\
]


#message d'aide si besoin
help="Attention, il faut qu'il y ait 16 chiffres !"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    afficher_correction()
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
