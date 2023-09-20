'''
MODULARITE EN PYTHON : Utiliser les modules
-------------------------------------------
import random
importe le module 'random' , vous devrez donc appeler des fonctions dans random à l'aide du prefixe random.<fonction>

from random import 'random' , randrange
importe le module 'random', mais seulement les fonctions 'randrange' et 'random', donc pas besoin d'indiquer l'espace de nom random !!

from random import *
importe tous les objets du module 'random' dans votre espace de nom actuel, donc pas besoin d'indiquer l'espace de nom 'random' !!

import random as r
'''
import random as r
import os

print(r.random())
print(r.randrange(1000))

os.system("cls")