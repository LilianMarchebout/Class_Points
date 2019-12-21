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
            d[str(key)] = l
        chaine = "Addition de " + self.name + " et de " + other.name + ": \n"
        for key in d.keys():
            chaine += str(d[key]) + "\n"
        return chaine
    def __sub__(self, other):
        d = {}
        for key in self.line.keys():
            l = []
            for i in range(len(self.line[key])):
                l.append(self.line[key][i] - other.line[key][i])
            d[str(key)] = l
        chaine = "Soustraction de " + self.name + " et de " + other.name + ": \n"
        for key in d.keys():
            chaine += str(d[key]) + "\n"
        return chaine
    def __mul__(self, other):
        d = {}
        for i in range(len(self.line.keys())):
            l = []
            i = self.line["line" + str(i+1)]


        d[str(i)] = l
        chaine = "Multiplication de " + self.name + " et de " + other.name + ": \n"
        for key in d.keys():
            chaine += str(d[key]) + "\n"
        return chaine

if __name__ == "__main__":
    print("Lancement du module __Point__ en cours...")
    m = Matrice("m", line1=[1,4,4], line2=[6,8,4])
    n = Matrice("n", line1=[2,1,3], line2=[4,1,5])
    print(m)
    print(n)
    print(m + n)
    print("Fin du module.")
    while 1:
        os.system("pause")