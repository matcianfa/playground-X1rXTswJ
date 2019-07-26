#liste des valeurs à tester
# Attention de bien mettre dans un tuplet ou une liste les valeurs à tester même si la fonction n'a qu'un argument.
valeurs_a_tester=[3,10,50,100]


#message d'aide si besoin
help="N'oublie pas d'utiliser return pour renvoyer le resultat."

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
# Si le mot de passe est bon on affiche la correction
try :  
    cheat(chemin+module,mdp) 
except: pass
# On récupère la fonction solution
exec("from {}_Correction import u as u_sol, x as x_sol,y as y_sol".format(module))

#--------------------------------------
def test():
    try:
        for valeur in valeurs_a_tester:
            ru,rx,ry = u(valeur),x(valeur),y(valeur)
            su,sx,sy = u_sol(valeur),x_sol(valeur),y_sol(valeur)
            assert abs(ru-su)<10**(-13) and all([abs(x-xs)<10**(-13) for x,xs in zip(rx,sx)]) and all([abs(y-ys)<10**(-13) for y,ys in zip(ry,sy)]), "En testant la valeur n={} le résultat obtenu est u(n)={}, x(n)={} et y(n) ={} au lieu de u(n)={}, x(n)={} et y(n) ={}".format(str(valeur),str(ru),str(rx),str(ry),str(su),str(sx),str(sy))
            send_msg("Tests validés","En testant la valeur n={} le résultat obtenu est u(n)={}, x(n)={} et y(n) ={}.".format(str(valeur),str(ru),str(rx),str(ry)))
        success(chemin+module)
    except AssertionError as e:
        fail()
        send_msg("Oops! ", e)
        if help:
            send_msg("Aide 💡", help)

#--------------------------------------
if __name__ == "__main__": test()
