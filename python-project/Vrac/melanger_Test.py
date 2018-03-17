#Ne pas oublier de changer le module à importer
from melanger import mélanger as mon_programme
import sys
import io
from random import randint

#liste des couples input/output
input_output=[\
[1,2,3,4,5],\
[1,2,3,1,2,3],\
[randint(0,1000) for _ in range(200)]\
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
      for inp in input_output:
        count1 =mon_programme(inp)
        assert sorted(count1) == sorted(inp), "En testant la liste {} le résultat obtenu est {} ce qui n'est pas un mélange.".format(str(inp),str(count1))
        send_msg("Tests validés","En testant les valeurs {}, un mélange est bien {}".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
