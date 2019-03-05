def hanoi(n,debut,inter,fin):
    if n>0:
        hanoi(n-1,debut,fin,inter)
        print(debut+" "+fin)
        hanoi(n-1,inter,debut,fin)
