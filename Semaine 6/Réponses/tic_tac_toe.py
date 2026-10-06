from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QGridLayout, \
    QApplication, QDialog
from collections import deque

class TicTacToe(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")

        widget_central = QWidget()
        disposition_jeu = QGridLayout()
        widget_central.setLayout(disposition_jeu)
        self.setCentralWidget(widget_central)

        # boucles pour créer les boutons (de façon dynamique, aurait pu êtr fait manuellement)
        for ligne in range(3):
            for colonne in range(3):
                bouton = QPushButton()
                bouton.setObjectName(f"bouton_{ligne}_{colonne}")
                disposition_jeu.addWidget(bouton, ligne, colonne)
                bouton.clicked.connect(self.bouton_clicked)

        self.jeu = TicTacToeJeu()

    # lorsqu'un des boutons est cliqué, cette méthode est appelée
    def bouton_clicked(self):
        # On va chercher le bouton qui a été cliqué
        bouton = self.sender()
        nom_bouton = bouton.objectName()

        # extraire les coordonnées du bouton
        ligne, colonne = nom_bouton.split("_")[1:]
        idx_ligne = int(ligne)
        idx_colonne = int(colonne)

        bouton.setEnabled(False)
        bouton.setText(self.jeu.joueur_courant.pion)
        self.jeu.tableau_jeu[idx_colonne][idx_ligne] = self.jeu.joueur_courant.pion

        resultat = self.jeu.verifier_etat_jeu(idx_colonne, idx_ligne, self.jeu.joueur_courant.pion)
        if resultat is None:
            return
        elif resultat == "nul":
            dialog = QDialog(self)
            dialog.setWindowTitle("Fin de la partie")
            dialog_layout = QVBoxLayout()
            dialog_layout.addWidget(QLabel("Match nul"))
            dialog.setLayout(dialog_layout)
            dialog.exec()
        else:
            dialog = QDialog(self)
            dialog.setWindowTitle("Fin de la partie")
            dialog_layout = QVBoxLayout()
            dialog_layout.addWidget(QLabel(f"{resultat} a gagné"))
            dialog.setLayout(dialog_layout)
            dialog.exec()


# Modèle représentant un joueur
class Joueur:
    def __init__(self, nom: str, pion: str):
        self.nom = nom
        self.pion = pion


# Modèle représentant le jeu Tic Tac Toe
class TicTacToeJeu:

    def __init__(self):

        self.tableau_jeu = [[None, None, None],
                       [None, None, None],
                       [None, None, None]]

        # utiliser deque pour alterner entre les joueurs
        self.joueurs = deque([Joueur("Alice", "X"), Joueur("Bob", "O")])
        self.joueur_courant = self.joueurs[0]
        self.nb_coups = 0

    # Méthode pour vérifier s'il y a un gagnant
    # retourne le nom du joueur gagnant, None s'il n'y a pas de gagnant ou "nul" s'il y a égalité
    def verifier_etat_jeu(self, colonne, ligne, coup):
        # vérifie si la colonne est gagnante
        for j in range(0, 3):
            if self.tableau_jeu[colonne][j] != coup:
                break
            if j == 2:
                return self.joueur_courant.nom

        # vérifie si la ligne est gagnante
        for i in range(0, 3):
            if self.tableau_jeu[i][ligne] != coup:
                break
            if i == 2:
                return self.joueur_courant.nom

        # Vérifie la première diagonale
        if ligne == colonne:
            for i in range(0, 3):
                if self.tableau_jeu[i][i] != coup:
                    break
                if i == 2:
                    return self.joueur_courant.nom

        # Vérifie la deuxième diagonale
        if colonne + ligne == 2:
            for i in range(0, 3):
                if self.tableau_jeu[i][2 - i] != coup:
                    break
                if i == 2:
                    return self.joueur_courant.nom
        # Si 9 coups ont été joués, c'est un match nul
        if self.nb_coups == 9:
            return "nul"

        # Si aucun gagnant n'a été trouvé, on alterne les joueurs
        self.joueurs.rotate()
        self.joueur_courant = self.joueurs[0]
        return None


app = QApplication()
window = TicTacToe()
window.show()
app.exec()
