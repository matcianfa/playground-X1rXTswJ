#Ne pas oublier de changer le module à importer
from Monty_Hall import mon_programme
import sys
import io
from random import randint

nb_tests=100000

#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      compteur=0
      #On fait quelques parties qu'on affiche
      for i in range(1,11):
        send_msg("Jeu de Monty Hall", "Partie n°{}".format(str(i)))
        porte_gagnante=randint(1,3)
        res=mon_programme(0)
        send_msg("Jeu de Monty Hall", "Pour cette première phase du jeu, vous proposez la porte n° {}".format(str(res)))
        porte_ouverte=[n for n in range(1,4) if n not in [res, porte_gagnante]][0]
        send_msg("Jeu de Monty Hall", "Le présentateur ouvre la porte n°{}. C'est une chèvre !".format(str(porte_ouverte)))
        res=mon_programme(porte_ouverte)
        send_msg("Jeu de Monty Hall", "Pour cette seconde phase du jeu, vous proposez la porte n°{}".format(str(res)))
        if res==porte_ouverte: send_msg("Jeu de Monty Hall", "Attention ! Vous avez proposé la porte qui a été ouverte ! Votre programme a un souci")
        if porte_gagnante==res:
          send_msg("Jeu de Monty Hall", "Vous avez trouvé la bonne porte ! Bravo !")
          compteur+=1
        else:
          send_msg("Jeu de Monty Hall", "Ce n'était pas la bonne porte. Il fallait choisir la porte n°{}".format(str(porte_gagnante)))
      #On attaque le gros des tests.
      for i in range(1,nb_tests-10):
        porte_gagnante=randint(1,3)
        res=mon_programme(0)
        porte_ouverte=[n for n in range(1,4) if n not in [res, porte_gagnante]][0]
        res=mon_programme(porte_ouverte)
        if porte_gagnante==res:
          compteur+=1     
      #On analyse les résultats.
      proportion=compteur/nb_tests
      if proportion>0.66:
        send_msg("Jeu de Monty Hall", "Bravo ! Votre proportion de victoire sur les {} essais est de {}".format(str(nb_tests),str(proportion)))
        success()
      else:
        send_msg("Jeu de Monty Hall", "Votre proportion de victoire sur les {} essais est de {}. C'est encore trop faible, revoyez votre stratégie.".format(str(nb_tests),str(proportion)))
        fail()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
