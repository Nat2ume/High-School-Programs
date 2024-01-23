'''Importation de modules du projet'''
# Importations d’une librairie standard
from random import *
# Importation de modules du projet
from carte import *
# Création des listes familles et valeurs avant de les utiliser
liste_familles = ["Pique", "Coeur", "Carreau", "Trèfle"]
liste_valeurs = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R", ]

class JeuCarte:
    ''' Création d'une class JeuCarte qui permettra de gérer toutes les cartes '''
    def __init__(self, modele):
        ''' Initie les attribut essentiel au jeu de carte '''
        if modele in ["32", "52"]:
            self.modele = modele
            if modele == "32":
                self.jeu = [Carte(v, f) for v in [liste_valeurs[0]]
                            + liste_valeurs[6:] for f in liste_familles]
            else:
                self.jeu = [Carte(v, f) for v in liste_valeurs for f in liste_familles]
        else:
            print("Création non licite")
            return None

    def get_modele(self):
        ''' Retourne le nombre de carte dans le jeu'''
        return self.modele

    def get_jeu(self):
        ''' Retourne toutes les cartes du jeu'''
        return [c.get_attributs() for c in self.jeu]

    def set_modele(self, modele):
        ''' Demande le modèle du jeu 
            Recrée le jeu (self.jeu) si le modèle est différent de self.modele
        '''
        if modele == self.modele:
            pass
        elif modele in ["32", "52"]:
            self.modele = modele
            if modele == "32":
                self.jeu = [Carte(v, f) for v in [liste_valeurs[0]]
                            + liste_valeurs[6:] for f in liste_familles]
            else:
                self.jeu = [Carte(v, f) for v in liste_valeurs for f in liste_familles]
                return True
        else:
            return False

    def tirer_carte(self):
        ''' Affiche la carte du dessus '''
        return choice(self.jeu).get_attributs()

    def melanger_jeu(self):
        ''' Mélange le jeu complet '''
        shuffle(self.jeu)

