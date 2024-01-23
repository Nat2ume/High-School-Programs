'''Importation de modules du projet'''


class Carte:
    ''' Création d'une class Carte qui permettra de creer des cartes'''
    def __init__(self, val, fam):
        ''' Initie les attribut essentiel aux cartes '''
        self.valeur = val
        self.famille = fam
    def get_attributs(self):
        ''' Retourne les données d'une carte'''
        return (self.valeur, self.famille)

    def get_valeur(self):
        ''' Retourne la valeur d'une carte'''
        return self.valeur

    def get_famille(self):
        ''' Retourne la famille d'une carte'''
        return self.famille

    def set_valeur(self, val):  # méthode 5 : un 1er mutateur
        ''' Demande la valeur de la carte
            Fait l'égalité entre val et self.valeur si la valeur existe bien dans val[]
        '''
        if val in ["7", "8", "9", "10", "V", "D", "R", "As"]:
            self.valeur = val
            return True
        return False

    def set_famille(self, fam):  # méthode 6 : un 2ème mutateur
        ''' Demande la famille de la carte
            Fait l'égalité entre fam et self.famille si la famille existe bien dans fam[]
        '''
        if fam in ["Pique", "Coeur", "Carreau", "Trèfle"]:
            self.famille = fam
            return True
        return False
