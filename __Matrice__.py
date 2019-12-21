import os

class Matrice:
    def __init__(self, name="m",**line):
        self.name = name
        self.line = line
    def __str__(self):
        chaine = self.name + " = \n"
        for key in self.line.keys():
            chaine += str(self.line[key]) + "\n"
        return chaine
    def __add__(self, other):
        d = {}
        for key in self.line.keys():
            l = []
            for i in range(len(self.line[key])):
                l.append(self.line[key][i] + other.line[key][i])
                d["line"+ str(i+1)] = l
        chaine = "Addition de " + self.name + " et de " + other.name + ": \n"
        for key in d.keys():
            chaine += str(d[key]) + "\n"
        return chaine

if __name__ == "__main__":
    print("Lancement du module __Point__ en cours...")
    m = Matrice("m", line1=[56,54], line2=[51,0])
    n = Matrice("n", line1=[45,0], line2=[0,55])
    print(m)
    print(n)
    add = m + n
    print(add)
    print("Fin du module.")
    while 1:
        os.system("pause")