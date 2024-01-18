import turtle
from trait import trait

def toit1(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    '''
    if niveau == 0:
        turtle.penup()
        turtle.fillcolor("black")
        turtle.begin_fill()
        trait(x-80, y_sol + 60, x + 80, y_sol + 60 )
        trait(x+80, y_sol + 60, x, y_sol + 60 + 40 )
        trait(x, y_sol + 60 + 40, x-80, y_sol + 60)
        turtle.end_fill()
    elif niveau == 1:
        turtle.penup()
        turtle.fillcolor("black")
        turtle.begin_fill()
        trait(x-80, y_sol + 2*60, x + 80, y_sol + 2*60 )
        trait(x+80, y_sol + 2*60, x, y_sol + 2*60 + 40 )
        trait(x, y_sol + 2*60 + 40, x-80, y_sol + 2*60)
        turtle.end_fill()
    elif niveau == 2:
        turtle.penup()
        turtle.fillcolor("black")
        turtle.begin_fill()
        trait(x-80, y_sol + 3*60, x + 80, y_sol + 3*60 )
        trait(x+80, y_sol + 3*60, x, y_sol + 3*60 + 40 )
        trait(x, y_sol + 3*60 + 40, x-80, y_sol + 3*60)
        turtle.end_fill()
    elif niveau == 3:
        turtle.penup()
        turtle.fillcolor("black")
        turtle.begin_fill()
        trait(x-80, y_sol + 4*60, x + 80, y_sol + 4*60 )
        trait(x+80, y_sol + 4*60, x, y_sol + 4*60 + 40 )
        trait(x, y_sol + 4*60 + 40, x-80, y_sol + 4*60)
        turtle.end_fill()
    else :
        turtle.penup()
        turtle.fillcolor("black")
        turtle.begin_fill()
        trait(x-80, y_sol + 5*60, x + 80, y_sol + 5*60 )
        trait(x+80, y_sol + 5*60, x, y_sol + 5*60 + 40 )
        trait(x, y_sol + 5*60 + 40, x-80, y_sol + 5*60)
        turtle.end_fill()


if __name__ == '__main__':
    toit1(0,0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()