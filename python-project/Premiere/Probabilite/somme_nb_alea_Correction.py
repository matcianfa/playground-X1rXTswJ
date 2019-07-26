from random import random
N = 10000000

def ma_fonction():
    S = 0
    for _ in range(N):
        somme = 0
        n = 0
        while somme < 1 :
            somme += random()
            n += 1
        S += n
    return S/N
