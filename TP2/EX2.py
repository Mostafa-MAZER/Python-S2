import random
def lancer_de():
    return random.randint(1,6)
print(lancer_de())

def tirer_liste_aleatoire(n,a,b):
    return [random.randint(a,b) for _ in range(n)]
print(tirer_liste_aleatoire(4,1,5))


def choisir_element(liste):
    if not list:
        return None
    return random.choice(liste)
print(choisir_element([1,2,3,4]))


def melanger_liste(liste):
    random.shuffle(liste)
    return liste
print(melanger_liste([1,2,3,4]))