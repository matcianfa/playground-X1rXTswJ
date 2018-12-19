# A modifier si besoin
dossier="Variables_et_fonctions/"
module="Bases_armees"
nom_fonction="ma_fonction"

#liste des valeurs à tester
# Attention de bien mettre dans un tuplet ou une liste les valeurs à tester même si la fonction n'a qu'un argument.
valeurs_a_tester=[(1,1),(1,6),(5,1),(5,6),(8,4),(13,25),(15,27)]

#message d'aide si besoin
help="N'oublie pas d'utiliser return pour afficher le resultat."

# Les imports
import sys
# Ma boite à outils
from ma_bao import * 
# On teste s'il n'y a pas d'erreurs de synthaxe etc. et on les montre si besoin
tester("from {} import *".format(module),globals()) 
# On renomme ma fonction f
f=eval(nom_fonction)
# Si le mot de passe est bon on affiche la correction
try :  
    cheat(dossier+module,mdp) 
except: pass
# On récupère la fonction solution
exec("from {}_Correction import {} as f_sol".format(module,nom_fonction))


def test():
    try:
        for valeur in valeurs_a_tester:
            rep=f(*valeur)
            sol=f_sol(*valeur)
            assert str(rep) == str(sol), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(valeur),str(rep),str(sol))
            send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(valeur),str(rep)))
        success(dossier+module)
    except AssertionError as e:
        fail()
        send_msg("Oops! ", e)
        if help:
            send_msg("Aide 💡", help)


if __name__ == "__main__": test()
