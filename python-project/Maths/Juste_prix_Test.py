#Ne pas oublier de changer le module à importer
from Juste_prix import mon_programme
from random import randint
import sys
import io




#message d'aide si besoin
help="N'oublie pas d'utiliser return pour afficher le resultat qui doit être un entier"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Le juste prix !","Bravo ! C'était bien le juste prix !")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    nombre_a_trouver=randint(1,2000)
    n_joueur=mon_programme("Go")
    while 1:
        send_msg("Le juste prix !", "Vous proposez "+str(n_joueur))
        if n_joueur==nombre_a_trouver:
            success()
            break
        elif n_joueur>nombre_a_trouver:
            n_joueur=mon_programme("Plus petit")
        else:
            n_joueur=mon_programme("Plus grand")


if __name__ == "__main__": test()
