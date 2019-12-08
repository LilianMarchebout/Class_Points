import math
import os
import turtle as ttl
import __function__ as fonc

class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.norme = math.sqrt((self.x)**2 + (self.y)**2)
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
    def __add__(self, other):
        return Vecteur(self.x + other.x, self.y + other.y)
    def colineaire(self, other):
        """
        Verifie si deux vecteurs sont colinéaires, renvoie True si c'est vrai, sinon renvoie False
        """
        try:
            k = [self.x/other.x, self.y/other.y]
        except ZeroDivisionError:
            if other.x == 0 and other.y != 0:
                k = [0, self.y/other.y]
            elif other.y == 0 and other.x != 0:
                k = [self.x/other.x, 0]
            elif other.x == 0 and other.y == 0:
                k = [0,0]
        if k[0] == k[1] or k[0] == 0 or k[1] == 0:
            return True
        else:
            return False
    def produit_scalaire(self, other):
        """
        Calcule le produit scalaire de deux vecteurs
        """
        return self.x * other.x + self.y * other.y
        #return fonc.int_decimal(1/2*((self.norme)**2 + (other.norme)**2 - round(((self+other).norme)**2, 4)))
    def angle_degree(self, other):
        """
        Definit l'angle entre deux vecteurs en degree
        """
        try:
            return math.degrees(math.acos((self.produit_scalaire(other))/(self.norme * other.norme)))
        except ZeroDivisionError:
            return math.degrees(math.acos(self.produit_scalaire(other)))
    def angle_radian(self, other):
        """
        Definit l'angle entre deux vecteurs en radian
        """
        return math.acos((self.produit_scalaire(other))/(self.norme * other.norme))
    def tracage(self):
        """
        Trace le vecteur
        """
        tortue = fonc.tortue()
        tortue.up()
        tortue.home()
        tortue.left(self.angle_degree(Vecteur(100,0)))
        tortue.down()
        tortue.goto(self.x,self.y)
        tortue.up()

if __name__ == "__main__":
    print("Lancement du module __Vecteur__ en cours...")
    a = Vecteur(-40,20)
    b = Vecteur(50,100)
    a.tracage()
    b.tracage()
    print(a.angle_degree(b))
    print(a.produit_scalaire(b))
    print("Fin du module.")
    while 1:
        os.system("pause")