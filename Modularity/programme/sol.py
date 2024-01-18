# Module par sebastien chanthery

import turtle
from trait import trait

# ----- Sol de la rue -----
def sol(y_sol):
    '''
    Paramètres
        y_sol : ordonnée du sol du la rue
    Cete fonction dessine un trait horizontale de 3 pixels d'épaisseur
    '''
    turtle.penup()
    turtle.pensize(3)
    turtle.sety(y_sol)
    turtle.setx(-400)
    turtle.pendown()
    turtle.goto(400,y_sol)
    turtle.pensize(1)

if __name__ == '__main__':
    sol(0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()