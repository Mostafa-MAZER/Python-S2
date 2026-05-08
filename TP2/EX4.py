import os

def repertoire_courant():
    return os.getcwdb()
print(repertoire_courant())

def contenu_repertiore(chemin):
    return os.listdir(chemin)
print(contenu_repertiore("."))

def fichier_existe(chemin):
    if os.path.exists(chemin):
        return True
    else:
        return False

def creer_dossier(nom_dossier):
    if not os.path.exists(nom_dossier):
         os.mkdir(nom_dossier)
         return True
    else:
        return False

def compter_fichiers(chemin):
    return len([f for f in os.listdir(chemin)
                if os.path.isfile(os.path.join(chemin, f))])