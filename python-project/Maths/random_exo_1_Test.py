#Ne pas oublier de changer le module à importer
module="Maths/random_exo_1"
import sys
import io
#On récupère les données de l'utilisateur
sauvegarde_stdout=sys.stdout
sys.stdout=io.StringIO()
# On va simuler beaucoup de lancer pour vérifier que la répartition de la somem des deux dés est cohérente
compteur=[0]*13
N_essais=1000000
# précision de la vérification
precision = 0.001
for _ in range(N_essais):
    from random_exo_1 import *
    count1 = sys.stdout.getvalue()[:-1]
    compteur[int(count1)]+=1
compteur=[k/N_essais for k in compteur]
sys.stdout=sauvegarde_stdout
#from ma_bao import *

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

#La réponse
reponse=[0,0,1/36,2/36,3/36,4/36,5/36,6/36,5/36,4/36,3/36,2/36,1/36]


#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat."

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
      assert all([abs(a-b)<precision for (a,b) in zip(compteur,reponse)]), "Le résultat obtenu est {} mais ce n'est pas le bon.".format(str(count1))
      send_msg("Tests validés","Le résultat cherché est bien {}".format(str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
