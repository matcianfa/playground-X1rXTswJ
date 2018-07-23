texte="azqcoiihcvobzerajzasoijixbougroizaziabxbncpvirizojasgpoofoabsvhcvxihosaojqxxbbxhjvvwiyagslxmxciabnxqlahxgavvwcbavvwcgsioidhkkgcgkjzbnvxgcahgcxaxgjhxwglja"


for lettre in texte :
    if lettre == "z":
        nouvelle_lettre = "a"
    else :
        nouvelle_lettre = chr(ord(lettre)+1)
    print(nouvelle_lettre)
    
