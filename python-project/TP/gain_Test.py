# A modifier si besoin
nom_fonction="resultat"

#liste des valeurs à tester
# Attention de bien mettre dans un tuplet ou une liste les valeurs à tester même si la fonction n'a qu'un argument.
valeurs_a_tester=[[5,2],[5,1],[5,0],[4,2],[4,1],[4,0],[3,2],[3,1],[3,0],[2,2],[2,1],[2,0],[1,2],[1,1],[1,0],[0,2],[0,0]]

f_sol(n,e):
    if n == 5 :
        if e == 2 : return 15000000
        elif e == 1 : return 310751
        else : return 51792
    elif n == 4 :
        if e == 2 : return 4143
        elif e == 1 : return 201
        else : return 101
    elif n == 3 :
        if e == 2 : return 59
        elif e == 1 : return 14
        else : return  12
    elif n == 2 :
        if e == 2 : return 19
        elif e == 1 : return 8
        else : return 4
    elif n == 1 :
        if e == 2 : return  10
    return 0
    
    
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
        for valeur in valeurs_a_tester:
            rep=f(*valeur)
            sol=f_sol(*valeur)
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
