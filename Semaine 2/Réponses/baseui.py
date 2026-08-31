from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QToolBar, QMenu, QStatusBar,
                               QMenuBar, QPushButton)
from PySide6.QtGui import QAction, QIcon, QPixmap


class BaseUI(QMainWindow):

    def __init__(self):
        super().__init__()
        # Titre de la fenêtre
        self.setWindowTitle("Mon application")

        # Création de la barre de menu par défaut, il est possible à la place d'initialiser son propre QMenuBar et de
        # l'assigner :
        # self.barre_menu = QMenuBar()
        # self.setMenuBar(self.barre_menu)
        self.barre_menu = self.menuBar()
        # Création des QMenu
        # L'éperluette (&) permet de définir un raccourci clavier pour le menu
        # Il n'apparait pas dans le menu par défaut, mais peut être affiché en appuyant sur la touche Alt
        self.menu1 = QMenu("&Menu1")
        # Création des QAction qui sont ajoutées aux QMenu
        self.action_menu1 = QAction("Item Menu1")
        self.menu1.addAction(self.action_menu1)
        self.menu1.triggered.connect(self.afficher_message_menu1)
        self.menu2 = QMenu("M&enu2")
        self.action_menu2 = QAction("Item Menu2")
        self.action_menu2.triggered.connect(self.afficher_message_menu2)
        self.menu2.addAction(self.action_menu2)
        # ajout des QMenu à la barre de menu
        self.barre_menu.addMenu(self.menu1)
        self.barre_menu.addMenu(self.menu2)
        # ajout d'une barre d'outils
        self.barre_outils = QToolBar()
        bouton_outils = QPushButton("Bouton")
        # connection du signal clicked avec la méthode définie plus loin
        bouton_outils.clicked.connect(self.bouton_outils_appuye)
        self.barre_outils.addWidget(bouton_outils)
        self.addToolBar(self.barre_outils)

        # Ajout de la barre de statut
        self.barre_statut = QStatusBar(self)
        self.setStatusBar(self.barre_statut)
        # Affichage d'un message temporaire dans la barre de statut (10 secondes)
        self.barre_statut.showMessage("Message de la barre de statut", 10000)

    def afficher_message_menu1(self):
        self.barre_statut.setStatusTip("Menu 1")

    def afficher_message_menu2(self):
        self.barre_statut.setStatusTip("Menu 2")

    def bouton_outils_appuye(self):
        print("Click!!!!")


app = QApplication()
base_ui = BaseUI()
base_ui.show()
app.exec()



