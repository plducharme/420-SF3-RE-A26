from PySide6.QtWidgets import QGridLayout, QApplication, QMainWindow, QPushButton, QWidget, QLabel


class FenetrePrincipale(QMainWindow):
    def __init__(self):
        super().__init__()

        widget_central = QWidget()
        disposition_grid = QGridLayout()
        widget_central.setLayout(disposition_grid)

        # Boucle pour la ligne
        for i in range(4):
            # Boucle pour la colonne
            for j in range(4):
                bouton = QPushButton("(" + str(i) + ", " + str(j) + ")")
                disposition_grid.addWidget(bouton, i, j)

        label_colonne = QLabel("Sur deux colonnes")
        # addWidget(widget, row, column, rowspan, colspan)
        disposition_grid.addWidget(label_colonne, 4, 0, 1, 2)
        label_ligne = QLabel("Sur deux lignes")
        disposition_grid.addWidget(label_ligne, 4, 2, 2, 1)
        label_seul = QLabel("(4, 3)")
        disposition_grid.addWidget(label_seul, 4, 3)
        label_50 = QLabel("(5, 0)")
        disposition_grid.addWidget(label_50, 5, 0)
        label_51 = QLabel("(5, 1)")
        disposition_grid.addWidget(label_51, 5, 1)
        self.setCentralWidget(widget_central)


app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()