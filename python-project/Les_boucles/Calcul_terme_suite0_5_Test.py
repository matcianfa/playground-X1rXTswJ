#Ne pas oublier de changer le module à importer
module="Les_boucles/Calcul_terme_suite0_5"

import sys
import io
from ma_bao import *
tester("from Calcul_terme_suite0_5 import mon_programme",globals())

#liste des couples input/output
input_output=[\
((1,5),-17),\
((5,1),-409),\
((10,0),-629145),\
((0,10),10),\
((0,0),0),\
((1000,10),1079242853557799252778863209107021064980978639963373488448984172616220285708828095025259917137515893723339206760648215007040291823211272011540375474796653994267821897965935432006474523993456421791431913706596770700947185358276050621104780044780383727326506967646726548804079518292859129505639943686521127204635187744453909952662367157194392153668786899104032625537042282806906876443021044142555918103181742030556726330394004730668997996302619922564484360678679664053216603165742917168104770397836327477900576000487024545966478592342661312383803592368496676649093970727734722045688875265364537600800876135)\
]


#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat"

#Afficher la correction
def afficher_correction():
    try:
        with open(module+"_Correction.py", "r") as correction :
            ligne="Voici un ou des exemples de corrections possibles"
            send_msg("Exemple(s) de correction", ligne)
            ligne="-------------------------------------------------"
            send_msg("Exemple(s) de correction", ligne)
            lignes=correction.read().split("\n")
            for ligne in lignes:
                send_msg("Exemple(s) de correction", ligne)
    except:
        pass



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
        mon_programme(*inp)
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
