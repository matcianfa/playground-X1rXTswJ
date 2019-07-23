from random import randint

mes_numeros = [1,2,3,4,5]
mes_etoiles = [1,2]

prix_ticket = 2.5

nb_simulations = 1000000


def tirages():
    tirage=[]
    for i in range(5):
        boule = randint(1,50)
        while boule in tirage :
            boule = randint(1,50)
        tirage.append(boule)
    etoiles = []
    for i in range(2):
        etoile = randint(1,11)
        while etoile in etoiles :
            etoile = randint(1,11)
        etoiles.append(etoile)
    return tirage,etoiles

def resultat(mes_numeros,mes_etoiles,tirage,etoiles) :
    compteur_numeros = 0
    for n in mes_numeros:
        if n in tirage :
            compteur_numeros += 1
    compteur_etoiles = 0
    for e in mes_etoiles:
        if e in etoiles :
            compteur_etoiles += 1
    return compteur_numeros, compteur_etoiles

def donner_gain(n,e) :
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

def simulation() :
    total_gains = 0
    for i in range(nb_simulations):
        tirage,etoiles = tirages()
        n, e = resultat(mes_numeros,mes_etoiles,tirage,etoiles)
        gain = donner_gain(n,e) - prix_ticket
        if gain > 100 :
            print("Au tirage n° {}, j'ai gagné {} euros".format(i,gain))
        total_gains += gain
    print("Au final, j'ai gagné {} en {} tirages ce qui fait une moyenne de {} par tirage".format(total_gains,nb_simulations,total_gains/nb_simulations))
