import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QLabel, QStatusBar, QPushButton, QMenuBar
from PySide6.QtGui import QAction, QKeySequence, QIcon


class FenetrePrincipale(QMainWindow):
    def __init__(self):
        super().__init__()
        # Créer un label qui aura comme texte "texte"
        label_texte = QLabel("texte")

        # Le QMainWindow contient un widget central qui peut contenir d'autres widgets
        # avec un widget sans disposition (layout) le widget central prendra toute la place
        self.setCentralWidget(label_texte)

        # Initialise un QMenuBar directement à partir du QMainWindow
        barre_menus = self.menuBar()
        # On aurait pu aussi créer un QMenuBar et faire un setMenuBar sur le QMainWindow
        # barre_menus = QMenuBar()
        # self.setMenuBar(barre_menus)

        # Appelle la méthode creer_menus pour ajouter des menus à la barre
        self.creer_menus(barre_menus)
        # Créer un icône avec l'image "jouer.png", le path est relatif dans ce cas-ci = "./jouer.png"
        icone = QIcon("jouer.png")
        # Créer un bouton avec le texte "Test" et l'icône icone
        bouton_test = QPushButton("Test")
        bouton_test.setIcon(icone)
        # Connecte l'événement pressed du bouton à la méthode action_executee
        bouton_test.pressed.connect(self.action_executee)

        # Créer une barre d'outils
        barre_outils = QToolBar("Barre d'outils")
        # Grosseur des icônes dans la barre d'outils
        barre_outils.setIconSize(QSize(16, 16))
        barre_outils.addWidget(bouton_test)
        # Ajoute la barre d'outils à la fenêtre (QMainWindow)
        self.addToolBar(barre_outils)

        # Créer une deuxième barre d'outils
        barre_outils_2 = QToolBar("Barre d'outils 2")
        barre_outils_2.setIconSize(QSize(16, 16))
        bouton_outils = QPushButton("Outils")
        bouton_outils.pressed.connect(self.action_executee)
        barre_outils_2.addWidget(bouton_outils)
        self.addToolBar(barre_outils_2)

        # Créer une barre de statut
        self.barre_statut = QStatusBar(self)
        # Affiche un conseil dans la barre de statut
        self.barre_statut.setStatusTip("cliquer un bouton")
        self.setStatusBar(self.barre_statut)

        # Nom de la fenêtre principale
        self.setWindowTitle("Exemple QMainWindow")

    # Méthode pour créer les menus
    # Un QMenu est ajouté à une QMenuBar
    # On ajoute des QAction à un QMenu
    def creer_menus(self, barre_menus):
        menu_fichier = barre_menus.addMenu("&Fichier")
        action_test = QAction(text="Test!", parent=self)
        action_test.setStatusTip("Cliquez pour un test")
        action_test.triggered.connect(self.action_executee)
        menu_fichier.addAction(action_test)

        menu_quitter = barre_menus.addMenu("&Quitter")
        action_quitter = QAction(text="Quitter", parent=self)
        action_quitter.triggered.connect(self.close)
        action_quitter.setShortcut(QKeySequence("Ctrl+Q"))
        menu_quitter.addAction(action_quitter)

    def action_executee(self):
        print("click!!!")
        self.barre_statut.setStatusTip("click!!!!!!!")


app = QApplication(sys.argv)
f = FenetrePrincipale()
f.show()
app.exec()
