#TP1 Correction.py
'''
TP1 : Python3
-------------
vous êtes stagiaire chez "Maison2Ch'nord" et l'on vous demande 
de créer un programme (sous forme de terminal) permmetant de: 
-Calculer une surface en m2     -> surface = longeur x largeur
-Calculer un volume en m3       -> volume = longeur x largeur x hauteur

Le programme devra afficher la liste des commandes sur demande de l'utilisateur

une commande doit permettre de quitter le programme
'''
dico = {"aide" : "Affiche les commandes du programme" ,
       "surface" : "Calculer la surface en m2" ,
       "volume" : "Calculer le volume en m3" ,
       "quitter" : "Quitter le programme"}
print("Tapez aide pour afficher les commandes")

while True:
    com = input("com>")
    
    if com=="aide":
        print("Liste des commandes du programme")
        print("--------------------------------")
        for k, v in dico.items():
            print(k , ":" , v)
    elif com=="surface":
        lon = input("Longeur ?")
        lar = input("Largeur ?")        
        try:            
            print(f"la surface est de {float(lon)*float(lar)}m2")
        except:
            print("Une erreur s'est produite...")
            continue
    elif com=="volume":
        lon = input("Longeur ?")
        lar = input("Largeur ?")
        hau = input("Hauteur ?")
        try:            
            print(f"le volume est de {float(lon)*float(lar)*float(hau)}m3")
        except:
            print("Une erreur s'est produite...")
            continue
    elif com=="quitter": break
    
    
