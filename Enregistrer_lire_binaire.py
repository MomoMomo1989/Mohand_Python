'''
Gestion des fichiers en Python : Enregister et lire dans un fichier binaire
'''

class Humain():
    '''
    Classe des Humains
    '''
    def __init__(self, nom , prenom):
        '''
        Constructeur de classe
        '''
        self.nom = nom
        self.prenom = prenom
    
    def Info(self):
        '''
        Fonction d'information de l'objet
        '''
        print(f"je suis {self.nom} {self.prenom}")
        

h1 = Humain("parein" , "jean-philippe")
h1.Info()