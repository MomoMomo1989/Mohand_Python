'''
TP2 : Réaliser une fonction qui affiche le nombre de voyelles dans une chaine de caractère, peu importe la casse (Majuscule Minuscule)
'''
voyelles = "aeiouyAEIOUY"

def nbVoy(chaine):
    compteur = 0
    for lettre in chaine:
        if lettre in voyelles : compteur += 1
    return compteur

print(nbVoy("il y a 12 voyelles dans cette phrases."))
