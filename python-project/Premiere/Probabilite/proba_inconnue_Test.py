# A modifier si besoin
nom_fonction="ma_fonction"


sol=[0.1234,0.5678,0.3088]


#message d'aide si besoin
help="N'hésitez pas à augmenter le nombre d'essais"

#------------------------------------
# Les imports
import sys
# On rajoute le chemin de ma_bao.py dans le sys.path
sys.path.append("/project/target")
# Ma boite à outils
from ma_bao import * 
# Donne les noms du dossier et du module (automatiquement avec __file__
chemin,module=donner_chemin_nom(__file__)
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

        rep=f()
        assert all([r==s for r,s in zip(rep,sol)]), "Le résultat obtenu est {} mais ce n'est pas assez précis.".format(str(rep))
        send_msg("Tests validés","Le résultat obtenu est bien {}".format(str(rep)))
        success(chemin+module)
    except AssertionError as e:
        fail()
        send_msg("Oops! ", e)
        if help:
            send_msg("Aide 💡", help)

#--------------------------------------
if __name__ == "__main__": test()
