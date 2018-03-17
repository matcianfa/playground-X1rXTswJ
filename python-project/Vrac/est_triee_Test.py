#Ne pas oublier de changer le module à importer
from est_triee import est_triée as mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
([1,2,3,4,5],True),\
([5,4,3,2,1],False),\
([1,1,2,3,3,4],True),\
([14,12,23,31,3,42],False),\
([1,1,1,2,1,3,4],False)\
]


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
      for inp,outp in input_output:
        count1 = mon_programme(inp)
        assert count1 == outp, "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
