
import sys
import io
module="Variables_et_fonctions/Calcul_distance_vol_oiseau"
from ma_bao import *
tester("from Calcul_distance_vol_oiseau import mon_programme",globals())


#liste des couples input/output
input_output=[\
((41.6224058529981,8.97565171122551,41.62229757997833,8.975488096475601),"0.018","Salle 126 / Cafeteria"),\
((41.6224058529981,8.97565171122551,41.675341599501635,8.90268087387085),"8.45","Salle 126 / Propriano"),\
((41.6224058529981,8.97565171122551,42.30500714099166,9.154958724975586),"77.336","Salle 126 / Université de Corte"),\
((41.6224058529981,8.97565171122551,41.64149675649513,9.01263803243637),"3.736","Salle 126 / Granace"),\
((41.36505993656176,9.180021286010742,43.010873394600694,9.419231414794922),"184.064","Extreme sud / Cap Corse"),\
((42.57250088260599,8.70941162109375,43.55173333719531,7.14385986328125),"167.429","Corse / France"),\
((41.36505993656176,9.180021286010742,41.25912361872887,9.229545593261719),"12.485","Corse / Sardaigne"),\
((41.6224058529981,8.97565171122551,41.52297166135157,8.967552781105042),"11.077","Salle 126 / mon lit")\
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
      for inp,outp,texte in input_output:
        sauvegarde_stdout=sys.stdout
        sys.stdout=io.StringIO()
        mon_programme(*inp)
        count1 = sys.stdout.getvalue()[:-1]
        sys.stdout=sauvegarde_stdout
        assert str(count1) == str(outp), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","La distance {} est bien {} kilomètres".format(texte,str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__":
  test()
