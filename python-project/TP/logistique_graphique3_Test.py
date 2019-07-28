# Les imports
import sys
# On rajoute le chemin de ma_bao.py dans le sys.path
sys.path.append("/project/target")
# Ma boite à outils
from ma_bao import * 
# Donne les noms du dossier et du module (automatiquement avec __file__
chemin,module=donner_chemin_nom(__file__)
# Si le mot de passe est bon on affiche la correction
try :  
    cheat(chemin+module,mdp) 
except: pass

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

fig=plt.figure()
from logistique_graphique3 import dessiner

mus=[ 3.5,3.7,3.9, 4]
r = matplotlib.patches.Rectangle((0,0), 1, 1, fill=False, edgecolor='none', visible=False)
for i in range(1,5):
    plt.subplot(2,2,i)
    dessiner(mus[i-1],0.9,30)
    plt.legend(loc = "lower right",handles=[r],labels=["mu={}".format(mus[i-1])],framealpha=0.5)
plt.show()

fig.savefig('output.png', dpi=fig.dpi)
print("TECHIO> open -s /project/target/ index_grossissant.html")
