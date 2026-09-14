from PySide6.QtWidgets import QFrame, QApplication, QLabel, QMenu, QVBoxLayout
from PySide6.QtGui import QPixmap, QFont


class Exercice1(QFrame):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exercice 1")
        # Cette fois-ci, nous avons hérité de QFrame au lieu de QMainWindow.
        # Nous n'avons donc pas de barre de menu par défaut.
        disposition = QVBoxLayout()
        self.setLayout(disposition)

        # Lorsque l'on a seulement un menu, on peut l'ajouter directement à la disposition au lieu de le regrouper
        # dans une barre de menu.
        self.menu = QMenu("Menu")
        action_quitter = self.menu.addAction("Quitter")
        action_quitter.triggered.connect(self.close)
        action_renommer = self.menu.addAction("Renommer")
        action_renommer.triggered.connect(lambda : self.setWindowTitle("Titre modifié"))

        libelle_texte_riche = QLabel()
        # Cette version utilise du HTML pour le texte riche
        libelle_texte_riche.setText(
            "<h1>Texte riche</h1>"
            "<p style='color:blue;'>Ceci est un texte en <b>gras</b> et en <i>italique</i>.</p>"
            "<p style='color:green;'>Voici une liste:</p>"
            "<ul>"
            "<li>Élément 1</li>"
            "<li>Élément 2</li>"
            "<li>Élément 3</li>"
            "</ul>"
            "<p style='color:red;'>Voici un lien vers <a href='https://www.w3schools.com/Html/default.asp'>Tutoriel HTML</a></p>"
        )
        disposition.addWidget(libelle_texte_riche)

        libelle_image = QLabel()
        # Cette version utilise une image
        # Un QPixmap est un objet qui représente une image
        image = QPixmap("./ex1.png")
        libelle_image.setPixmap(image)
        libelle_image.setFrameShadow(QFrame.Shadow.Sunken)
        disposition.addWidget(libelle_image)

        # Autre version pour du texte riche, ceci s'appliquera à tout le texte
        libelle_texte_riche2 = QLabel()
        libelle_texte_riche2.setText("Texte riche avec QFont")
        police = QFont()
        police.setBold(True)
        police.setPointSize(24)
        police.setItalic(True)
        police.setFamily("Lydian")
        libelle_texte_riche2.setFont(police)
        disposition.addWidget(libelle_texte_riche2)


app = QApplication()
ex1 = Exercice1()
ex1.show()
app.exec()

