from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, \
    QCheckBox, QComboBox


class FenetreEtWidgets(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fenêtre et widgets")

        # Création d'un libellé
        self.label = QLabel("Étiquette")
        # Création d'un bouton
        self.bouton = QPushButton("Cliquez ici")
        # Connexion du signal "clicked" du bouton à la méthode afficher_message
        # Remarquez que la méthode n'a pas de parenthèses, on ne l'appelle pas, on la passe en paramètre
        self.bouton.clicked.connect(self.afficher_message)

        # La disposition des widgets est gérée par un layout, celui-ci les positionne de manière automatique
        # verticalement
        disposition_verticale = QVBoxLayout()
        disposition_verticale.addWidget(self.label)
        disposition_verticale.addWidget(self.bouton)

        # Création d'un layout horizontal
        disposition_horizontale = QHBoxLayout()
        self.case_a_cocher = QCheckBox("Case à cocher")
        # Connexion du signal "clicked" de la case à cocher à la méthode afficher_si_coche
        self.case_a_cocher.clicked.connect(self.afficher_si_coche)
        disposition_horizontale.addWidget(self.case_a_cocher)
        # Création d'une liste déroulante
        self.liste_deroulante = QComboBox()
        self.liste_deroulante.addItem("Premier élément")
        self.liste_deroulante.addItem("Deuxième élément")
        disposition_horizontale.addWidget(self.liste_deroulante)
        # Ajoute le layout vertical dans le layout horizontal
        disposition_horizontale.addLayout(disposition_verticale)

        # Création d'un bouton avec une icône
        bouton_icone = QPushButton("Bouton avec icône")
        bouton_icone.setIcon(QIcon("poisson.png"))
        disposition_horizontale.addWidget(bouton_icone)

        # Création d'un widget pour contenir les autres widgets
        widget = QWidget()
        widget.setLayout(disposition_horizontale)

        # Un QMainWindow possède un widget central, on peut y placer notre widget contenant les autres widgets
        # QMainWindow comprend plusieurs autres emplacements prédéfinis pour les widgets (central_widget, menu_bar,
        # status_bar, etc.)
        self.setCentralWidget(widget)

        # Création d'un menu
        menu = self.menuBar().addMenu("Menu")
        quitter_action = menu.addAction("Quitter")
        quitter_action.triggered.connect(self.close)

    # méthode qui sera appelée lorsqu'on cliquera sur le bouton
    def afficher_message(self):
        self.label.setText("Bonjour, le monde !")

    def afficher_si_coche(self):
        if self.case_a_cocher.isChecked():
            self.statusBar().showMessage("Case cochée")
        else:
            self.statusBar().showMessage("Case non cochée")


if __name__ == "__main__":
    app = QApplication([])
    fenetre = FenetreEtWidgets()
    fenetre.show()
    app.exec()