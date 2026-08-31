from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QToolBar, QMenuBar, QMenu, QWidget
from PySide6.QtGui import QAction, QIcon, QMovie, QKeySequence


class FenetrePrincipale(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lecteur de GIFs")

        # Ajout d'un widget avec une disposition contenant l'étiquette
        disposition = QVBoxLayout()
        etiquette = QLabel()
        disposition.addWidget(etiquette)
        widget_central = QWidget()
        widget_central.setLayout(disposition)
        self.setCentralWidget(widget_central)

        # Initialisation de l'animation et assignation à l'étiquette
        self.animation = QMovie("sup.gif")
        etiquette.setMovie(self.animation)
        # Débuter l'animation
        self.animation.start()

        # Création des actions (ne pas oublié d'assigner le parent (self dans ce cas-ci)
        action_jouer = QAction(QIcon("jouer.png"), "Jouer", self)
        action_jouer.triggered.connect(self.jouer)

        action_stop = QAction(QIcon("stop.png"), "Stop", self)
        action_stop.triggered.connect(self.stop)

        action_quitter = QAction("Quitter", self)
        action_quitter.setText("&Quitter")
        # Ajout d'un raccourci clavier pour quitter
        action_quitter.setShortcut(QKeySequence("Ctrl+Q"))
        action_quitter.triggered.connect(self.close)

        # Création de la barre d'outils et ajout des actions à celle-ci
        barre_outils = QToolBar("Barre outils")
        barre_outils.addAction(action_jouer)
        barre_outils.addAction(action_stop)
        self.addToolBar(barre_outils)

        # Création de la barre de menu
        barre_menu = QMenuBar()

        # Création du menu de contrôles et ajout des actions
        menu_controles = QMenu("&Contrôles")
        menu_controles.addAction(action_jouer)
        menu_controles.addAction(action_stop)
        # Ajoute un séparateur avant la prochaine action
        menu_controles.addSeparator()
        menu_controles.addAction(action_quitter)

        barre_menu.addMenu(menu_controles)
        self.setMenuBar(barre_menu)

    def jouer(self):
        self.animation.start()

    def stop(self):
        self.animation.stop()


app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()
