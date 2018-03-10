#Ne pas oublier de changer le module à importer
from Juste_prix import mon_programme
from random import randint
import sys
import io

#Mon IA
prix_minIA=0
prix_maxIA=2000
mon_prixIA=1000

def mon_programmeIA(paroles):
    global prix_minIA, prix_maxIA, mon_prixIA
    if paroles=="Go": return mon_prixIA
    elif paroles=="Plus grand":
        prix_minIA=mon_prixIA
        mon_prixIA=(prix_minIA+prix_maxIA)//2
        return mon_prixIA
    else:
        prix_maxIA=mon_prixIA
        mon_prixIA=(prix_minIA+prix_maxIA)//2
        return mon_prixIA



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
    succes=0
    nombre_a_trouver=randint(1,2000)
    n_joueur=mon_programme("Go")
    n_IA=mon_programmeIA("Go")
    compteur=0
    while 1:
        compteur+=1
        if compteur==8: send_msg("Le juste prix !", "Olala quel suspens !")
        send_msg("Le juste prix !", "Le présentateur se tourne vers vous")
        send_msg("Le juste prix !", "Vous proposez "+str(n_joueur))
        if n_joueur==nombre_a_trouver:
            succes=1
            break
        elif n_joueur>nombre_a_trouver:
            send_msg("Le juste prix !", "Le présentateur vous dit plus petit !")
            n_joueur=mon_programme("Plus petit")
        else:
            send_msg("Le juste prix !", "Le présentateur vous dit plus grand !")
            n_joueur=mon_programme("Plus grand")
        send_msg("Le juste prix !", "Le présentateur se tourne à présent vers votre adversaire !")
        send_msg("Le juste prix !", "Votre adversaire propose "+str(n_IA))
        if n_IA==nombre_a_trouver:
            send_msg("Le juste prix !", "Que c'est dommage ! votre adversaire vient de trouver le juste prix de "+str(nombre_a_trouver))
            fail()
            break
        elif n_IA>nombre_a_trouver:
            send_msg("Le juste prix !", "Le présentateur lui dit plus petit !")
            n_IA=mon_programmeIA("Plus petit")
        else:
            send_msg("Le juste prix !", "Le présentateur lui dit plus grand !")
            n_IA=mon_programmeIA("Plus grand")
    #On relance 10 tests au cas où c'etait de la chance la premiere fois
    while succes<11:
        nombre_a_trouver=randint(1,2000)
        n_joueur=mon_programme("Go")
        n_IA=mon_programmeIA("Go")
        while 1:
            if n_joueur==nombre_a_trouver:
                succes+=1
                break
            elif n_joueur>nombre_a_trouver:
                n_joueur=mon_programme("Plus petit")
            else:
                n_joueur=mon_programme("Plus grand")
            if n_IA==nombre_a_trouver:
                send_msg("Le juste prix !", "Vous avez gagné la première fois mais vous n'avez pas gagné les 10 parties jouées en aveugle pour éviter que vous ne gagniez par chance !")
                fail()
                break
            elif n_IA>nombre_a_trouver:
                n_IA=mon_programmeIA("Plus petit")
            else:
                n_IA=mon_programmeIA("Plus grand")  
    if succes>=11: success()
if __name__ == "__main__": test()
