'''
LES FONCTIONS Valeurs de retour des fonctions
---------------------------------------------
2 type de fonctions : 
    print()-->ne retourne rien (procedure)
    input()-->retourne une valeur que l'on peu stocker dans une variable

mot cle : def (define)---> def <nomFonction>:
return : renvoyer des valeurs

'''

def addition(nb1 , nb2):
    return nb1 + nb2
    print("ceci est une addition")

def additionSoustraction(nb1 , nb2):
    return (nb1 + nb2 , nb1 - nb2)

print(additionSoustraction(10,5))

(add , sous) = additionSoustraction (10,5)
print(f"addition:{add}      soustraction:{sous}")

def pgq10(nb):
    if nb>10: return "c'est vrai"
    elif nb<10: return "c'est faux"
    else: return "égal a 10"
    
print (pgq10(10))

