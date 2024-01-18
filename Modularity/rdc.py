from random import shuffle, randint
from facade import facade
from porte import porte
from porte2 import porte2
from fenetre import fenetre
import turtle

def rdc(x, y_sol, c_facade, c_porte):
    '''
    Paramètres
        x : (int) abscisse du centre
        y_sol : ordonnée du sol du la rue
        c_facade : couleur de la façade
        c_porte : couleur de la porte
    remarque:
        Cette fonction dessine le rdc en 2 étapes
        D'abord la façade
        Puis les 3 élements : 1 porte et 2 fenêtres disposées au hasard
    '''
    # Dessine la facade

    facade(x,y_sol,c_facade,0)

    # Construit les 3 éléments (1 porte et 2 fenetres)

    ordre = ["fenetre", "fenetre", "porte"]
    shuffle(ordre)
    position = -40


    for element in ordre:
        if element == "porte":
            if randint(1,2) == 1:
                porte(x + position, y_sol, c_porte)
            else:
                porte2(x + position, y_sol, c_porte)
        if element == "fenetre":
            fenetre(x + position, y_sol + 15)
        position += 40

if __name__ == '__main__':
    rdc(0,0,"red","green")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()