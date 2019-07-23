# A modifier si besoin
nom_fonction="tirages"

# Test Particulier: il faut tester si les tirages sont corrects
def est_correct(tirage,etoile):
    if len(tirage)!=5 or len(etoile)!=2 or len(set(tirage))!=5 or len(set(etoile))!=2 or not all([0<n<51 for n in tirage]) or not all([0<e<12 for e in etoile]) : return False
    return True

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
        for i in range(100000):
            tirage,etoile=f()
            assert est_correct(tirage,etoile), "La fonction a renvoyé {},{} ce qui n'est pas correct".format(tirage,etoile)
        print("TECHIO> success true")
    except AssertionError as e:
        print("TECHIO> success false")
        send_msg("Oops! ", e)
        if help:
            send_msg("Aide 💡", help)

#--------------------------------------
if __name__ == "__main__": test()
