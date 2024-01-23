'''Importation de modules du projet'''


class Pile:
    ''' Création d'une class Pile qui permettra de gérer les entrées et sorties de valeurs '''
    def __init__(self):  # méthode 1 : constructeur
        ''' Initie les attribut essentiel a la pile '''
        self.donnee = []

    def etre_vide(self):
        ''' Dit si la classe pile est vide '''
        if len(self.donnee) == 0 :
            return True
        return False

    def empiler(self,data):
        ''' Ajoute les éméléments donner a la fin de la pile'''
        self.donnee.append(data)

    def depiler(self):
        ''' Retire la derniere valeur de la pile en la montrant'''
        if self.etre_vide():
            return None
        return self.donnee.pop()

    def acceder_sommet(self):
        ''' Montre la derniere valeur de la pile sans la supprimer'''
        if self.etre_vide():
            return None
        return self.donnee[-1]

    def calculer_taille(self):
        ''' Calcule la taille de la pile'''
        if self.etre_vide():
            return 0
        return  len(self.donnee)

    def afficher(self):
        '''Affiche toute la pile'''
        for i in range(len(self.donnee)):
            print(self.donnee[-1 -i])
