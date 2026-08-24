from PySide6.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu, QWidget
from PySide6.QtGui import QAction, QIcon
from random import choice
import logging


# Créer une application avec une icône dans la barre système (system tray) qui contient un menu contextuel permettant
# de modifier la couleur de l'arrière-plan du widget. On peut seulement quitter l'application via l'icône
# Contient aussi un exemple de logger
class FenetrePrincipale(QMainWindow):

    def __init__(self):
        super().__init__()
        # Initialisation du logger. Avec la limite logging.INFO, les logs INFO, WARNING, ERROR et CRITICAL seront
        # "logged"
        logging.basicConfig(level=logging.INFO)
        self.widget_central = QWidget()
        self.setCentralWidget(self.widget_central)
        self.setWindowTitle("Exemple icône barre de système")

        # Créer l'icône à utiliser
        # <a href="https://www.flaticon.com/free-icons/concert" title="concert icons">Concert icons created by Freepik - Flaticon</a>
        icone = QIcon("./images/rock.png")

        # Créer l'icône dans la barre système, la barre système est similaire à une barre d'outils. On lui ajoute des
        # menus et des actions
        icone_systeme = QSystemTrayIcon(self)
        icone_systeme.setIcon(icone)

        menu = QMenu(parent=self)
        # Les actions ajoutées à ce QMenu doivent être une variable d'instance (ex: self.action) pour fonctionner
        self.action_quitter = QAction("Quitter")
        # Comme on empêche de quitter si on ferme la fenêtre, la méthode "quit()" doit être appelé explicitement
        # Alternativement, on aurait pu appeler "sys.exit" à la place
        self.action_quitter.triggered.connect(QApplication.instance().quit)
        menu.addAction(self.action_quitter)

        self.action_couleur = QAction("Échange Couleurs")
        self.action_couleur.triggered.connect(self.changer_couleur_action_clicked)
        menu.addAction(self.action_couleur)

        if QSystemTrayIcon.isSystemTrayAvailable():
            # Log de type information
            logging.info("Ajout de l'icône à la barre système")
            # On assigne notre menu à la barre de système
            icone_systeme.setContextMenu(menu)
            # Visible pour qu'il puisse apparaître
            icone_systeme.setVisible(True)
            icone_systeme.show()
        else:
            logging.error("Impossible d'ajouter l'icône à la barre système")

    def changer_couleur_action_clicked(self):
        couleurs = ["blue", "brown", "coral", "black", "silver", "gray", "red"]
        self.widget_central.setStyleSheet("QWidget {background-color: " + choice(couleurs) + ";}")



app = QApplication()
# On empêche de quitter lorsqu'il n'y a plus de fenêtre
app.setQuitOnLastWindowClosed(False)
fp = FenetrePrincipale()
fp.show()
app.exec()