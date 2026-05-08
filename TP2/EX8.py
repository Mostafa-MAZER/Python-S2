def lire_age(age):
    try:
        if age<0:
            raise ValueError("l'age est negatif")
        return "age est verifie"
    except ValueError:
        return "Impossible l'age est negatif"


def lire_note(note):
    try:
        if note<0 or note >20:
            raise ValueError("la note est ne pas comprise entre 0 et 20 ")
        return "la note est comprise"
    except ValueError:
        return "Impossible: la note est ne pas comprise entre 0 est 20 "



def moyenne_notes_valides(notes):
    try:
        somme=0
        for note in notes:
            if note<0 or note>20:
                raise ValueError("note est invalide")
            somme+=note
            return somme/len(notes)
    except ValueError:
        return "Erreur : une note est invalide"

print(moyenne_notes_valides([29,88,-4]))