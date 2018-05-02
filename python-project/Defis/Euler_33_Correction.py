# On va multiplier au fur et à mesure les numérateurs et dénominateurs qu'on trouve
produit_numerateur=1
produit_denominateur=1

# L'idée est simple : on transforme le numérateur et dénominateur en chaine de caractères
# et on cherche si un des chiffres du numérateur est égale à un des chiffres du dénominateur
# Si c'est le cas on teste si la fraction de départ est égale à celle simplifiée (en utilisant la caractérisation par le produit en croix)
for numerateur in range(10,99):
    for denominateur in range(numerateur+1,100):
        num=str(numerateur)
        den=str(denominateur)
        for i in range(2):
            for j in range(2):
                if num[i]==den[j]!="0" and numerateur*int(den[1-j])==denominateur*int(num[1-i]):
                    produit_numerateur*=numerateur
                    produit_denominateur*=denominateur

# il reste maintenant à simplifier la fraction produit_numerateur/produit_denominateur pour en tirer le dénominateur réduit
# Pour calculer le PGCD de a et b on utilise l'algorithme d'Euclide
def PGCD(a,b):
    if(b==0):
        return a
    else:
        return PGCD(b,a%b)

print(produit_denominateur//PGCD(produit_numerateur,produit_denominateur))
