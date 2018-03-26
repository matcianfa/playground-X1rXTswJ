# dictionnaire pour passer du nombre au nombre de lettres pour l'écrire
dictionnaire = {0:0, 1:3, 2:3, 3:5,4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3,11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6}

# fonction qui donne le nombre de lettres d'un nombre
def nombre_lettres(n):
    if n==1000 : return 11
    if n%100==0 : return nombre_lettres(n//100) + 7 # multiple de 100 sans and
    if n>100:
        return nombre_lettres(n//100) + 10 + nombre_lettres(n%100) # Le chiffre des centaines + "hundred and" + le nombre des dizaines-unités
    if n>20 :
        return dictionnaire[(n//10)*10] + dictionnaire[n%10]
    return dictionnaire[n]

print(sum([nombre_lettres(n) for n in range(1,1001)]))
