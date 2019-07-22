# -*- coding: utf-8 -*

#from math import gcd
def gcd(a,b):
    if b==0 : return a
    return gcd(b,a%b)


class Fraction :

    def __init__(self,a,b):
        """
        Permet d'initialiser notre classe. Indispensable !
        """
        if b==0 : raise ZeroDivisionError
        if b<0 : a,b=-a,-b
        self.num = a
        self.den = b

    def __str__(self):
        """
        Permet de choisir ce que l'ont souhaite renvoyer lorsqu'on applique str ou print à  notre classe
        """
        if self.den == 1 : return self.num
        return "{} / {}".format(self.num,self.den)

    def reduire(self):
        """
        Permet de réduire une fraction
        """
        pgcd=gcd(self.num,self.den)
        return Fraction(self.num//pgcd,self.den//pgcd)

    def __eq__(self,fraction2):
        """
        Permet de définir ce qu'on doit faire lorsqu'on teste self==fraction2
        """
        return self.num * fraction2.den == self.den * fraction2.num

    def __lt__(self,fraction2):
        """
        Permet de définir ce qu'on doit faire lorsqu'on teste self==fraction2
        """
        return self.num * fraction2.den < self.den * fraction2.num

    def __le__(self,fraction2):
        """
        Permet de définir ce qu'on doit faire lorsqu'on teste self==fraction2
        """
        return self.num * fraction2.den <= self.den * fraction2.num

    def __add__(self,fraction2):
        """
        Permet de redéfinir l'addition
        """
        return Fraction(self.num * fraction2.den + self.den * fraction2.num, self.den * fraction2.den).reduire()

    def __sub__(self,fraction2):
        """
        Permet de redéfinir la soustraction
        """
        return Fraction(self.num * fraction2.den - self.den * fraction2.num, self.den * fraction2.den).reduire()

    def __mul__(self,fraction2):
        """
        Permet de redéfinir la multiplication
        """
        return Fraction(self.num * fraction2.num, self.den * fraction2.den).reduire()

    def __truediv__(self,fraction2):
        """
        Permet de redéfinir la division
        """
        return Fraction(self.num * fraction2.den, self.den * fraction2.num).reduire()










