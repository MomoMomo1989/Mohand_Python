'''
Structures de données : Dictionnaires

dico = {}   Dictionnaire vide
dico = {<key>:<value> , <key2>:<value2>}
        paire (clé:valeur)

Lire une valeur : dico[<key>]
ajout/modification d'une valeur : dico[<key>] = <value>

pop     Supprimer une paire du dico
clear   supprime le dico
copy    copier un dictionnaire

boucle
------
for val in dico.values():
for key in dico.keys():
for key , value in dico.items():

'''
dico = {"prenom":"jean-philippe" , 
        "nom":"parein" , 
        "age": 44}

if "taille" in dico:
    print ("la clé est présent")
else:
    print ("la cle est absente")


