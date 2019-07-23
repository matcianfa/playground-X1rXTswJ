# A modifier si besoin
nom_fonction="resultat"

#liste des valeurs à tester
# Attention de bien mettre dans un tuplet ou une liste les valeurs à tester même si la fonction n'a qu'un argument.
valeurs_a_tester=[[[[1,2,3,4,5],[6,7],[2,4,6,8,10],[7,11]],(2,1)],[[[1,2,3,4,5],[6,7],[5,4,3,2,1],[7,6]],(5,2])],[[[1,2,3,4,5],[6,7],[9,7,6,8,10],[1,11]],(0,0)]]

#message d'aide si besoin
help=""

#------------------------------------
# Les imports
import sys
# On rajoute le chemin de ma_bao.py dans le sys.path
sys.path.append("/project/target")
# Ma boite à outils
from ma_bao import * 
# Donne les noms du dossier et du module (automatiquement avec __file__
chemin,module=donner_chemin_nom(__file__)
module = "Euromillion"
# On teste s'il n'y a pas d'erreurs de synthaxe etc. et on les montre si besoin
tester("from {} import *".format(module),globals()) 
# On renomme ma fonction f
f=eval(nom_fonction)
# Si le mot de passe est bon on affiche la correction
try :  
    cheat(chemin+module,mdp) 
except: pass


#--------------------------------------
def test():
    try:
        for valeur,sol in valeurs_a_tester:
            rep=f(*valeur)
            assert str(rep) == str(sol), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(",".join([str(val) for val in valeur]),str(rep),str(sol))
            send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(",".join([str(val) for val in valeur]),str(rep)))
        print("TECHIO> success true")
    except AssertionError as e:
        print("TECHIO> success false")
        send_msg("Oops! ", e)
        if help:
            send_msg("Aide 💡", help)

#--------------------------------------
if __name__ == "__main__": test()
