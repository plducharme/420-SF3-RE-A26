from PySide6.QtWidgets import QApplication, QVBoxLayout, QLabel, QMainWindow, QWidget


class ExempleQVBoxLayout(QMainWindow):

    def __init__(self):
        super().__init__()

        # Les dispositions seront vues en détails dans un cours subséquents. Ceci est un exemple commenté pour vous
        # donner un aperçu. QVBoxLayout empile verticalement par le bas.

        # Une disposition s'applique à n'importe quel widget, comme on veut juste utilisé la disposition, on peut la
        # créer sur un QWidget générique.
        widget_central = QWidget()
        # On l'assigne à l'emplacement central
        self.setCentralWidget(widget_central)

        # On créé la disposition
        disposition = QVBoxLayout()
        # On l'assigne au widget_central
        widget_central.setLayout(disposition)

        # On ajout des widgets qui vont s'empiler, dans ce cas-ci des QLabel
        etiquette_1 = QLabel("widget 1")
        disposition.addWidget(etiquette_1)
        etiquette_2 = QLabel("widget 2")
        disposition.addWidget(etiquette_2)
        etiquette_3 = QLabel("widget 3")
        disposition.addWidget(etiquette_3)


app = QApplication()
exl = ExempleQVBoxLayout()
exl.show()
app.exec()