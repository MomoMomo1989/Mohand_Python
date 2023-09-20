'''
Structures de données : Listes
------------------------------
append      Ajouter un element à la fin de la liste
insert      Ajouter un element selon un index
remove      Supprimer un element par sa valeur
pop         Supprimer un element par son index
index       Afficher l'index selon une valeur
count       Nombre de fois ou l'element apparait
sort        Trier par ordre croissant
reverse     inverser l'odre de la liste
copy        Copie d'une liste
extend      Etendre une liste
clear       Effacer une liste
'''
maListe = ["zoe" , "marc" , "alain" , "adrien"]


for element in maListe:
    print(element)

maListe2 = maListe[:]
print("--------")

for element in maListe2:
    print(element)
