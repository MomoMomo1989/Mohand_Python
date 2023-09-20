'''
Erreurs et exceptions
---------------------
try:    tester un bloc de code
except: le bloc est executé en cas d'erreur
except<NomException>:
except(<NomException1>,<NomException2>):
except  Exception as err:
else:   Executer si aucune exeption n'est levée
finally:Bloc executé aprés que tous les autres blocs aient été exécutés
'''

nb1 = input("nb1?")
nb2 = input("nb2?")
try:
    print (int(nb1) / int(nb2))
except:
    pass

print ("fin du programme")

    

