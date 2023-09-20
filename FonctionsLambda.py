'''
FONCTIONS LAMBDA
----------------
Les fonctions lambda sont en général utilisées dans un certain contexte, 
pour lequel définir une fonction à l'aide de 'def' serait plus long et moins pratique.


syntaxe --> lambda <arg1>,<arg2>,... : instruction de retour
'''

carre = lambda x : x * x

print(carre(55))

addition = lambda nb1, nb2 : nb1 + nb2

print(addition(10,11))


