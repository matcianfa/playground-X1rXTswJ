# A modifier si besoin
nom_fonction="ma_fonction"

#liste des valeurs à tester
# Attention de bien mettre dans un tuplet ou une liste les valeurs à tester même si la fonction n'a qu'un argument.
valeurs_a_tester=[(41.6224058529981,8.97565171122551,41.62229757997833,8.975488096475601),(41.6224058529981,8.97565171122551,41.675341599501635,8.90268087387085),(41.6224058529981,8.97565171122551,42.30500714099166,9.154958724975586),(41.6224058529981,8.97565171122551,41.64149675649513,9.01263803243637),(41.36505993656176,9.180021286010742,43.010873394600694,9.419231414794922),(42.57250088260599,8.70941162109375,43.55173333719531,7.14385986328125),(41.36505993656176,9.180021286010742,41.25912361872887,9.229545593261719),(41.6224058529981,8.97565171122551,41.52297166135157,8.967552781105042),]

#message d'aide si besoin
help="N'oublie pas d'utiliser return pour renvoyer le resultat."

#------------------------------------
# Les imports
import sys
# Ma boite à outils
from math import *
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
            rep=f(*valeur)
            sol=f_sol(*valeur)
            assert str(rep) == str(sol), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(",".join([str(val) for val in valeur]),str(rep),str(sol))
            send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(",".join([str(val) for val in valeur]),str(rep)))
        success(chemin+module)
    except AssertionError as e:
        fail()
        send_msg("Oops! ", e)
        if help:
            send_msg("Aide 💡", help)

#--------------------------------------
if __name__ == "__main__": test()
    
