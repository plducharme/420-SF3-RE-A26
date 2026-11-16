from PySide6.QtWidgets import QApplication, QMainWindow, QDockWidget, QWidget, QFrame, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class DockedExemple(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemple DockWidget")
        widget_central = QWidget()
        widget_central.setGeometry(0, 0, 100, 100)
        self.setCentralWidget(widget_central)

        # Créer une fenêtre de type QDockWidget
        self.fenetre1 = QDockWidget()
        self.fenetre1.setWindowTitle("fenêtre 1")
        # Contenu du dockwidget, on crée un widget avec notre contenu et on l'assigne au dockwidget
        self.contenu_fenetre1 = QFrame()
        self.disposition_fenetre1 = QVBoxLayout()
        self.contenu_fenetre1.setLayout(self.disposition_fenetre1)
        self.libelle_fenetre1 = QLabel("ceci est du contenu")
        self.disposition_fenetre1.addWidget(self.libelle_fenetre1)
        self.fenetre1.setWidget(self.contenu_fenetre1)

        # On assigne les fonctionnalités permises du QDockWidget (dans ce cas-ci, on a pas mis la possibilité de fermer
        # la fenêtre
        self.fenetre1.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetMovable |
                                  QDockWidget.DockWidgetFeature.DockWidgetFloatable)
        # ajouter la fenêtre dans la position de gauche par défaut
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.fenetre1)

        # Créer une fenêtre de type QDockWidget
        self.fenetre2 = QDockWidget()
        self.fenetre2.setWindowTitle("fenêtre 2")
        # ajouter la fenêtre dans la position de droite par défaut
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.fenetre2)

        # Créer une fenêtre de type QDockWidget
        self.fenetre3 = QDockWidget()
        self.fenetre3.setWindowTitle("fenêtre 3")
        # ajouter la fenêtre dans la position du bas par défaut
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.fenetre3)

        # Créer une fenêtre de type QDockWidget
        self.fenetre4 = QDockWidget()
        self.fenetre4.setWindowTitle("fenêtre 4")
        # ajouter la fenêtre dans la position du haut par défaut
        self.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, self.fenetre4)

        # Créer une fenêtre de type QDockWidget
        self.fenetre5 = QDockWidget()
        self.fenetre5.setWindowTitle("fenêtre 5")
        # ajouter la fenêtre dans la position de gauche par défaut
        self.addDockWidget(Qt.DockWidgetArea.NoDockWidgetArea, self.fenetre5)


app = QApplication()
ex = DockedExemple()
ex.show()
app.exec()