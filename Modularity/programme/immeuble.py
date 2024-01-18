# module immeuble

from couleur_aleatoire import couleur_aleatoire
from random import randint
from rdc import rdc
from etage import etage
from toit import toit
import turtle

def immeuble(x, y_sol):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
    Cette fonction dessine un immeuble Le nombre d'étage est compris aléatoirement entre 0 et 4
    La couleur de la façade et la couleur de la porte sont tirées au hasard
    '''
    # Nombre d'étage (aléatoire)

    nb_etage = randint(0,4)

    #Couleurs des éléments (aléatoire)

    couleur_facade = couleur_aleatoire()
    couleur_porte = couleur_aleatoire()
    while couleur_facade == couleur_porte :
        couleur_porte = couleur_aleatoire()

    # Dessin du RDC

    rdc(x,y_sol,couleur_facade, couleur_porte)

    # Dessin des étages
    a=0
    for i in range (nb_etage) :
        etage(x,y_sol+60+a,couleur_facade, i+1)

        a+=60
    # Dessin du toit

    toit(x,y_sol,nb_etage)

if __name__ == '__main__':
    immeuble(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()