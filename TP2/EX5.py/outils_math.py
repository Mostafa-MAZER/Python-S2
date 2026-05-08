
def carre(x):
    return x**2

def cube(x):
    return x**3

def est_pair(n):
    if n%2==0:
        return "nombre pair"
    else:
        return "nombre impair"

def somme_liste(liste):
    somme=0
    for i in liste:
        somme+=i
    return somme