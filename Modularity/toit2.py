import turtle
from trait import trait

def toit2(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit plat d'épaisseur 10 pixels et mesurant 140 pixels de large
    '''
    turtle.pensize(10)
    if niveau == 0:
        turtle.penup()
        trait(x-70, y_sol + 60, x + 70, y_sol + 60 )
    elif niveau == 1:
        turtle.penup()
        trait(x-70, y_sol + 2*60, x + 70, y_sol + 2*60 )
    elif niveau == 2:
        turtle.penup()
        trait(x-70, y_sol + 3*60, x + 70, y_sol + 3*60 )
    elif niveau == 3:
        turtle.penup()
        trait(x-70, y_sol + 4*60, x + 70, y_sol + 4*60 )
    else :
        turtle.penup()
        trait(x-70, y_sol + 5*60, x + 70, y_sol + 5*60 )
    turtle.pensize(1)



if __name__ == '__main__':
    toit2(0,0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()