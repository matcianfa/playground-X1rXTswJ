#Ne pas oublier de changer le module à importer
from Gardner import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
(1,2),\
(2,4),\
(3,11),\
(5,83),\
(7,616),\
(10,12367),\
(15,1835421)\
]


#message d'aide si besoin
help=""



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
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
      send_msg("Tests validés","Les tests s'arretent à 15 car à 20 seulement Python est déja trop lent pour calculer. Le résultat serait 272400600. Alors imaginez si on cherche pour 100...")
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
