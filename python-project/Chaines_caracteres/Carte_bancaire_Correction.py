def mon_programme(numero):
    somme=0
    if len(numero)==16:
        for i in range(16):
            if i%2==0:
                chiffre=int(numero[i])*2
                if chiffre>9:
                    chiffre-=9
            else:
                chiffre=int(numero[i])
            somme+=chiffre
        if somme%10==0:
            print('VALIDE')
        else:
            print('NON VALIDE')
    else:
        print('NON VALIDE')
