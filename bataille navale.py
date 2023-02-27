import pprint  

class rentreededonnees: #partie entrée de données 

    def __init__(self):
        self.coordonnées = [[0]*10 for i in range(10)] #un tableau a deux dimensions qui fait 10*10 et rempli de "0"


    def validité(self, ligne, colonne):#on vérifie qu'il n'y a pas déja de bateau a l'emplacement choisi par le joueur 
        if self.coordonnées[ligne][colonne] == 1:
            print("il y a deja un bateau ici, c'est discutable strategiquement parlant de faire rentrer un bateau dans un autre, met le ailleur")
            return False
        else:
            return True


    def saisie(self, taille):
        houv = None # "H" pour horizontal ou "V" pour vertical
        ligne = -1 # Valeur d'initialisation, c'est la coordonnée X de la ou tu vas placer ton bateau 
        colonne = -1#Valeur d'initialisation, c'est la coordonnée Y de la ou tu vas placer ton bateau 
        while houv != "h" and houv != "v":# tant que l'utilisateur n'écrit pas soit un "H" soit un "V"
            houv = input("Ton bateau est-il à l'horizontale ou à la verticale ? (rentre h ou v), sa taille est de {}\n".format(taille))

        if houv == "h":#le joueur a choisi que son bateau soit a la verticale 

            while ligne < 0 or ligne >10: #tant que l'utilisateur ne choisis pas une ligne valide
                ligne = int(input("Quelle ligne pour ton bateau (il a une taille de {}) ?\n".format(taille)))

            while colonne < 0 or colonne + taille > 10: #tant que lutilisateur ne choisis pas une colonne valide 
                colonne = int(input("À partir de quelle colonne tu le places ? (Il remplira {} cases vers la droite à partir de celle-ci)\n".format(taille)))

            for i in range(taille):# on vérifie qu'il y a pas déja un bateau a cet emplacement

                if not self.validité(ligne-1, colonne-1+i):
                    return self.saisie(taille)
                self.coordonnées[ligne-1][colonne-1+i] = 1

        else: #le joueur a placé son bateau a l'horizontale 

            while colonne < 0 or colonne > 10 : #tant que l'utilisateur ne choisis pas une colonne valide 
                colonne = int(input("Quelle colonne pour ton bateau (il a une taille de {}) ?\n".format(taille)))

            while ligne <0 or ligne + taille >10: #tant que l'utilisateur ne choisis pas une ligne valide 
                ligne = int(input("À partir de quelle ligne tu le places ? (Il remplira {} cases vers le bas à partir de celle-ci)\n".format(taille)))

            for i in range(taille):

                if not self.validité(ligne+i-1, colonne-1):
                    return self.saisie(taille)
                self.coordonnées[ligne+i-1][colonne-1] = 1


class jeu:

    def __init__(self) :
        self.essais = [["~"]*10 for i in range(10)]# on crée un tableau de 10*"~" par 10* "~",l'idée c'est de signifier on n'a pas tiré a cet emplacement 




    def tour(self,grilledefenseur):# tour de j1 ou tour de j2
        colonne = -1#valeur d'initalissation
        ligne = -1#valeur d'initalisation 
        while colonne < 0 or colonne > 10 :
            colonne = int(input("a quelle colonne tu vas frapper ?"))

        while ligne < 0 or colonne > 10 :
            ligne = int(input("a quelle ligne vas tu frapper ?"))

        if grilledefenseur[ligne-1][colonne-1]==1:

            print("kaboom tu l'as eu !")
            self.essais[ligne-1][colonne-1] = "O"

        else :

            print("ploof")
            self.essais[ligne-1][colonne-1] = "X"
        pprint.pprint(self.essais)
        
        
        



grillej1 = rentreededonnees() # on crée la grille du joueur 1

grillej1.saisie(5)#on place un bateau de 5 cases de long sur la grille 
pprint.pprint(grillej1.coordonnées)

grillej1.saisie(4)#pareil mais 4 cases 
pprint.pprint(grillej1.coordonnées)

grillej1.saisie(4)#
pprint.pprint(grillej1.coordonnées)

grillej1.saisie(3)#pareil mais 3 cases 
pprint.pprint(grillej1.coordonnées)

grillej1.saisie(2)#pareil mais 2 cases
pprint.pprint(grillej1.coordonnées)



grillej2 = rentreededonnees()#on crée la grille du joueur 2 

grillej2.saisie(5)
pprint.pprint(grillej2.coordonnées)

grillej2.saisie(4)
pprint.pprint(grillej2.coordonnées)

grillej2.saisie(4)
pprint.pprint(grillej2.coordonnées)

grillej2.saisie(3)
pprint.pprint(grillej2.coordonnées)

grillej2.saisie(2)
pprint.pprint(grillej2.coordonnées)

tourj1 = jeu()
tourj2 = jeu()
partie = True

while partie == True :# tant qu'une des grilles n'a pas 18 "0" (c'est ce qui s'affiche quand un bateau est touché)

    print("au tour de j1")
    tourj1.tour(grillej2.coordonnées)

    if sum(ligne.count("O") for ligne in grillej2.coordonnées) == 18:

        print("Tous les bateaux de j2 ont été touchés ! j1 a gagné !")
        partie = False



    print("au tour de j2")
    tourj2.tour(grillej1.coordonnées)

    if sum(ligne.count("O") for ligne in grillej1.coordonnées) == 18:

        print("Tous les bateaux de j1 ont été touchés ! j2 a gagné !")
        partie = False