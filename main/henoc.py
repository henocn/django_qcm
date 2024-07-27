import random


def presence(liste):
    for proposition in liste:
        if proposition[1] == "vrai" or proposition[1] == "Vrai":
            return True
    else:
        return False

def verifierNombre(qcms):
    if len(qcms) < 10:
        qcms = random.sample(qcms, len(qcms))
    else:
        qcms = random.sample(qcms, 10)
    return qcms

def appreciation(note):
    if note <= 5:
        appreciation = "Totalement insuffisant"
    elif note < 10:
        appreciation = "Insuffisant"
    elif note < 12:
        appreciation = "Passable"
    elif note < 14:
        appreciation = "Assez-Bien"
    elif note < 16:
        appreciation = "Bien"
    elif note < 18:
        appreciation = "Très-bien"
    elif note <= 20:
        appreciation = "Excellent"

    return appreciation