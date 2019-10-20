def ma_fonction(xA,yA,xB,yB):
    return (yB-yA)/(xB-xA)
    
# S'il on avait voulu considérer la possibilité d'une division par 0,
# On aurait pu faire : 
'''
def ma_fonction(xA,yA,xB,yB):
    if xA == xB :
        return "Impossible"
    else :  
        return (yB-yA)/(xB-xA)

'''
