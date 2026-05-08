import math
def division_securisee(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Erreur : division par zero impossible"

def racine_securisse(x):
    try:
        if x<0:
            raise ValueError("Nombre negatif")
        return math.sqrt(x)
    except ValueError:
        return "Erreur : impossible la racine d'un nombre negatif"
print(racine_securisse(-3))
    
def conversion_entier(texte):
    try:
        return int(texte)
    except ValueError:
        return "Erreur : conversion impossible en entier"
    