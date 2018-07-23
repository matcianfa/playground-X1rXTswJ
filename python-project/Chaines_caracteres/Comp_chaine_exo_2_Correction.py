texte="azqcoiihcvobzerajzasoijixbougroizaziabxbncpvirizojasgpoofoabsvhcvxihosaojqxxbbxhjvvwiyagslxmxciabnxqlahxgavvwcbavvwcgsioidhkkgcgkjzbnvxgcahgcxaxgjhxwglja"


solution=""
for lettre in texte :
    if lettre == "z":
        nouvelle_lettre = "a"
    else :
        nouvelle_lettre = chr(ord(lettre)+1)
    solution += nouvelle_lettre
    
