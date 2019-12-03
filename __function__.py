"""
Ensemble des fonctions utilisées dans __main__
"""
import turtle as ttl

def tortue():
    """
    Créé un tortue
    """
    tortue = ttl.Turtle()
    return tortue

def repere(tortue):
    """
    Trace un repère orthonormé
    """
    tortue.up()
    tortue.goto(0,100)
    tortue.down()
    tortue.home()
    tortue.goto(100,0)
    tortue.up()

def clear_data():
    """
    Efface les données écrites dans le fichier "data.txt"
    """
    fichier = open("data.txt", 'w')
    fichier.write("")
    fichier.close()

if __name__ == "__main__":
    print("Lancement du module __fonction__ en cours...")
    tortue()
    repere(tortue())
    print("Fin du module.")