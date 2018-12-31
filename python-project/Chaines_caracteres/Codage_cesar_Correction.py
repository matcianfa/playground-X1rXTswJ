def ma_fonction(n,message):
    message_codé=''
    for lettre in message:
        if 65<=ord(lettre)<=90: #Si c'est une lettre, je la décale de n en utilisant l'astuce du reste de la division euclidienne
            message_codé+=chr((ord(lettre)-65+n)%26 + 65)
        else:
            message_codé+=lettre

    return message_codé
