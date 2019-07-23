from Euromillion import *
# On rajoute le chemin de ma_bao.py dans le sys.path
sys.path.append("/project/target")
# Ma boite à outils
from ma_bao import * 

if len(mes_numeros)!=5 or len(mes_etoiles)!=2 or len(set(mes_numeros))!=5 or len(set(mes_etoiles))!=2 or not all([0<n<51 for n in mes_numeros]) or not all([0<e<12 for e in mes_etoiles]) : 
    send_msg("Oops! ", "La variable mes_numeros ou mes_etoiles n'est pas valide")
    print("TECHIO> success false")
else : 
    simulation()
    
