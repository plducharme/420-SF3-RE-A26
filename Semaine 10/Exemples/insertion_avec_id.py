from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit
import sqlite3


class ExempleInsertion(QMainWindow):

    def __init__(self):
        super().__init__()

        widget = QWidget()
        disposition = QVBoxLayout()
        widget.setLayout(disposition)

        self.textarea = QTextEdit()
        self.textarea.setReadOnly(True)
        disposition.addWidget(self.textarea)
        self.setCentralWidget(widget)

        self.textarea.append("Creation de la BD")
        insertion_bd = InsertionDB()
        insertion_bd.creer_bd()
        self.textarea.append("\nInsertion d'un légume")
        carotte_id = insertion_bd.inserer("carotte", "orange")
        self.textarea.append("\nId inséré: " + str(carotte_id))
        betterave_id = insertion_bd.inserer("betterave", "mauve")
        self.textarea.append("\nId inséré: " + str(betterave_id))


class InsertionDB:
    def __init__(self):
        self.connexion = sqlite3.connect("legumes.db")
        self.curseur = self.connexion.cursor()

    def creer_bd(self):
        self.curseur.execute("DROP TABLE IF EXISTS LEGUME")
        self.curseur.execute("CREATE TABLE LEGUME(legumeId INTEGER PRIMARY KEY autoincrement, nom NOT NULL, couleur)")

    # Insère dans la BD et retourne le id inséré
    def inserer(self, nom: str, couleur: str) -> int:
        self.curseur.execute("INSERT INTO LEGUME(nom, couleur) VALUES('" + nom + "', '" + couleur + "')")
        self.connexion.commit()
        return self.curseur.lastrowid


app = QApplication()
ex = ExempleInsertion()
ex.show()
app.exec()