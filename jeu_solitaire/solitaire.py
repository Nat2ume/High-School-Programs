'''Importation de modules du projet'''
from pile_liste import*
from carte import*
from jeu_carte import*

class Solitaire:
    ''' Création d'une class Solitaire qui permettra de jouer au solitaire '''
    def __init__(self):
        ''' Initie les attribut essentiel au solitaire '''
        self.jeu = None
        self.talon = Pile()
        self.defausse_talon = Pile()
        self.emplacement_coeur = Pile()
        self.emplacement_pique = Pile()
        self.emplacement_carreau = Pile()
        self.emplacement_trefle = Pile()
        self.defausse_1 = Pile()
        self.defausse_2 = Pile()
        self.defausse_3 = Pile()
        self.defausse_4 = Pile()

    def choisir_jeu(self):
        ''' Met en place du jeu de carte en fonction du jeu souhaité'''
        essai = True
        # Boucle qui tourne jusqu'à ce que l'utilisateur choisisse un bon jeu
        while essai is True:
            nombre_cartes = int(input("Voulez vous jouer avec un jeu de 32 ou 52 cates : "))
            if nombre_cartes == 32:
                self.jeu = JeuCarte("32")
                self.valeurs = ["As", "7", "8", "9", "10", "V", "D", "R"]
                essai = False
            elif nombre_cartes == 52:
                self.jeu = JeuCarte("52")
                self.valeurs = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R"]
                essai = False
            else :
                print(" Choisissez un jeu de carte traditionnel")
    def creer_talon(self):
        ''' Création de la pioche tout en mélangeant les cartes du jeu '''
        self.jeu.melanger_jeu()
        for carte in self.jeu.get_jeu():
            self.talon.empiler(carte)

    def tirer_carte(self):
        ''' Tire une carte du talon en la mettant face visible sur la défausse du talon'''
        # Vérification que le talon est vide
        if self.talon.etre_vide():
            while self.defausse_talon.calculer_taille() > 0:
                carte_defausse = self.defausse_talon.depiler()
                self.talon.empiler(carte_defausse)
        # Tirage de cartes
        carte_pioche = self.talon.depiler()
        self.defausse_talon.empiler(carte_pioche)
        return carte_pioche

    def creer_defausses(self):
        ''' Création de toutes les défausses en distribution classique '''
        carte_pioche = self.talon.depiler()
        self.defausse_1.empiler(carte_pioche)
        carte_pioche = self.talon.depiler()
        self.defausse_2.empiler(carte_pioche)
        carte_pioche = self.talon.depiler()
        self.defausse_3.empiler(carte_pioche)
        carte_pioche = self.talon.depiler()
        self.defausse_4.empiler(carte_pioche)
        carte_pioche = self.talon.depiler()
        self.defausse_2.empiler(carte_pioche)
        carte_pioche = self.talon.depiler()
        self.defausse_3.empiler(carte_pioche)
        carte_pioche = self.talon.depiler()
        self.defausse_4.empiler(carte_pioche)
        carte_pioche = self.talon.depiler()
        self.defausse_3.empiler(carte_pioche)
        carte_pioche = self.talon.depiler()
        self.defausse_4.empiler(carte_pioche)
        carte_pioche = self.talon.depiler()
        self.defausse_4.empiler(carte_pioche)

    def deplacement_defausse(self):
        '''
        Déplacement des cartes d'une défausse en direction de toutes
        les familles et de toutes les autres défausses
            Vérification comprise
        '''

        carte_bouge = input(" Quelle carte voulez vous bouger ? "
            "\n défausse 1 : 1   |   défausse 2 : 2   |"
            "   défausse 3 : 3   |   défausse 4 : 4\n       ")
        # Enlève la carte qui va être déplacé
        if carte_bouge == "1":
            carte = self.defausse_1.depiler()
        elif carte_bouge == "2":
            carte = self.defausse_2.depiler()
        elif carte_bouge == "3":
            carte = self.defausse_3.depiler()
        elif carte_bouge == "4":
            carte = self.defausse_4.depiler()
        else:
            return None

        if carte is not None:
            carte_acceuil = input(" Ou voulez vous la placer ? "
                "\n famille : 1   |   autre défausse : 2\n       ")
            # Déplacement en direction des familles
            if carte_acceuil == "1":
                # Déplacement vers la famille Carreau
                if carte[1] == "Carreau":
                    carte_dessous = self.emplacement_carreau.acceder_sommet()
                    if carte_dessous is None:
                        if (self.valeurs.index(carte[0])) == (self.valeurs.index("As")):
                            self.emplacement_carreau.empiler(carte)
                        if (carte_bouge == "1"
                                and (self.valeurs.index(carte[0])) != (self.valeurs.index("As"))):
                            self.defausse_1.empiler(carte)
                        elif (carte_bouge == "2"
                              and (self.valeurs.index(carte[0])) != (self.valeurs.index("As"))):
                            self.defausse_2.empiler(carte)
                        elif (carte_bouge == "3"
                              and (self.valeurs.index(carte[0])) != (self.valeurs.index("As"))):
                            self.defausse_3.empiler(carte)
                        elif (carte_bouge == "4"
                              and (self.valeurs.index(carte[0])) != (self.valeurs.index("As"))):
                            self.defausse_4.empiler(carte)
                        self.affichage()
                        return None
                    if (self.valeurs.index(carte_dessous[0])+1) == (self.valeurs.index(carte[0])):
                        self.emplacement_carreau.empiler(carte)
                    elif (self.valeurs.index(carte_dessous[0])+1) != (self.valeurs.index(carte[0])):
                        if carte_bouge == "1":
                            self.defausse_1.empiler(carte)
                        elif carte_bouge == "2":
                            self.defausse_2.empiler(carte)
                        elif carte_bouge == "3":
                            self.defausse_3.empiler(carte)
                        elif carte_bouge == "4":
                            self.defausse_4.empiler(carte)
                    self.affichage()

                # Déplacement vers la famille Trèfle
                elif carte[1] == "Trèfle":
                    carte_dessous = self.emplacement_trefle.acceder_sommet()
                    if carte_dessous is None:
                        if (self.valeurs.index(carte[0])) == (self.valeurs.index("As")):
                            self.emplacement_trefle.empiler(carte)
                        if (carte_bouge == "1"
                                and (self.valeurs.index(carte[0])) != (self.valeurs.index("As"))):
                            self.defausse_1.empiler(carte)
                        elif (carte_bouge == "2"
                              and (self.valeurs.index(carte[0])) != (self.valeurs.index("As"))):
                            self.defausse_2.empiler(carte)
                        elif (carte_bouge == "3"
                              and (self.valeurs.index(carte[0])) != (self.valeurs.index("As"))):
                            self.defausse_3.empiler(carte)
                        elif (carte_bouge == "4"
                              and (self.valeurs.index(carte[0])) != (self.valeurs.index("As"))):
                            self.defausse_4.empiler(carte)
                        self.affichage()
                        return None
                    if (self.valeurs.index(carte_dessous[0])+1) == (self.valeurs.index(carte[0])):
                        self.emplacement_trefle.empiler(carte)
                    elif (self.valeurs.index(carte_dessous[0])+1) != (self.valeurs.index(carte[0])):
                        if carte_bouge == "1":
                            self.defausse_1.empiler(carte)
                        elif carte_bouge == "2":
                            self.defausse_2.empiler(carte)
                        elif carte_bouge == "3":
                            self.defausse_3.empiler(carte)
                        elif carte_bouge == "4":
                            self.defausse_4.empiler(carte)
                    self.affichage()

                # Déplacement vers la famille Coeur
                elif carte[1] == "Coeur":
                    carte_dessous = self.emplacement_coeur.acceder_sommet()
                    if carte_dessous is None:
                        if (self.valeurs.index(carte[0])) == (self.valeurs.index("As")):
                            self.emplacement_coeur.empiler(carte)
                        if (carte_bouge == "1"
                                and (self.valeurs.index(carte[0])) != (self.valeurs.index("As"))):
                            self.defausse_1.empiler(carte)
                        elif (carte_bouge == "2"
                              and (self.valeurs.index(carte[0])) != (self.valeurs.index("As"))):
                            self.defausse_2.empiler(carte)
                        elif (carte_bouge == "3"
                              and (self.valeurs.index(carte[0])) != (self.valeurs.index("As"))):
                            self.defausse_3.empiler(carte)
                        elif (carte_bouge == "4"
                              and (self.valeurs.index(carte[0])) != (self.valeurs.index("As"))):
                            self.defausse_4.empiler(carte)
                        self.affichage()
                        return None
                    if (self.valeurs.index(carte_dessous[0])+1) == (self.valeurs.index(carte[0])):
                        self.emplacement_coeur.empiler(carte)
                    elif (self.valeurs.index(carte_dessous[0])+1) != (self.valeurs.index(carte[0])):
                        if carte_bouge == "1":
                            self.defausse_1.empiler(carte)
                        elif carte_bouge == "2":
                            self.defausse_2.empiler(carte)
                        elif carte_bouge == "3":
                            self.defausse_3.empiler(carte)
                        elif carte_bouge == "4":
                            self.defausse_4.empiler(carte)
                    self.affichage()

                # Déplacement vers la famille Pique
                elif carte[1] == "Pique":
                    carte_dessous = self.emplacement_pique.acceder_sommet()
                    if carte_dessous is None:
                        if (self.valeurs.index(carte[0])) == (self.valeurs.index("As")):
                            self.emplacement_pique.empiler(carte)
                        if (carte_bouge == "1"
                                and (self.valeurs.index(carte[0])) != (self.valeurs.index("As"))):
                            self.defausse_1.empiler(carte)
                        elif (carte_bouge == "2"
                              and (self.valeurs.index(carte[0])) != (self.valeurs.index("As"))):
                            self.defausse_2.empiler(carte)
                        elif (carte_bouge == "3"
                              and (self.valeurs.index(carte[0])) != (self.valeurs.index("As"))):
                            self.defausse_3.empiler(carte)
                        elif (carte_bouge == "4"
                              and (self.valeurs.index(carte[0])) != (self.valeurs.index("As"))):
                            self.defausse_4.empiler(carte)
                        self.affichage()
                        return None
                    if (self.valeurs.index(carte_dessous[0])+1) == (self.valeurs.index(carte[0])):
                        self.emplacement_pique.empiler(carte)
                    elif (self.valeurs.index(carte_dessous[0])+1) != (self.valeurs.index(carte[0])):
                        if carte_bouge == "1":
                            self.defausse_1.empiler(carte)
                        elif carte_bouge == "2":
                            self.defausse_2.empiler(carte)
                        elif carte_bouge == "3":
                            self.defausse_3.empiler(carte)
                        elif carte_bouge == "4":
                            self.defausse_4.empiler(carte)
                    self.affichage()

            # Déplacement en direction d'une autre défausse
            elif carte_acceuil == "2":
                carte_deplace = input(" Dans quelle défausse voulez vous la mettre ? "
                    "\n défausse 1 : 1   |   défausse 2 : 2   |"
                    "   défausse 3 : 3   |   défausse 4 : 4\n       ")

                # Déplacement en direction de la défausse 1
                if carte_deplace == "1" :
                    carte_dessous = self.defausse_1.acceder_sommet()
                    if carte_dessous is None:
                        if (self.valeurs.index(carte[0])) == (self.valeurs.index("R")):
                            self.defausse_1.empiler(carte)
                        else:
                            return None
                    elif ((self.valeurs.index(carte_dessous[0])-1) == (self.valeurs.index(carte[0]))
                            and (carte_dessous[1] == "Carreau" or carte_dessous[1] == "Coeur")
                            and (carte[1] == "Pique" or carte[1] == "Trèfle")):
                        self.defausse_1.empiler(carte)

                    elif ((self.valeurs.index(carte_dessous[0])-1) == (self.valeurs.index(carte[0]))
                          and (carte[1] == "Carreau" or carte[1] == "Coeur")
                          and (carte_dessous[1] == "Pique" or carte_dessous[1] == "Trèfle")):
                        self.defausse_1.empiler(carte)
                    else :
                        if carte_bouge == "1":
                            self.defausse_1.empiler(carte)
                        elif carte_bouge == "2":
                            self.defausse_2.empiler(carte)
                        elif carte_bouge == "3":
                            self.defausse_3.empiler(carte)
                        elif carte_bouge == "4":
                            self.defausse_4.empiler(carte)

                # Déplacement en direction de la défausse 2
                elif carte_deplace == "2" :
                    carte_dessous = self.defausse_2.acceder_sommet()
                    if carte_dessous is None:
                        if (self.valeurs.index(carte[0])) == (self.valeurs.index("R")):
                            self.defausse_2.empiler(carte)
                        else:
                            return None
                    elif ((self.valeurs.index(carte_dessous[0])-1) == (self.valeurs.index(carte[0]))
                            and (carte_dessous[1] == "Carreau" or carte_dessous[1] == "Coeur")
                            and (carte[1] == "Pique" or carte[1] == "Trèfle")):
                        self.defausse_2.empiler(carte)

                    elif ((self.valeurs.index(carte_dessous[0])-1) == (self.valeurs.index(carte[0]))
                          and (carte[1] == "Carreau" or carte[1] == "Coeur")
                          and (carte_dessous[1] == "Pique" or carte_dessous[1] == "Trèfle")):
                        self.defausse_2.empiler(carte)
                    else :
                        if carte_bouge == "1":
                            self.defausse_1.empiler(carte)
                        elif carte_bouge == "2":
                            self.defausse_2.empiler(carte)
                        elif carte_bouge == "3":
                            self.defausse_3.empiler(carte)
                        elif carte_bouge == "4":
                            self.defausse_4.empiler(carte)

                # Déplacement en direction de la défausse 3
                elif carte_deplace == "3" :
                    carte_dessous = self.defausse_3.acceder_sommet()
                    if carte_dessous is None:
                        if (self.valeurs.index(carte[0])) == (self.valeurs.index("R")):
                            self.defausse_3.empiler(carte)
                        else:
                            return None
                    elif ((self.valeurs.index(carte_dessous[0])-1) == (self.valeurs.index(carte[0]))
                            and (carte_dessous[1] == "Carreau" or carte_dessous[1] == "Coeur")
                            and (carte[1] == "Pique" or carte[1] == "Trèfle")):
                        self.defausse_3.empiler(carte)
                    elif ((self.valeurs.index(carte_dessous[0])-1) == (self.valeurs.index(carte[0]))
                          and (carte[1] == "Carreau" or carte[1] == "Coeur")
                          and (carte_dessous[1] == "Pique" or carte_dessous[1] == "Trèfle")):
                        self.defausse_3.empiler(carte)
                    else :
                        if carte_bouge == "1":
                            self.defausse_1.empiler(carte)
                        elif carte_bouge == "2":
                            self.defausse_2.empiler(carte)
                        elif carte_bouge == "3":
                            self.defausse_3.empiler(carte)
                        elif carte_bouge == "4":
                            self.defausse_4.empiler(carte)

                # Déplacement en direction de la défausse 4
                elif carte_deplace == "4" :
                    carte_dessous = self.defausse_4.acceder_sommet()
                    if carte_dessous is None:
                        if (self.valeurs.index(carte[0])) == (self.valeurs.index("R")):
                            self.defausse_4.empiler(carte)
                        else:
                            return None
                    elif ((self.valeurs.index(carte_dessous[0])-1) == (self.valeurs.index(carte[0]))
                            and (carte_dessous[1] == "Carreau" or carte_dessous[1] == "Coeur")
                            and (carte[1] == "Pique" or carte[1] == "Trèfle")):
                        self.defausse_4.empiler(carte)

                    elif ((self.valeurs.index(carte_dessous[0])-1) == (self.valeurs.index(carte[0]))
                          and (carte[1] == "Carreau" or carte[1] == "Coeur")
                          and (carte_dessous[1] == "Pique" or carte_dessous[1] == "Trèfle")):
                        self.defausse_4.empiler(carte)
                    else :
                        if carte_bouge == "1":
                            self.defausse_1.empiler(carte)
                        elif carte_bouge == "2":
                            self.defausse_2.empiler(carte)
                        elif carte_bouge == "3":
                            self.defausse_3.empiler(carte)
                        elif carte_bouge == "4":
                            self.defausse_4.empiler(carte)
                else:
                    if carte_bouge == "1":
                        self.defausse_1.empiler(carte)
                    elif carte_bouge == "2":
                        self.defausse_2.empiler(carte)
                    elif carte_bouge == "3":
                        self.defausse_3.empiler(carte)
                    elif carte_bouge == "4":
                        self.defausse_4.empiler(carte)
            else:
                if carte_bouge == "1":
                    self.defausse_1.empiler(carte)
                elif carte_bouge == "2":
                    self.defausse_2.empiler(carte)
                elif carte_bouge == "3":
                    self.defausse_3.empiler(carte)
                elif carte_bouge == "4":
                    self.defausse_4.empiler(carte)
        self.affichage()

    def deplacement_talon(self):
        ''' Déplacement des cartes de la défausse du talon en direction de
         toutes les familles et de toutes les défausses
            Vérification comprise
        '''
        carte_bouge = input(" Ou voulez vous mettre la carte du talon ?"
                            "\n défausse 1 : 1   |   défausse 2 : 2   |   défausse 3 : 3   |"
                            "   défausse 4 : 4   |   emplacements familles : 5\n       ")
        carte = self.defausse_talon.acceder_sommet()

        if carte is not None:
            # Déplacement en direction de la défausse 1
            if carte_bouge == "1" :
                carte_dessous = self.defausse_1.acceder_sommet()
                self.defausse_talon.depiler()
                if (carte_dessous is None and carte[0] == "R"):
                    self.defausse_1.empiler(carte)
                elif (carte_dessous is None and carte[0] != "R"):
                    self.defausse_talon.empiler(carte)
                elif ((self.valeurs.index(carte_dessous[0])-1) == (self.valeurs.index(carte[0]))
                        and (carte_dessous[1] == "Carreau" or carte_dessous[1] == "Coeur")
                        and (carte[1] == "Pique" or carte[1] == "Trèfle")):
                    self.defausse_1.empiler(carte)
                elif ((self.valeurs.index(carte_dessous[0])-1) == (self.valeurs.index(carte[0]))
                      and (carte[1] == "Carreau" or carte[1] == "Coeur")
                      and (carte_dessous[1] == "Pique" or carte_dessous[1] == "Trèfle")):
                    self.defausse_1.empiler(carte)
                else :
                    self.defausse_talon.empiler(carte)

            # Déplacement en direction de la défausse 2
            if carte_bouge == "2" :
                carte_dessous = self.defausse_2.acceder_sommet()
                self.defausse_talon.depiler()
                if (carte_dessous is None and carte[0] == "R"):
                    self.defausse_2.empiler(carte)
                elif (carte_dessous is None and carte[0] != "R"):
                    self.defausse_talon.empiler(carte)
                elif ((self.valeurs.index(carte_dessous[0])-1) == (self.valeurs.index(carte[0]))
                        and (carte_dessous[1] == "Carreau" or carte_dessous[1] == "Coeur")
                        and (carte[1] == "Pique" or carte[1] == "Trèfle")):
                    self.defausse_2.empiler(carte)
                elif ((self.valeurs.index(carte_dessous[0])-1) == (self.valeurs.index(carte[0]))
                      and (carte[1] == "Carreau" or carte[1] == "Coeur")
                      and (carte_dessous[1] == "Pique" or carte_dessous[1] == "Trèfle")):
                    self.defausse_2.empiler(carte)
                else :
                    self.defausse_talon.empiler(carte)

            # Déplacement en direction de la défausse 3
            if carte_bouge == "3" :
                carte_dessous = self.defausse_3.acceder_sommet()
                self.defausse_talon.depiler()
                if (carte_dessous is None and carte[0] == "R"):
                    self.defausse_3.empiler(carte)
                elif (carte_dessous is None and carte[0] != "R"):
                    self.defausse_talon.empiler(carte)
                elif ((self.valeurs.index(carte_dessous[0])-1) == (self.valeurs.index(carte[0]))
                        and (carte_dessous[1] == "Carreau" or carte_dessous[1] == "Coeur")
                        and (carte[1] == "Pique" or carte[1] == "Trèfle")):
                    self.defausse_3.empiler(carte)
                elif ((self.valeurs.index(carte_dessous[0])-1) == (self.valeurs.index(carte[0]))
                      and (carte[1] == "Carreau" or carte[1] == "Coeur")
                      and (carte_dessous[1] == "Pique" or carte_dessous[1] == "Trèfle")):
                    self.defausse_3.empiler(carte)
                else :
                    self.defausse_talon.empiler(carte)

            # Déplacement en direction de la défausse 4
            if carte_bouge == "4" :
                carte_dessous = self.defausse_4.acceder_sommet()
                self.defausse_talon.depiler()
                if (carte_dessous is None and carte[0] == "R"):
                    self.defausse_4.empiler(carte)
                elif (carte_dessous is None and carte[0] != "R"):
                    self.defausse_talon.empiler(carte)
                elif ((self.valeurs.index(carte_dessous[0])-1) == (self.valeurs.index(carte[0]))
                        and (carte_dessous[1] == "Carreau" or carte_dessous[1] == "Coeur")
                        and (carte[1] == "Pique" or carte[1] == "Trèfle")):
                    self.defausse_4.empiler(carte)
                elif ((self.valeurs.index(carte_dessous[0])-1) == (self.valeurs.index(carte[0]))
                      and (carte[1] == "Carreau" or carte[1] == "Coeur")
                      and (carte_dessous[1] == "Pique" or carte_dessous[1] == "Trèfle")):
                    self.defausse_4.empiler(carte)
                else :
                    self.defausse_talon.empiler(carte)

            # Déplacement en direction des familles
            if carte_bouge == "5" :
                if carte[1] == "Carreau":
                    carte_dessous = self.emplacement_carreau.acceder_sommet()
                    if carte_dessous is None:
                        if (self.valeurs.index(carte[0])) == (self.valeurs.index("As")):
                            self.emplacement_carreau.empiler(self.defausse_talon.depiler())
                        self.affichage()
                    elif (self.valeurs.index(carte_dessous[0])+1) == (self.valeurs.index(carte[0])):
                        self.emplacement_carreau.empiler(self.defausse_talon.depiler())
                elif carte[1] == "Trèfle":
                    carte_dessous = self.emplacement_trefle.acceder_sommet()
                    if carte_dessous is None:
                        if (self.valeurs.index(carte[0])) == (self.valeurs.index("As")):
                            self.emplacement_trefle.empiler(self.defausse_talon.depiler())
                        self.affichage()
                    elif (self.valeurs.index(carte_dessous[0])+1) == (self.valeurs.index(carte[0])):
                        self.emplacement_trefle.empiler(self.defausse_talon.depiler())
                elif carte[1] == "Coeur":
                    carte_dessous = self.emplacement_coeur.acceder_sommet()
                    if carte_dessous is None:
                        if (self.valeurs.index(carte[0])) == (self.valeurs.index("As")):
                            self.emplacement_coeur.empiler(self.defausse_talon.depiler())
                        self.affichage()
                    elif (self.valeurs.index(carte_dessous[0])+1) == (self.valeurs.index(carte[0])):
                        self.emplacement_coeur.empiler(self.defausse_talon.depiler())
                elif carte[1] == "Pique":
                    carte_dessous = self.emplacement_pique.acceder_sommet()
                    if carte_dessous is None:
                        if (self.valeurs.index(carte[0])) == (self.valeurs.index("As")):
                            self.emplacement_pique.empiler(self.defausse_talon.depiler())
                        self.affichage()
                    elif (self.valeurs.index(carte_dessous[0])+1) == (self.valeurs.index(carte[0])):
                        self.emplacement_pique.empiler(self.defausse_talon.depiler())
                self.affichage()
        self.affichage()

    def affichage(self):
        ''' Affiche tout le jeu que ce soit:
                - Talon et sa défausse
                - Autres défausses
                - Familles
        '''
        defausse_talon = self.defausse_talon.acceder_sommet()
        print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n"
        "\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n"
        "\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
        print("       🎴                                  ♠️               "
            "    ♥️                   ♦️                   ♣️")
        print("(Talon) ", defausse_talon, "             ",
            solitaire.emplacement_pique.acceder_sommet(), "   ",
            solitaire.emplacement_coeur.acceder_sommet(), "   ",
            solitaire.emplacement_carreau.acceder_sommet(), "   ",
            solitaire.emplacement_trefle.acceder_sommet(), "   ")
        print()
        print()

        print("        ", solitaire.defausse_1.calculer_taille(), "​🃏​               ",
            solitaire.defausse_2.calculer_taille(), "​🃏​               ",
            solitaire.defausse_3.calculer_taille(), "​🃏​                ",
            solitaire.defausse_4.calculer_taille(), "​🃏​                ")
        print("        ", solitaire.defausse_1.acceder_sommet(), "   ",
            solitaire.defausse_2.acceder_sommet(), "   ",
            solitaire.defausse_3.acceder_sommet(), "   ",
            solitaire.defausse_4.acceder_sommet(), "   ",)
        print(" \n \n")

    def finir_jeu(self):
        ''' Donne la fin du jeu si tous les Rois sont dans leurs emplacements
         familles respectives '''
        carte_fin1 = self.emplacement_carreau.acceder_sommet()
        carte_fin2 = self.emplacement_coeur.acceder_sommet()
        carte_fin3 = self.emplacement_trefle.acceder_sommet()
        carte_fin4 = self.emplacement_pique.acceder_sommet()
        if (carte_fin1 is not None and carte_fin2 is not None
                and carte_fin3 is not None and carte_fin4 is not None):
            if (carte_fin1[0] == "R" and carte_fin2[0] == "R"
                    and carte_fin3[0] == "R" and carte_fin4[0] == "R"):
                return True
            return False

    def saisie(self):
        ''' Boucle du jeu qui pose les questions afin de faire les actions '''
        demande = ""
        compteur_t = 0

        while demande != "x":
            demande = input("Quelle action voulez vous faire ?"
                            "\n t : retourner une carte du talon"
                            "\n d : effectuer un déplacement"
                            "\n x : abandonner la partie \n      ")
            if self.finir_jeu() is True:
                print(" Vous avez gagné la partie")
                print(" Vous avez tourné",compteur_t,"fois les cartes du talon")
                print(" Appuyez sur 'x' pour terminer le jeu et relancer une nouvelle partie")
            if demande == "t":
                compteur_t += 1
                print("\n \n \n")
                defausse_talon = self.tirer_carte()
                self.affichage()
                if self.defausse_talon is None:
                    return None

            elif demande == "d":
                deplacement = input(" Quelle carte voulez vous déplacer ?"
                                    "\n p : pioche      |      d : défausses \n      ")
                if deplacement == "d":
                    self.deplacement_defausse()
                elif deplacement == "p":
                    self.deplacement_talon()

        print(" _______________________")
        print(" Vous avez arreté le jeu")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        return None

    def lancement(self):
        ''' Lancement de toutes les méthodes afin de faire tourner le jeu '''
        print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n"
        "\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n"
        "\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
        solitaire.choisir_jeu()
        solitaire.creer_talon()
        solitaire.creer_defausses()
        solitaire.affichage()
        solitaire.saisie()

if __name__ == "__main__" :
    ''' Programme Main'''
    solitaire = Solitaire()
    solitaire.lancement()