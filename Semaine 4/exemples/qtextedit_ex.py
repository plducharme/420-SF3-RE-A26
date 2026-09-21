from PySide6.QtWidgets import QApplication, QFrame, QVBoxLayout, QHBoxLayout, QTextEdit, QCheckBox, QPushButton
from PySide6.QtCore import Qt


class EditeurTexte(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Éditeur de texte simple")

        disposition = QVBoxLayout()
        self.setLayout(disposition)

        self.texte_edit = QTextEdit()
        self.texte_edit.setText("C'est dans <b>nos moments</b> les plus sombres\n "
                                "que nous devons nous concentrer pour voir la lumière.")
        disposition.addWidget(self.texte_edit)

        disposition_boutons = QHBoxLayout()
        disposition.addLayout(disposition_boutons)

        self.bouton_gras_tout = QCheckBox("Gras tout")
        self.bouton_gras_tout.checkStateChanged.connect(self.bouton_gras_tout_changed)
        disposition_boutons.addWidget(self.bouton_gras_tout)

        self.bouton_italique_tout = QCheckBox("Italique")
        self.bouton_italique_tout.checkStateChanged.connect(self.bouton_italique_tout_changed)
        disposition_boutons.addWidget(self.bouton_italique_tout)

        self.bouton_gras_texte = QPushButton("G")
        self.bouton_gras_texte.clicked.connect(self.bouton_gras_texte_clicked)
        disposition_boutons.addWidget(self.bouton_gras_texte)

    def bouton_gras_tout_changed(self, etat):
        if etat == Qt.CheckState.Checked:
            police = self.texte_edit.font()
            police.setBold(True)
            self.texte_edit.setFont(police)
        else:
            police = self.texte_edit.font()
            police.setBold(False)
            self.texte_edit.setFont(police)

    def bouton_italique_tout_changed(self, etat):
        if etat == Qt.CheckState.Checked:
            police = self.texte_edit.font()
            police.setItalic(True)
            self.texte_edit.setFont(police)
        else:
            police = self.texte_edit.font()
            police.setItalic(False)
            self.texte_edit.setFont(police)

    def bouton_gras_texte_clicked(self):
        texte = self.texte_edit.textCursor().selectedText()
        texte = f"<b>{texte}</b>"
        self.texte_edit.textCursor().insertHtml(texte)


app = QApplication()
et = EditeurTexte()
et.show()
app.exec()
