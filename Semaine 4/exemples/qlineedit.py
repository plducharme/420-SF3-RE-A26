from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QGridLayout, QWidget, QTextEdit


class FenetrePrincipale(QMainWindow):

    def __init__(self):
        super().__init__()

        widget_central = QWidget()
        # Cette fois-ci, on utilise un QGridLayout comme disposition
        disposition = QGridLayout()
        widget_central.setLayout(disposition)
        self.setCentralWidget(widget_central)

        entree_base = QLineEdit()
        disposition.addWidget(entree_base, 0, 0)

        entree_mdp = QLineEdit()
        entree_mdp.setEchoMode(QLineEdit.EchoMode.Password)
        disposition.addWidget(entree_mdp, 0, 1)

        entree_masque = QLineEdit()
        entree_masque.setInputMask("(999)-999-9999")
        disposition.addWidget(entree_masque, 1, 0)

        texte_edit = QTextEdit()
        disposition.addWidget(texte_edit, 1, 1)


app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()


