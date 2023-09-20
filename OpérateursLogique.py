'''
Operateurs Logique

    not     n'est pas
    and     et logique
    or      ou logique
'''

username = "jean"
password = "1234"

print ("Interface de connexion de la NASA")
print ("_________________________________")

userInput = input("Login:")
passInput = input("Password:")

if userInput==username and passInput==password:
    print (f"Bienvenue {userInput} à la NASA...")
else:
    print("Authentification non valide...")