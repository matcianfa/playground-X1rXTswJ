texte = "O temps ! suspends ton vol, et vous, heures propices ! Suspendez votre cours : Laissez-nous savourer les rapides délices Des plus beaux de nos jours !"

for lettre in texte :
    if lettre == "z":
        print("a")
    elif lettre in "abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXY" :
        print(chr(ord(lettre)+1))
    else :
        print(lettre)
