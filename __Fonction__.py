import __Point__ as cp
import __function__ as fonc
import turtle as ttl
import os
import math

class Fonction:
    def __init__(self, fonction, name="f"):
        self.name = name
        self.fonction = fonction
    def __str__(self):
        return self.name + "(x) = "  + self.fonction
    def y(self,x):
        if x < 0:
            x = "(" + str(x) + ")"
        return eval(self.fonction.replace("x", str(x)))

if __name__ == "__main__":
    print("Lancement du module __Fonction__ en cours...")
    f = Fonction("math.cos(x)")
    print(f)
    print(f.y(90))
    print("Fin du module.")
    while 1:
        os.system("pause")