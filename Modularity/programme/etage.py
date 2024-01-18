from facade import facade
from random import shuffle,randint
from fenetre import fenetre
from fenetre_balcon import fenetre_balcon
import turtle
import random
def etage(x, y_sol, couleur, niveau):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Remarque
       Cette fonction dessine un étage d'un immeuble
    '''

    # dessin des murs

    facade(x,y_sol,couleur,niveau)
    position = -40

    # dessin des 3 Eléments

    for element in range(3):
        if randint(1,2) == 1:
            fenetre(x + position, y_sol + 15)
        else:
            fenetre_balcon(x + position, y_sol)
        position += 40

if __name__ == '__main__':
    etage(0,0,"red",0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()