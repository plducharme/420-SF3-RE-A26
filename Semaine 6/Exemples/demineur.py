from PySide6.QtWidgets import QApplication, QFrame, QHBoxLayout, QGridLayout, QPushButton, QLabel, QVBoxLayout, \
    QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import random


class Demineur(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Démineur 2025")

        # Modèle
        self.largeur_jeu = 16
        self.hauteur_jeu = 16
        self.nombre_mines = 32
        self.jeu = DemineurJeu(self.largeur_jeu, self.hauteur_jeu, self.nombre_mines)

        self.disposition_principale = QVBoxLayout()
        self.setLayout(self.disposition_principale)

        self.disposition_score = QHBoxLayout()
        self.libelle_score = QLabel("Score:")
        self.libelle_total_score = QLabel("0")
        self.disposition_score.addWidget(self.libelle_score)
        self.disposition_score.addWidget(self.libelle_total_score)
        self.disposition_principale.addLayout(self.disposition_score)

        self.disposition_jeu = QGridLayout()
        self.disposition_jeu.setSpacing(0)

        for i in range(self.jeu.hauteur):
            for j in range(self.jeu.largeur):
                case_demineur: QPushButton = QPushButton()
                case_demineur.setObjectName(f"case_{i}_{j}")
                case_demineur.clicked.connect(self.case_clicked)
                case_demineur.setMinimumSize(32, 32)
                case_demineur.setMaximumSize(32, 32)
                self.disposition_jeu.addWidget(case_demineur, i, j)

        self.disposition_principale.addLayout(self.disposition_jeu)

    def case_clicked(self):
        case_cliquee: QPushButton = self.sender()
        nom_case = case_cliquee.objectName()
        # Les cases sont nommés case_idxligne_idxcolonne
        case_split = nom_case.split("_")
        ligne = int(case_split[1])
        colonne = int(case_split[2])

        if self.jeu.tableau_jeu[ligne][colonne] != DemineurJeu.CASE_MINE:
            case_cliquee.setText(str(self.jeu.tableau_jeu[ligne][colonne]))
            case_cliquee.setEnabled(False)
            self.jeu.cases_decouvertes += 1
            self.decouvrir_voisines(ligne, colonne)

            if self.jeu.verifier_gagnant():
                QMessageBox.information(self, "Bravo!", "Vous avez gagné")
                self.jeu = DemineurJeu(self.largeur_jeu, self.hauteur_jeu, self.nombre_mines)
        # Cliquer une mine
        else:
            case_cliquee.setText("X")
            QMessageBox.critical(self, "Partie Perdu", "Vous avez sauté!\nMeilleure chance la prochaine fois!")
            self.close()

    def decouvrir_voisines(self, ligne, colonne):
        # Générer liste de tuples des cases avoisinantes en excluant la case elle-même pour vérifier si on doit
        # découvrir des "0"
        voisines = [
            (r, c)
            for r in range(ligne - 1, ligne + 2)
            for c in range(colonne - 1, colonne + 2)
            if (r, c) != (ligne, colonne)
            and 0 <= ligne <= self.jeu.hauteur - 1 and 0 <= colonne <= self.jeu.largeur - 1
        ]

        for v in voisines:
            print(v[0], v[1])
            c = v[1]
            r = v[0]
            # Cette case est à 0
            if self.jeu.tableau_jeu[r][c] == 0 and 0 <= r <= self.jeu.hauteur-1 and 0 <= c <= self.jeu.largeur-1:
                case = self.findChild(QPushButton, f"case_{r}_{c}")
                if case.isEnabled():
                    case.setText("0")
                    case.setEnabled(False)
                    self.jeu.cases_decouvertes += 1
                    # FIXME: BUG out of range dans la récursion même si les bornes sont vérifiés
                    # self.decouvrir_voisines(r, c)


class DemineurJeu:
    CASE_MINE = 9

    def __init__(self, largeur: int = 16, hauteur: int = 16, nombre_mines: int = 32):
        self.__largeur: int = largeur
        self.__hauteur: int = hauteur
        self.__nombre_mines: int = nombre_mines
        self.__tableau_jeu = []
        self.__mines_trouvees: int = 0
        self.__cases_decouvertes: int = 0
        self.creer_jeu()

    @property
    def largeur(self):
        return self.__largeur

    @largeur.setter
    def largeur(self, largeur):
        self.__largeur = largeur

    @property
    def hauteur(self):
        return self.__hauteur

    @hauteur.setter
    def hauteur(self, hauteur):
        self.__hauteur = hauteur

    @property
    def nombre_mines(self):
        return self.__nombre_mines

    @nombre_mines.setter
    def nombre_mines(self, nombre_mines):
        self.nombre_mines = nombre_mines

    @property
    def tableau_jeu(self):
        return self.__tableau_jeu

    @tableau_jeu.setter
    def tableau_jeu(self, tableau_jeu):
        self.__tableau_jeu = tableau_jeu

    @property
    def mines_trouvees(self):
        return self.__mines_trouvees

    @mines_trouvees.setter
    def mines_trouvees(self, mine_trouvees):
        self.__mines_trouvees = mine_trouvees

    @property
    def cases_decouvertes(self):
        return self.__cases_decouvertes

    @cases_decouvertes.setter
    def cases_decouvertes(self, nombre: int):
        self.__cases_decouvertes = nombre


    def creer_jeu(self):

        for i in range(self.hauteur):
            ligne = []
            for j in range(self.largeur):
                ligne.append(0)
            self.__tableau_jeu.append(ligne)

        mine_a_placer = self.nombre_mines

        while mine_a_placer > 0:
            ligne = random.randint(0, self.hauteur - 1)
            colonne = random.randint(0, self.largeur - 1)

            if self.__tableau_jeu[ligne][colonne] == 0:
                self.__tableau_jeu[ligne][colonne] = DemineurJeu.CASE_MINE
                mine_a_placer -= 1

                # Générer liste de tuples des cases avoisinantes en excluant la case elle-même
                voisines = [
                    (r, c)
                    for r in range(ligne - 1, ligne + 2)
                    for c in range(colonne - 1, colonne + 2)
                    if (r, c) != (ligne, colonne)
                ]

                # mettre à jour le nombre sur les cases voisines de la mine
                for v in voisines:
                    self.mise_a_jour_case_voisine(v[0], v[1])
            else:
                continue
        self.__tableau_jeu = self.__tableau_jeu

    def mise_a_jour_case_voisine(self, ligne, colonne):
        if 0 <= ligne <= self.hauteur-1 and 0 <= colonne <= self.largeur-1:
            if self.tableau_jeu[ligne][colonne] != DemineurJeu.CASE_MINE:
                self.tableau_jeu[ligne][colonne] += 1

    def verifier_gagnant(self):
        if self.cases_decouvertes == self.largeur * self.hauteur - self.nombre_mines:
            return True
        return False


app = QApplication()
demineur = Demineur()
demineur.show()
app.exec()
