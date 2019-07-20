#Ne pas oublier de changer le module à importer
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
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

fig=plt.figure()
import Newton_graphique
fig.savefig('output.png', dpi=fig.dpi)
print("TECHIO> open -s /project/target/ index_grossissant.html")
