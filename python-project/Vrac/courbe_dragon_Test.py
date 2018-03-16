#Ne pas oublier de changer le module à importer
from courbe_dragon import pliage
import sys
import io
from random import randint

#reponse
def pliage2(k):
    while k%2==0:
        k//=2
    if k%4==1:
        return "G"
    else :
        return "D"

#message d'aide si besoin
help="N'oublie pas d'utiliser return pour afficher le resultat"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for _ in range(15):
        k=randint(2,1000)
        count1=pliage(k)
        outp=pliage2(k)
        assert str(count1) == str(outp), "En testant l valeur k={} le résultat obtenu est {} au lieu de {}".format(str(k),str(count1),str(outp))
        send_msg("Tests validés","En testant la valeur k={} le résultat obtenu est bien {}".format(str(k),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
