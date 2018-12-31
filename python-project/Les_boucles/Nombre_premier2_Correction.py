from math import *

def ma_fonction(n):
    if n<2 or (n%2==0 and n!=2):
        return 'PAS PREMIER'
    else:
        for d in range(3,int(sqrt(n))+1,2):
            if n%d==0:
                return 'PAS PREMIER'
                break
        else:
            return 'PREMIER'
