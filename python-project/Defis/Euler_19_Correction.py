# Associons les jours à un nombre modulo 7. comme c'est dimanche qui nous interesse : dimanche correspond à 0, lundi au 1 etc.
# Comme le premier janvier 1900 est un lundi (donc 1) le premier janvier 1901 correspond à 1+365%7
jour_de_la_semaine = 366%7
# Liste des jours par mois:
liste_jours_normale=[31,28,31,30,31,30,31,31,30,31,30,31]
liste_jours_bissextile=[31,28,31,30,31,30,31,31,30,31,30,31]
# Compteur qui compte le nombre de dimanche qui tombe un premier du mois
compteur=0
for année in range(1901,2001):
    if année%4==0: #le seul siècle à considérer est 2000 qui est bissextil
        liste_jours=liste_jours_bissextile
    else:
        liste_jours=liste_jours_normale
    for jours in liste_jours:# pour chaque mois, on rajoute le nombre de jours
        jour_de_la_semaine=(jour_de_la_semaine+jours)%7
        if jour_de_la_semaine==0: # Si c'est un dimanche, on le compte
            compteur+=1

print(compteur)

#------------------------------------------------------------------------------
# Version utilisant le module gérant directement les dates
#------------------------------------------------------------------------------
# En utilisant les fonctions qui donnent directement les dates et les jours de la semaines
# Le dimanche correspond à 6
from datetime import *

compteur=0 # Compteur qui compte le nombre de dimanches qui tombent un premier du mois
la_date=date(1901,1,1) # On commence le 1 janvier 1901
while la_date<date(2001,1,1):
    if la_date.day==1 and la_date.weekday()==6 : # Si le jour est le premier du mois et le jour de la semaine est 6 (un dimanche)
        compteur+=1
    la_date += timedelta(1) # On rajoute un jour à la date

print(compteur)
