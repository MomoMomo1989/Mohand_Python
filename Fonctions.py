'''
LES FONCTIONS EN PYTHON
-----------------------
print() input() type() float() str() etc.. ->fonction native de python
Les fonctions permettent de regrouper plusieurs instructions dans un bloc qui sera appelé grâce à un nom.
Bonne pratique une fonction = 1 traitement

2 type de fonctions : 
    print()-->ne retourne rien
    input()-->retourne une valeur que l'on peu stocker dans une variable

En c# par exemple la signature d'une fonction depend de son nom et du type de chacun de ses paramètres, en Python : Typage dynamique donc la signature est son nom, c'est donc la derniére qui ecrase les précedentes

mot cle : def (define)---> def <nomFonction>:

'''
def table2():
    for i in range(11):
        print(f"{i} * 2 = {i*2}")

def table(x):
    for i in range(11):
        print(f"{i} * {x} = {i*x}")
        
def ditBonjour(nom="parein" , prenom="jean", age=44):
    print(f"Bonjour je suis {nom} {prenom}, j'ai {age} ans")

def affiche(*mots):
    for m in mots:
        print(m)
        
def table2():
    print("je suis la fonction table2")
    
table2()


