from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QWidget


class Fenetre(QMainWindow):

    def __init__(self):
        super().__init__()
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        disposition = QVBoxLayout()
        self.etiquette = QLabel("")
        edit = QLineEdit()

        # le signal textChanged du QLine Edit émet une str contenant le nouveau texte. En le connectant à la
        # fente (slot) edit_textChanged, textChanged sera appelée avec la str contenant le nouveau texte en
        # paramètre.
        edit.textChanged.connect(self.edit_text_changed)

        disposition.addWidget(self.etiquette)
        disposition.addWidget(edit)
        widget_central.setLayout(disposition)

    def edit_text_changed(self, nouveau_text: str):
        self.etiquette.setText(nouveau_text)


app = QApplication()
fenetre = Fenetre()
fenetre.show()
app.exec()