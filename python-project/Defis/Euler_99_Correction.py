# L'idée est on ne peut plus bete : on calcule avec le logarithme

# liste nombres sous la forme (base,exp)
liste= # A copier coller
from numpy import log

val_max=0
ligne_max=(0,0)
for i,(base,exp) in enumerate(liste):
    calc=exp*log(base)
    if calc>val_max:
        val_max=calc
        ligne_max=i
       
print(ligne_max+1) # Décalage entre indice et numero de la ligne
