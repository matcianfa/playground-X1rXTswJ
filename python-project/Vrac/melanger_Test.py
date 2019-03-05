from random import randint

# A modifier si besoin
nom_fonction="mélanger"

#liste des valeurs à tester
# Attention de bien mettre dans un tuplet ou une liste les valeurs à tester même si la fonction n'a qu'un argument.
valeurs_a_tester=[[1,2,3,4,5],[1,2,3,1,2,3],[randint(0,1000) for _ in range(200)]]


#message d'aide si besoin
help="N'oublie pas d'utiliser return pour renvoyer le resultat."

#------------------------------------
# Les imports
import sys
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
# On récupère la fonction solution
exec("from {}_Correction import {} as f_sol".format(module,nom_fonction))

#--------------------------------------
def test():
    try:
        for valeur in valeurs_a_tester:
            val=valeur.copy()
            rep=f(val)
            val=valeur.copy()
            sol=f_sol(val)
            assert str(sorted(rep)) == str(sorted(sol)), "En testant les valeurs {} le résultat obtenu est {}".format(str(valeur),str(rep))
            send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(valeur),str(rep)))
        success(chemin+module)
    except AssertionError as e:
        fail()
        send_msg("Oops! ", e)
        if help:
            send_msg("Aide 💡", help)

#--------------------------------------
if __name__ == "__main__": test()
