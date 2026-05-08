import time

def timer(f):
    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = f(*args, **kwargs)
        fin = time.time()
        print(f"Temps d'exécution: {fin - debut}")
        return resultat
    return wrapper

@timer
def calcul():
    time.sleep(1)

calcul()