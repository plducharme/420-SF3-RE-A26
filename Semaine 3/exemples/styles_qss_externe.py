from PySide6.QtWidgets import QApplication, QFrame, QPushButton, QVBoxLayout


class StylesExterne(QFrame):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Styles Externes")
        self.setObjectName("widgetprincipal")

        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)

        self.bouton1 = QPushButton("Mon bouton")
        # on utilise le nom de la classe QSS pour le nom d'objet
        self.bouton1.setObjectName("monbouton")
        self.disposition.addWidget(self.bouton1)

        self.bouton2 = QPushButton("Un autre bouton")
        self.bouton2.setObjectName("autrebouton")
        self.disposition.addWidget(self.bouton2)


app = QApplication()
# Lecture du fichier
with open("./styles.qss") as fichier:
    app.setStyleSheet(fichier.read())
se = StylesExterne()
se.show()
app.exec()
