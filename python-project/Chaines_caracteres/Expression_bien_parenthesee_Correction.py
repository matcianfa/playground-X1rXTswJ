def mon_programme(expression):
    compteur_parenthèse=0
    for c in expression:
        if c=='(' :
            compteur_parenthèse+=1
        elif c==')':
            compteur_parenthèse-=1
            if compteur_parenthèse<0:
                break
    if compteur_parenthèse==0:
        print('BIEN PARENTHESEE')
    else:
        print('MAL PARENTHESEE')
