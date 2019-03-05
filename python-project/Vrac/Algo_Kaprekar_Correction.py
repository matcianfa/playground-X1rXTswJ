def ma_fonction(n):
    carré=str(n**2)
    for i in range(1,len(carré)):
        if int(carré[:i])+int(carré[i:])==n:
            return "KAPREKAR"
            break
    else:
        return "PAS KAPREKAR"
