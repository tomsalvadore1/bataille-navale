import pprint 

class rentreededonnees:
    def __init__(self):
        self.coordonnées = [[0]*10 for i in range(10)]

    def validité(self, ligne, colonne):
        if self.coordonnées[ligne][colonne] == 1:
            print("il y a deja un bateau ici, c'est discutable strategiquement parlant de faire rentrer un bateau dans un autre, met le ailleur")
            return False
        else:
            return True

    def saisie(self, taille):
        houv = None
        ligne = -1
        colonne = -1
        while houv != "h" and houv != "v":
            houv = input("Ton bateau est-il à l'horizontale ou à la verticale ? (rentre h ou v), sa taille est de {}\n".format(taille))
        if houv == "h":
            while ligne < 0 or ligne >10:
                ligne = int(input("Quelle ligne pour ton bateau (il a une taille de {}) ?\n".format(taille)))
            while colonne < 0 or colonne + taille > 10:
                colonne = int(input("À partir de quelle colonne tu le places ? (Il remplira {} cases vers la droite à partir de celle-ci)\n".format(taille)))
            for i in range(taille):
                if not self.validité(ligne-1, colonne-1+i):
                    return self.saisie(taille)
                self.coordonnées[ligne-1][colonne-1+i] = 1
        else:
            while colonne < 0 or colonne > 10 :
                colonne = int(input("Quelle colonne pour ton bateau (il a une taille de {}) ?\n".format(taille)))
            while ligne <0 or ligne + taille >10:
                ligne = int(input("À partir de quelle ligne tu le places ? (Il remplira {} cases vers le bas à partir de celle-ci)\n".format(taille)))
            for i in range(taille):
                if not self.validité(ligne+i-1, colonne-1):
                    return self.saisie(taille)
                self.coordonnées[ligne+i-1][colonne-1] = 1


class jeu:
    def __init__(self) :
        self.essais = [["~"]*10 for i in range(10)]
    def tour(self,grilledefenseur):
        colonne = -1
        ligne = -1
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
        
        
        



grillej1 = rentreededonnees()
grillej1.saisie(5)
pprint.pprint(grillej1.coordonnées)
"""grillej1.saisie(4)
pprint.pprint(grillej1.coordonnées)
grillej1.saisie(4)
pprint.pprint(grillej1.coordonnées)
grillej1.saisie(3)
pprint.pprint(grillej1.coordonnées)
grillej1.saisie(2)
pprint.pprint(grillej1.coordonnées)"""



grillej2 = rentreededonnees()
grillej2.saisie(5)
pprint.pprint(grillej2.coordonnées)
"""grillej2.saisie(4)
pprint.pprint(grillej2.coordonnées)
grillej2.saisie(4)
pprint.pprint(grillej2.coordonnées)
grillej2.saisie(3)
pprint.pprint(grillej2.coordonnées)
grillej2.saisie(2)
pprint.pprint(grillej2.coordonnées)"""
tourj1 = jeu()
tourj2 = jeu()

while True:
    print("au tour de j1")
    tourj1.tour(grillej2.coordonnées)
    if sum(ligne.count("O") for ligne in grillej2.coordonnées) == 5:
        print("Tous les bateaux de j2 ont été touchés ! j1 a gagné !")
        break

    print("au tour de j2")
    tourj2.tour(grillej1.coordonnées)
    if sum(ligne.count("O") for ligne in grillej1.coordonnées) == 5:
        print("Tous les bateaux de j1 ont été touchés ! j2 a gagné !")
        break