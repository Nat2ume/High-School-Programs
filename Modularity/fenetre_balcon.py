import turtle
from rectangle import rectangle
from trait import trait
from porte import porte
def fenetre_balcon(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    Remarque:
        Dessine une porte-fenetre avec balcon en 2 temps: la porte fenetre de 30 pixels de large par 50 pixels de hauteur
        puis le balcon
    '''
    # porte-fenetre
    porte(x,y,"white")
    turtle.penup()
    turtle.pensize(2)
    rectangle(x, y, 40, 25)
    trait(x, y, x, y + 25)
    trait(x+5, y, x+5, y + 25)
    trait(x + 10, y, x + 10, y + 25)
    trait(x + 15, y, x + 15, y + 25)
    trait(x - 5, y, x - 5, y + 25)
    trait(x - 10, y, x - 10, y + 25)
    trait(x - 15, y, x - 15, y + 25)
    turtle.pensize(1)



    # balcon


    pass



if __name__ == '__main__':
    fenetre_balcon(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()