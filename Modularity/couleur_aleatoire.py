import turtle
from random import randint

def couleur_aleatoire():
    '''
    renvoie un triplet de 3 nombres entier compris entre 0 et 255
    Ce triplet correspond à une couleur codée en RVB
    '''
    rouge = randint(0,255)
    bleu = randint(0,255)
    vert = randint(0,255)
    return (rouge,vert,bleu)

if __name__ == '__main__':
    print(couleur_aleatoire())

